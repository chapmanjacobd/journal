-- Illirik Smirnov

SELECT
  user_email,
  TIMESTAMP_TRUNC(end_time, HOUR) AS query_time_hour,
  SUM(total_bytes_billed) / POW(2, 40) AS tib_billed
FROM
  `region-us`.INFORMATION_SCHEMA.JOBS
WHERE
  end_time BETWEEN TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) AND CURRENT_TIMESTAMP()
AND
  job_type = "QUERY"
AND
  statement_type != "SCRIPT"
AND
  cache_hit != true
GROUP BY 1, 2
ORDER BY 2 DESC, 3 DESC
;


SELECT
  -- These columns have information that's useful for identifying the function and/or source of costly queries
  cache_hit,
  creation_time,
  end_time,
  job_id,
  job_type,
  parent_job_id
  query,
  referenced_tables,
  state,
  statement_type,
  total_bytes_billed,
  total_bytes_processed,
  total_slot_ms,
  user_email
FROM
  `region-us`.INFORMATION_SCHEMA.JOBS
WHERE
  creation_time BETWEEN TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) AND CURRENT_TIMESTAMP()
AND
  job_type = "QUERY"
AND
  statement_type != "SCRIPT"
AND
  cache_hit != true

;

DECLARE bytes_per_tib INT64 DEFAULT 1024 * 1024 * 1024 * 1024;
DECLARE cost_per_tib INT64 DEFAULT 5;
DECLARE lookback_period_hrs INT64 DEFAULT 24 * 7;

WITH

  time_spine AS (
    SELECT
        *
    FROM 
        UNNEST(
            GENERATE_TIMESTAMP_ARRAY(
                TIMESTAMP_SUB(
                    TIMESTAMP_TRUNC(
                        CURRENT_TIMESTAMP(),
                        HOUR
                    ),
                    INTERVAL lookback_period_hrs HOUR
                ),
                TIMESTAMP_TRUNC(
                    CURRENT_TIMESTAMP(),
                    HOUR
                ),
                INTERVAL 1 HOUR
            )
        ) AS query_time_hour
    ),

  user_emails AS (
    SELECT DISTINCT user_email FROM `region-us`.INFORMATION_SCHEMA.JOBS
  ),

  time_spine_with_user_emails AS (
    SELECT
        user_email,
        query_time_hour
    FROM
        user_emails
    CROSS JOIN
        time_spine
  ),

  bq_usage_by_hour AS (
    SELECT
        user_email,
        TIMESTAMP_TRUNC(end_time, HOUR) AS query_time_hour,
        SUM(total_bytes_billed) / bytes_per_tib AS tib_billed,
        COUNT(*) AS queries_run,
        SUM(total_slot_ms) / 1000 AS total_slot_seconds
    FROM
        `region-us`.INFORMATION_SCHEMA.JOBS
    WHERE
        end_time BETWEEN TIMESTAMP_SUB(TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), HOUR), INTERVAL lookback_period_hrs HOUR) AND CURRENT_TIMESTAMP()
    AND
        job_type = "QUERY"
    AND
        statement_type != "SCRIPT"
    AND
        cache_hit != true
    GROUP BY 1, 2
  ),

  bq_usage_with_timespine AS (
    SELECT
        COALESCE(bq_usage_by_hour.user_email, time_spine_with_user_emails.user_email) AS user_email,
        COALESCE(bq_usage_by_hour.query_time_hour, time_spine_with_user_emails.query_time_hour) AS query_time_hour,
        IFNULL(tib_billed, 0) AS tib_billed,
        IFNULL(tib_billed, 0) * cost_per_tib AS dollars_cost,
        IFNULL(queries_run, 0) AS queries_run,
        IFNULL(total_slot_seconds, 0) AS total_slot_seconds
    FROM
        time_spine_with_user_emails
    LEFT JOIN
        bq_usage_by_hour
    USING
        (user_email, query_time_hour)
  )

SELECT
    *,
    AVG(tib_billed)
    OVER(
        PARTITION BY user_email
        ORDER BY query_time_hour
        ROWS BETWEEN 23 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_tib_billed,
    AVG(dollars_cost)
    OVER(
        PARTITION BY user_email
        ORDER BY query_time_hour
        ROWS BETWEEN 23 PRECEDING AND CURRENT ROW
    ) AS rolling_avg_dollars_cost
FROM
    bq_usage_with_timespine


;

WITH
    total_tib_billed_last_7d AS (
        SELECT
            user_email,
            SUM(tib_billed) AS total_tib_billed
        FROM
            costs_data
        GROUP BY 1
    )
SELECT
    user_email,
    total_tib_billed,
    RANK() OVER(ORDER BY total_tib_billed DESC) AS usage_rank
FROM
    total_tib_billed_last_7d
ORDER BY 3

;

-- Get all queries run in the last 24h,
-- if spend over last 24h was greater than 24h_spend_limit

{% set spend_last_24h_query %}
SELECT
  SUM(dollars_billed)
FROM
  -- Model that aggregates BQ spend per hour
  {{ ref("bq_spend_per_hour") }}
WHERE
  query_hour >= TIMESTAMP_SUB(
    TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), HOUR),
    INTERVAL 24 HOUR
  )
{% endset %}
{% set results = run_query(spend_last_24h_query) %}
{% if execute %}
-- Return the first value from the first column
{% set spend_last_24h = results.columns[0][0] %}
{% else %}
{% set spend_last_24h = 0 %}
{% endif %}
SELECT
  *
FROM
  {{ ref("bq_spend_per_hour") }}
WHERE
  query_end >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 24 HOUR)
AND
  {{ spend_last_24h }} > {{ 24h_spend_limit }}
;

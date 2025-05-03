SELECT widget_id, ((positive + 1.9208) / (positive + negative) - 
                   1.96 * SQRT((positive * negative) / (positive + negative) + 0.9604) / 
                          (positive + negative)) / (1 + 3.8416 / (positive + negative)) 
       AS ci_lower_bound FROM widgets WHERE positive + negative > 0 
       ORDER BY ci_lower_bound DESC;

-- https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

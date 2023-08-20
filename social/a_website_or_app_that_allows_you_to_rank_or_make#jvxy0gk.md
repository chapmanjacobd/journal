I would use a spreadsheet to manually rank things... For example, Google Sheets. 

First, sort similar items together. You could do this by creating another column called "category" and assigning things into a fixed number of categories. After that, rank items within their category. Then rank categories against other categories. Finally, you can either sort by (category_rank, item_rank) or by using some formula like `category_rank * item_rank`.

But if you want to rank things based on many, many other ranks you could do something like this: [multi_rank.py](https://gist.github.com/chapmanjacobd/37d61693add62adb66b085e4e095aba1) 

Or if you want to weigh how important some categories are over others you should look into more robust [MCDA](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis#Solving_MCDM_problems). The most popular of these are SMART and AHP--but there are better options too: https://en.wikipedia.org/wiki/Preference_ranking_organization_method_for_enrichment_evaluation#The_mathematical_model

These might be relevant:

- https://decision-radar.com
- https://www.surveymonkey.com/market-research/resources/how-to-use-conjoint-analysis/
- https://conjointly.com/products/survey-tool/

edit: If you want a website to allow other people to vote over a list of 300 items, you should try to follow Tom Scott's methodology. Either randomize and have people vote between two items; or create a many surveys containing around ten items or less and exclude lower ranking items with each iteration of the survey. Online voting is difficult to do if you want unbiased results. The main concerns are overwhelming people with too many options and blocking vote-spamming

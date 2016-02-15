# Botify Query DSL

Botify Query DSL (BQL) simplifies the interaction between API users and Botify backend systems by providing an intermediate abstraction. It also facilitates the evolution of our data system since it helps decouple the API and the backends.

BQL provides following search/aggregation abilities on a per-URL basis on the analysis dataset:
  - Retrieve data fields
  - Filtering URL documents based on data fields
  - Sorting on retrieved results
  - Aggregation and nested-aggregation
  - Data models introspection


## Area

In almost every **analysis** endpoint dealing with URL Data model, an **area parameter** is present (its default value is `current`). It refers to the subset of URL to compute on:

![screenshot from 2016-01-08 11 49 14](https://cloud.githubusercontent.com/assets/1886834/12196436/df1d2632-b5fe-11e5-9f7a-04197d49a49f.png)
*URLs distribution chart available in movements tab of analysis report.*

- **current**: URLs that were crawled in the current analysis (blue and purple part)
- **new**: URLs crawled in the current analysis but not in the previous analysis (blue part)
- **disappeared**: URLs crawled in the previous analysis but not in the current analysis (red part)


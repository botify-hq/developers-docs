# Aggregate Analyses URLs

Using Botify API, you can **aggregate analyzed URLs** to compute metrics like sum of inlinks, average load time, etc. You can also **group URLs** on any aggregable field and compute metrics on each group. Full list of aggregable fields can be found in [[Analysis Datamodel;analysis-datamodel?filter=agg:]].
The following descirbe how to **perform aggregations on several project's analyses at a time**.

## Endpoint

- Operation: [[getProjectUrlsAggs;reference#/Project/getProjectUrlsAggs]]
- Path: `/projects/{username}/{project_slug}/urls/aggs`
- HTTP Verb: POST
- Body : `Array<BQLAggsQuery>`
- Response: `Array<BQLAggsResult>`

Please refer to [[BQLAggsQuery;bql-aggs-query]] documentation for information about input or refer to the following request examples.

```SH
curl "https://api.botify.com/v1/projects/${username}/${project_slug}/urls/aggs?last_analysis_slug=${analysis_slug}&nb_analyses=${count}" \
     -X POST \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json" \
     --data-binary "${UrlsAggsQueries}"
```

## Example

The following example of [[BQLAggsQuery;bql-aggs-query]] computes the sum of SEO visits for last analyses (according to `last_analysis_slug` & `nb_analyses` you asked).

### Request
```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          { "sum": "visits.organic.all.nb" }
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns a two dimensional array (number of queries * number of analyses).

Analyses are ordered from the latest to the oldest. For each one, their analysis slug and their start and finish date is given allowing you to display trend lines for instance.
`data.count` is the number of URLs matching the query (in case you filtered it).
`data.aggs` is the result of the aggregation. In the example, the sum of SEO visits is 104 for the last analysis.

```JSON
[
  [
    {
      "status": 200,
      "analysis_slug": "20161208",
      "date_finished": "2016-12-08 14:52:48.145643+00:00",
      "date_started": "2016-12-08 14:45:25.879995+00:00",
      "data": {
        "count": 42,
        "aggs": [
          {
            "metrics": [104.0]
          }
        ]
      }
    },
    {
      "status": 200,
      "analysis_slug": "20161207-2",
      "date_finished": "2016-12-07 18:28:04.774742+00:00",
      "date_started": "2016-12-07 18:21:43.595681+00:00",
      "data": {
        "count": 38,
        "aggs": [
          {
            "metrics": [98.0]
          }
        ]
      }
    },
    {
      "status": 200,
      "analysis_slug": "20161207",
      "date_finished": "2016-12-07 14:40:54.113411+00:00",
      "date_started": "2016-12-07 14:24:23.588670+00:00",
      "data": {
        "count": 38,
        "aggs": [
          {
            "metrics": [98.0]
          }
        ]
      }
    },
  ]
]
```

## Further examples

For further examples of aggregation including multiple groupby and filtering please refer to [[Aggregate URLs documentation;analysis-aggregate-urls#examples]].

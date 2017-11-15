# Aggregate URLs

Using the Botify API, you can **aggregate logs URLs** to compute metrics like the sum of visits in January, the number of crawls by day in January or the number of 404 URLs by segment in the last month.
Please refer to [[logs segments datamodel;logs-datamodel?datamodel=segments]] to find the list of [[aggregable fields;logs-datamodel?datamodel=segments&filter=agg:]] and [[filterable fields;logs-datamodel?datamodel=segments&filter=filters]].

## Endpoint
- Operation: [[getLogsSegmentsAggs;reference#/Logs/getLogsSegmentsAggs]]
- Path: `POST /logs/{username}/{project_slug}/segments/{date_start}/{date_end}/aggs`
- HTTP Verb: POST
- Body : `Array<BQLAggsQuery>`
- Response: `Array<BQLAggsResult>`

`date_start` and `date_end` define the period you want to work on. Date format is `YYYYMMDD`.
Please refer to [[BQLAggsQuery;bql-aggs-query]] documentation for information about input or refer to the following request examples.

```SH
curl "https://api.botify.com/v1/logs/${username}/${project_slug}/segments/${date_start}/${date_end}/aggs" \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json" \
     --data-binary "${UrlsAggsQueries}"
```


## Examples

- [Two metrics on a filtered dataset](#example-two-metrics-on-a-filtered-dataset)
- [Metrics on timeseries fields](#example-metrics-on-timeseries-fields)
- [Group-by with two metrics](#example-group-by-with-two-metrics)


## Example: Two metrics on a filtered dataset

The following example of [[BQLAggsQuery;bql-aggs-query]] computes the number visits and the number of URLs crawled or visited in January 2016 for article pages.

### Request
With `date_start = '20160101'` and `date_end = '20160131'`,
```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          { "sum": "visits.google.count" },
          { "sum": "crawls_or_visits.google.count_unique" }
        ]
      }
    ],
    "filters": {
      "field": "segments.segment_1.depth_1",
      "value": "articles"
    }
  }
]
```

### Response
A sample result would be the following. `status` is the status code of the request: 200 OK, 400 client error (query is invalid).
When everything went fine, aggregation response is in the `data` key. Requested metrics are returned in the same order they were set in the query.

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 37,
      "aggs": [
        {
          "metrics": [147725, 14544]
        }
      ]
    }
  }
]
```

## Example: Metrics on timeseries fields

The following example of [[BQLAggsQuery;bql-aggs-query]] computes the number crawls and visits by day in the first 7 days of January 2016.
### Request
With `date_start = '20160101'` and `date_end = '20160107'`,
```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          { "sum": "crawls.google.count_by_day" },
          { "sum": "visits.google.count_by_day" }
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns a two metrics with first, the total number of crawls by day and second the number of visits by day.

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 37,
      "aggs": [
        {
          "metrics": [
            [154979,168833,143881,140323,137696,130841,136991],
            [265495,272913,246233,239646,253667,229387,174781]
          ]
        }
      ]
    }
  }
]
```


## Example: Group-by with two metrics

The following example of [[BQLAggsQuery;bql-aggs-query]] computes the total number of 404 crawls within the first 7 days of January 2016, and the number of crawls by day for each segment.

### Request
With `date_start = '20160101'` and `date_end = '20160107'`,
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "segments.segment_1.value"
        ],
        "metrics": [
          { "sum": "crawls.google.http_codes.404.count" }
          { "sum": "crawls.google.http_codes.404.count_by_day" }
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs and the result of the aggregation.

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 1,
      "aggs": [
        {
          "groups": [
            {
              "key": ["home"],
              "metrics": [
                661,
                [54, 64, 60, 178, 188, 94, 23]
              ]
            },
            {
              "key": ["articles"],
              "metrics": [
                27608,
                [3389, 5952, 3354, 3054, 2774, 3673, 5412]
              ]
            },
            {
              "key": ["authors"],
              "metrics": [
                1,
                [1, 0, 0, 0, 0, 0, 0]
              ]
            }
          ]
        }
      ]
    }
  }
]
```

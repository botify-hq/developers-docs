# Aggregate URLs

Using the Botify API, you can **aggregate analyzed URLs** to compute metrics like the number of compliant URLs, the distribution of visits by segment or the sum of URLs by HTTP code and depth.
Please refer to [[analysis datamodel;analysis-datamodel]] to find the list of [[aggregable fields;analysis-datamodel?filter=agg:]] and [[filterable fields;analysis-datamodel?filter=filters]].


## Endpoint

- Operation: [[getUrlsAggs;reference#/Analysis/getUrlsAggs]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls/aggs`
- HTTP Verb: POST
- Body : `Array<BQLAggsQuery>`
- Response: `Array<BQLAggsResult>`

Please refer to [[BQLAggsQuery;bql-aggs-query]] documentation for information about input or refer to the following request examples.

```SH
curl "https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}/urls/aggs" \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json" \
     --data-binary "${UrlsAggsQueries}"
```


## Examples

- [Two metrics on a filtered dataset](#example-two-metrics-on-a-filtered-dataset)
- [Group-by with two metrics](#example-group-by-with-two-metrics)
- [Range group-by](#example-range-group-by)
- [Two group-bys](#example-two-group-bys)


## Example: Two metrics on a filtered dataset

The following example of [[BQLAggsQuery;bql-aggs-query]] computes the number of compliant URLs and their average response time.

### Request
```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          "count",
          { "avg": "delay_last_byte" }
        ]
      }
    ],
    "filters": {
      "field": "compliant.is_compliant",
      "predicate": "eq",
      "value": true
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
          "metrics": [37, 118.52380952380952]
        }
      ]
    }
  }
]
```


## Example: Group-by with two metrics

The following example of [[BQLAggsQuery;bql-aggs-query]] groups URLs by HTTP Code. Using `metrics` key, we request the number of URLs and average response time for each group of HTTP Code.

### Request
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "http_code"
        ],
        "metrics": [
          "count",
          { "avg": "delay_last_byte" }
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs and the result of the aggregation.

This example returns 2 groups:
- the URLs with HTTP code 200
- the URLs with HTTP code 301

For each group, requested metrics are returned in the same order they were in the query.

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 37,
      "aggs": [
        {
          "groups": [
            {
              "key": [200],
              "metrics": [28, 157.25]
            },
            {
              "key": [301],
              "metrics": [2, 751.25]
            }
          ]
        }
      ]
    }
  }
]
```


## Example: Range group-by

The following example of [[BQLAggsQuery;bql-aggs-query]] groups active URLs by response time in 2 groups (fast and slow URLs). The URLs dataset is filtered on compliant URLs using `filters` key.
**Note:** The default `metric` is `count`.

### Request
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          {
            "range": {
              "field": "delay_last_byte",
              "ranges": [
                {"from": 0, "to": 1000},
                {"from": 1000}
              ]
            }
          }
        ]
      }
    ],
    "filters": {
      "field": "visits.organic.all.active",
      "predicate": "eq",
      "value": true
    }
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs matching the filter and the result of the aggregation. The response returns the number of URLs for slow and fast URLs as request.

Note that **groups may not be in the same order you specified in ranges** due to multiple groupby capability, cf. bellow (ie. in the query, even you defined slow then fast URLs, responses can give the result for fast then slow URLs)

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 25,
      "aggs": [
        {
          "groups": [
            {
              "key": [{"from": 0, "to": 1000}],
              "metrics": [4]
            },
            {
              "key": [{"from": 1000}],
              "metrics": [19]
            },
          ]
        }
      ]
    }
  }
]
```


## Example: Two group-bys

The following example of [[BQLAggsQuery;bql-aggs-query]] groups URLs by depth and HTTP code.
**Note:** The default `metric` is `count`.

### Request
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "depth",
          "http_code"
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs matching the filter and the result of the aggregation.

It creates a group for each combination. For instance:
- the URLS on depth 1 with a 200 HTTP code.
- the URLS on depth 1 with a 301 HTTP code.
- the URLS on depth 2 with a 200 HTTP code.

**Note that combinations resulting to 0 URLs (ex: 301s on depth 2) are not returned.**

```JSON
[
  {
    "status": 200,
    "data": {
      "count": 25,
      "aggs": [
        {
          "groups": [
            {
              "key": [1, 200],
              "metrics": [4]
            },
            {
              "key": [1, 301],
              "metrics": [2]
            },
            {
              "key": [2, 200],
              "metrics": [19]
            }
          ]
        }
      ]
    }
  }
]
```

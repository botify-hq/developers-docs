# URLs Aggregation

Using Botify API, you can aggregate URLs to compute metrics like sum of inlinks, avegare load time, etc. You can also group URLs on any aggregable field and compute metrics on each group. **Full list of aggregable fields** can be found in [[Urls Datamodel;urls-datamodel#agg]].

## Endpoint

- Operation: [[getUrlsAggs;reference#Analysis_getUrlsAggs]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls/aggs`
- HTTP Verb: POST
- Body : `Array<UrlsAggsQuery>`
- Response: `Array<UrlsAggsResult>`

Please refer to [[UrlsAggsQuery;bql#urlsaggsquery]] documentation for information about input.

```SH
curl 'https://api.botify.com/analyses/${username}/${project_slug}/${analysis_slug}/urls/aggs' \
     -X POST \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json' \
     --data-binary '${UrlsAggsQueries}'
```


## Example: Aggregation on filtered dataset

The following example of [[UrlsAggsQuery;bql#urlsaggsquery]] compute the number of compliant URLs and their average response time.

### Request
```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          "count",
          {
            "avg": "delay_last_byte"
          }
        ]
      }
    ],
    "filters": {
      "field": "strategic.is_strategic",
      "predicate": "eq",
      "value": true
    }
  }
]
```

### Response
A sample result would be the following. Requested metrics are returned in the same order they were set in the query.

```JSON
[
  {
    "count": 37,
    "aggs": [
      {
        "metrics": [
          37,
          118.52380952380952,
        ],
      }
    ]
  }
]
```


## Example: Simple Group-By with two Metrics

The following example of [[UrlsAggsQuery;bql#urlsaggsquery]] groups URLs by HTTP Code. Using `metrics` key, we request the number of URLs and average response time for each group.

### Request
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "http_code",
        ],
        "metrics": [
          "count",
          {
            "avg": "delay_last_byte"
          }
        ]
      }
    ]
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs and the result of the aggregation.

This example returns 3 groups: the URLs with HTTP code 200, the URLs with HTTP code 201 and the URLs with HTTP code 404. For each group, requested metrics are returned in the same order they were set in the query.

```JSON
[
  {
    "count": 37,
    "aggs": [
      {
        "groups": [
          {
            "key": [
              200
            ],
            "metrics": [
              28,
              157.25
            ]
          },
          {
            "key": [
              201
            ],
            "metrics": [
              2,
              751.25
            ]
          },
          {
            "key": [
              404
            ],
            "metrics": [
              7,
              1809.8
            ]
          }
        ]
      }
    ]
  }
]
```


## Example: Simple and Range Group-By

The following example of [[UrlsAggsQuery;bql#urlsaggsquery]] groups URLs by HTTP code and response time on 2 ranges (fast and slow URLs). The URLs dataset is filtered on compliant URLs using `filters` key.

### Request
```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "http_code",
          {
            "range": {
              "field": "delay_last_byte",
              "ranges": [
                {
                  "from": 0,
                  "to": 1000
                },
                {
                  "from": 1000
                }
              ]
            }
          }
        ]
      }
    ],
    "filters": {
      "field": "strategic.is_strategic",
      "predicate": "eq",
      "value": true
    }
  }
]
```

### Response
A sample result would be the following. It returns the total number of URLs matching the filter and the result of the aggregation.

It creates a group for each combination of group-bys: the fast 200 URLs, the slow 200 URLs and the slow 201 URLs. **Note that combinations resulting to 0 URLs (fast 201 URLs) are not returned.**

**The default `metric` is `count`.**

```JSON
[
  {
    "count": 25,
    "aggs": [
      {
        "groups": [
          {
            "key": [
              200,
              {
                "from": 0,
                "to": 1000
              }
            ],
            "metrics": [
              4
            ]
          },
          {
            "key": [
              200,
              {
                "from": 1000
              }
            ],
            "metrics": [
              19
            ]
          },
          {
            "key": [
              201,
              {
                "from": 1000
              }
            ],
            "metrics": [
              2
            ]
          }
        ]
      }
    ]
  }
]
```

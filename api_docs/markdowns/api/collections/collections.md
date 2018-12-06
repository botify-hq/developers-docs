# Collections API -- Getting Started [Alpha Version]

## Summary

The goal of this API is to give the possibility to cross data from different sources and different periods on a given project. These data sources are named "collections" in this context. They represent data coming from Botify Analytics, Botify Log Analyzer, and Botify Keywords.

In the manner of an analytics tool, the collections API is queried by providing a set of dimensions and metrics to aggregate data.

## Data Querying Endpoint

- Operation: [[projectQuery;reference#/Project/projectQuery]]
- Path: `projects/{username}/{project_slug}/query`
- HTTP Verb: POST
- Response: `Pagination<BQL_COLLECTIONS_RESULT>`

Body:
```JSON
{
  "collections": [COLLECTIONS],
  "periods": [PERIODS],
  "query": BQL_COLLECTIONS_QUERY
}
```

### Collections

A Botify Project has multiple collections usable for querying. To retrieve the available collections one can query the endpoint:

- Operation: [[getProjectCollections;reference#/Collections/getProjectCollections]]
- Path: `projects/{username}/{project_slug}/collections`
- HTTP Verb: GET
- Response: `List<Collection>`

Three types of collections are to be distinguished:
- The `global` collection is unique and present on every project. It exposes dimensions that are available on all collections, like a project's segmentation, or base URL metrics.
- **Timestamped** collections represent data sets that evolve over time, for which we get a value for a date or time. They are always queried over a period ([start_date, end_date]). This includes, among others, the Log Analyzer, Keywords and Visits features.
- Non-timestamped collections. These collections represent a snapshot at a certain moment in time. This includes Botify Analytics crawl reports.

The most frequently used collections are:
- `crawl.YYYYMMDD`
- `search_console`
- `log_analyzer.google`

### Collection details

To get the available dimensions and metrics, a collection exposes the endpoint:
- Operation: [[getCollectionDetail;reference#/Collections/getCollectionDetail]]
- Path: `projects/{username}/{project_slug}/collections/{collection_id}`
- HTTP Verb: GET
- Response: `Datamodel`

The `collection_id` is being retrieved through the collections list endpoint. It is also the identifier used on the data querying endpoint to target the given collection.
For each field in the datamodel, a `kind` attributes specifies if a field is a dimension or a metric.

[comment]: # (TODO: somehow provide a list of available dimensions and metrics. Maybe not exhaustive, so not necessarily dynamic)

### Periods

A period represents the datespan on which a timestamped collection is queried. The format used for one period is a list of two dates in a "YYYY-MM-DD" format.
The dates on which a timestamped collection is available in the collections list endpoint through the *date_start* and *date_end* response keys.

### Collections BQL Query

A BQL Collection Query has the following format:
```JSON
{
  "dimensions": [DIMENSIONS],
  "metrics": [METRICS],
  "filters": FILTER,
  "sort": [SORTS]
}
```

#### Fields

Metrics and dimensions need to be prefixed with the collection from which they are queried.
For a non-timestamped collection, the prefix is just the collection id:
- `"{collection_id}.{field_slug}"`. For example: `"crawl.20180801.depth"`
For a timestamped collection, one needs to additionally specify the period index (0-based):
- `"{collection_id}.period_{idx}.{field_slug}"`. For example: `"search_console.period_0.count_clicks"`


"Global" dimensions, available on all collections, can be specified as such. No need to prefix them:
- `"{global_field_slug}"`. For example: `"url"`
An exception to this is the date field, which will only need to be prefixed by the period index to group multiple timestamped collections together on a certain date span:
- `"period_{idx}.date"`.


In dimensions, metrics and filters, [[BQL Functions can be used. See documentation.;bql-functions]]

#### Filters

[[The BQL Filter documentation is available here.;bql-filter]]

#### Sort

Each field on which we want to sort can be specified through the format:
```JSON
{
  "index": IDX,
  "type": TYPE,
  "order": ORDER
}
```
where:
- `IDX` is the 0-based index of the position of the field to sort
- `TYPE` can be `"dimensions"` or `"metrics"` (defaults to `"dimensions"`)
- `ORDER` can be `"asc"` or `"desc"` (defaults to `"asc"`)

### Collections BQL Response

The endpoint response is paginated and in JSON format. It is formalised as such:
```JSON
{
  "previous": LINK_TO_PREVIOUS_PAGE,
  "next": LINK_TO_NEXT_PAGE,
  "page": PAGE_NUMBER,
  "size": PAGE_SIZE,
  "results": [
    {
        "metrics": [METRIC_VALUES],
        "dimensions": [DIMENSION_VALUES]
    },
    ...
  ]
}
```

[comment]: # (TODO: add the count option information)

## Examples

First, a typical cURL pattern to use the collections API:

```bash
curl 'https://app.botify.com/api/v1/projects/{{username}}/{{project_slug}}/query?size=50' \
  --header 'Authorization: Token {{token}}' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --header 'X-Botify-Client: developers-doc' \
  --data 'BQL_COLLECTIONS_QUERY'
```

### Number of clicks by country during one month

```JSON
{
    "collections": [
        "search_console"
    ],
    "periods": [
      ["2018-08-01", "2018-08-30"]
    ],
    "query": {
        "dimensions": [
          "country"
        ],
        "metrics": [
          "search_console.period_0.count_clicks"
        ],
        "sort": [
          {"type": "metrics", "index": 0, "order": "desc"}
        ]
    }
}
```

### Average position of rankings (url+keyword couple) by date where the URL responded with a 200 HTTP Code on the crawl of August 29th 2018
```JSON
{
    "collections": [
        "search_console",
        "crawl.20180829"
    ],
    "periods": [
      ["2018-08-01", "2018-08-30"]
    ],
    "query": {
        "dimensions": [
          "url",
          "keyword",
          "period_0.date"
        ],
        "metrics": [
          "search_console.period_0.avg_position"
        ],
        "filters": {
          "field": "crawl.20180829.http_code",
          "predicate": "eq",
          "value": 200
        },
        "sort": [
          {"type": "dimensions", "index": 2, "order": "asc"}
        ]
    }
}
```

### Evolution of number of impressions of keywords between two months
```JSON
{
    "collections": [
        "search_console",
    ],
    "periods": [
      ["2018-08-01", "2018-08-30"],
      ["2018-09-01", "2018-09-30"]
    ],
    "query": {
        "dimensions": [
          "keyword"
        ],
        "metrics": [
          {
            "function": "sub",
            "args": [
              "search_console.period_1.count_impressions",
              "search_console.period_0.count_impressions"
            ]
          }
        ],
        "sort": [
          {"type": "metrics", "index": 0, "order": "desc"}
        ]
    }
}
```

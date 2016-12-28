# List and filter URLs

Botify API allows you to **list and filter logs URLs** and return their fields value (metadata). Full list of requestable fields can be found in [[logs URL datamodel;logs-datamodel]].


## Endpoint

- Operation: [[getLogsUrls;reference#/Logs/getLogsUrls]]
- Path: `logs/{username}/{project_slug}/urls/{date_start}/{date_end}`
- HTTP Verb: POST
- Body : `BQLQuery`
- Response: `Pagination<BQLResult>`

`date_start` and `date_end` define the period you want to work on. Date format is `YYYYMMDD`.
Please refer to [[BQLQuery;bql-query]] documentation for information about how to define fields to select, filters and sort.

```SH
curl 'https://api.botify.com/v1/logs/${username}/${project_slug}/urls/${date_start}/${date_end}' \
     -X POST \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json' \
     --data-binary '${BQLQuery}'
```

## Example

The following example of [[BQLQuery;bql-query]] returns the URLs which have been crawled at least once but have never been visited. It orders URLs by descending number of crawls. The filter on `segemnts.static` avoid listing static files like css or js sources.

```JSON
{
  "fields": [
    "url",
    "crawls.google.count_ever",
  ],
  "filters": {
    "and": [
      {
        "field": "crawls.google.count_ever",
        "predicate": "gt",
        "value": 0
      },
      {
        "field": "visits.google.count_ever",
        "predicate": "eq",
        "value": 0
      },
      {
        "field": "segments.static",
        "predicate": "eq",
        "value": false
      },
    ]
  },
  "sort": [
    { "crawls.google.count_ever": { "order": "desc" } }
  ]
}
```

A sample result would be:
```JSON
{
  "count": 11,
  "page": 1,
  "size": 2,
  "results": [
    {
      "url": "www.abc.com/1",
      "crawls": {
        "google": {
          "count_ever": 10837
        }
      }
    },
    {
      "url": "www.abc.com/2",
      "crawls": {
        "google": {
          "count_ever": 10426
        }
      }
    }
  ]
}
```

# Main

The main feature extracts every primary data from crawled URLs including depth, load time, HTTP codes, HTML tags, content type, language, no-index etc.

## URLs datamodel fields

[[Main feature's fields;analysis-urls-datamodel?feature=main]].


## Examples of Aggregation

The following examples uses [[URLs aggregation;analysis-aggregate-urls]] to metrics regarding main data.

### Number of compliant / not compliant URLs

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "compliant.is_compliant"
        ]
      }
    ]
  }
]
```

### Number of URLs by depth

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "depth"
        ]
      }
    ]
  }
]
```

### Number of URLs by group of HTTP code

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          {
            "range": {
              "field": "http_code",
              "ranges": [
                { "from": 200, "to": 300 },
                { "from": 300, "to": 400 },
                { "from": 400, "to": 500 },
                { "from": 500 },
                { "to": 200 }
              ]
            }
          }
        ]
      }
    ]
  }
]
```

# Links

The links feature is repsonsible for computing inlinks/outlinks for each URL, internal pagerank, internal follow outlinks destination, external follow outlinks destination (Top Domains), prev/next tags.


## Examples of Aggregation

The following examples uses [[URLs aggregation;analysis-aggregate-urls]] to metrics regarding main data.

### Number of internal inlinks by URL

```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          {
            "sum": "inlinks_internal.nb.follow.unique",
            "sum": "inlinks_internal.nb.nofollow.unique"
          }
        ]
      }
    ]
  }
]
```
**Note**: `unique` suffix means that 2 links to the same URL will be count only once. You can also compute the total number of inlinks by replacing `unique` suffix by `total`.


### Number of internal/external outlinks by URL

```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          {
            "sum": "outlinks_internal.nb.follow.unique",
            "sum": "outlinks_internal.nb.nofollow.unique",
            "sum": "outlinks_external.nb.follow.unique",
            "sum": "outlinks_external.nb.nofollow.unique"
          }
        ]
      }
    ]
  }
]
```
**Note**: `unique` suffix means that 2 links to the same URL will be count only once. You can also compute the total number of inlinks by replacing `unique` suffix by `total`.


### Number of internal outlinks to Bad HTTP Code URLs

```JSON
[
  {
    "aggs": [
      {
        "metrics": [
          {
            "sum": "outlinks_errors.3xx.nb",
            "sum": "outlinks_errors.4xx.nb",
            "sum": "outlinks_errors.5xx.nb"
          }
        ]
      }
    ]
  }
]
```

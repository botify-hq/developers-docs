# UrlsAggsQuery

`UrlsAggsQuery` is used for [[Urls Aggregation;usage-urls-aggregation]] to define aggregation to perform, metrics to compute, and filter to operate.

## Format
```JSON
{
  "aggs": [
    {
      "group_by": ?Array<GroupBy>,
      "metrics": Array<Metric>
    }
  ],
  "filters": ?UrlFilters
}
```

A `UrlsAggsQuery` is composed of a list of `Aggregate` and an optional `UrlFilters`. An `Aggregate` defines some `Metric` to compute. `GroupBys` can be used to group URLs and compute metrics on each groups.

### GroupBy
A `GroupBy` is defined by:
  - a `field` on which the group-by is performed.
  - some optional `ranges` that define buckets for the group-by operation.

#### Simple GroupBy
Only [[aggregables fields;urls-datamodel?filter=agg:]] can be used for group by operations.

**Example**
The following groups URLs by their `http_code`.
```JSON
{
  "field": "http_code"
}
```

#### Range GroupBy
Only [[numerical fields;urls-datamodel?filter=agg:numerical]] can be used for range group by operations.

**Example**
The following groups URLs by their `delay_last_byte` on two ranges (fast and slow URLs)
```JSON
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
```

### Metric
Metrics define the operation to compute. Except for `count`, a field on which the metric is applied must be provided. Available metrics are:
- `count`
- `sum`
- `avg`
- `min`
- `max`
Note: The default metric is `count`.

**Examples**
count of URLs
```JSON
"count"
```
Sum of internal inlinks nofollow
```JSON
{
  "sum": "inlinks_internal.nb.follow.total"
}
```


### `filters: UrlsFilter`

Please refer to [[UrlsFilter;bql-urls-filter]] documentation.


## Examples
Full examples in [[Urls Aggregation documentation;usage-urls-aggregation#example-aggregation-on-filtered-dataset]].

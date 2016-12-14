# BQLAggsQuery

`BQLAggsQuery` is used for [[Urls Aggregation;analysis-aggregate-urls]] to define aggregations to perform, metrics to compute, and filter to operate.

## Format
```JSON
{
  "aggs": [
    {
      "group_by": ?Array<BQLGroupBy>,
      "metrics": Array<BQLMetric>
    }
  ],
  "filters": ?BQLFilter
}
```

A `BQLAggsQuery` is composed of a list of `BQLAggregate` and an optional `BQLFilter`. An `BQLAggregate` defines some `BQLMetric` to compute. `BQLGroupBy` can be used to group URLs and compute metrics on each group.


### Group-Bys
A group-by is defined by:
  - a `field` on which the group-by is performed.
  - some optional `ranges` that define buckets for the group-by operation.

#### Simple GroupBy
Only [[aggregables fields;analysis-datamodel?filter=agg:]] can be used for group by operations.

**Example**
The following groups URLs by their `http_code`.
```JSON
"http_code"
```

#### Range GroupBy
Only [[numerical fields;analysis-datamodel?filter=agg:numerical]] can be used for range group by operations.

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

### Metrics
Metrics define the operation to compute. Except for `count`, a field on which the metric is applied must be provided. Available metrics are:
- `count`
- `sum`
- `avg`
- `min`
- `max`
Note: The default metric is `count`.

**Examples**
Count of URLs
```JSON
"count"
```
Sum of internal inlinks nofollow
```JSON
{ "sum": "inlinks_internal.nb.follow.total" }
```


### Filters

Please refer to [[BQLFilter;bql-filter]] documentation.


## Examples
Full examples in [[Urls Aggregation documentation;analysis-aggregate-urls#example-aggregation-on-filtered-dataset]].

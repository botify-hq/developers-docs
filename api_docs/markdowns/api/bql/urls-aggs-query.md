# UrlsAggsQuery

```JS
{
  "aggs": [
    {
      "group_by": Array<GroupBy>,
      "metrics": Array<Metric>
    }
  ],
  "filters": UrlFilters
}
```

A `UrlsAggsQuery` is composed a set of `Aggregate`s and an optional `Filters`.

## `aggs: Array<Aggregate>`
An `Aggregate` can define some `metric` to compute on a set of `groupby`s.

### GroupBy
A `groupby` is defined by.
  - a `field` on which the group-by is performed.
  - some optional `ranges` that define buckets for the group-by operation. Ranges are only available for **numerical fields**.

Examples

`'http_code'` allows to group-by each occurence of `http_code`

The following allows to group-by two ranges of `delay_last_byte` (fast and slow URLs)
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
Defines the operation to compute. Available metrics are:
- `count`
- `sum`
- `avg`
- `min`
- `max`

Except for `count`, a field on which the metric is applied must be provided.

Examples: `'count'` or `{ "sum": "inlinks_internal.nb.follow.total" }`

The default metric is `count`.

## `filters: UrlsFilter`

Please refer to [UrlsFilter](#urlsfilter) documentation.

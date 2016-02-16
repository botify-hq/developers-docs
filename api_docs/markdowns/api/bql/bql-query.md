# BQLQuery

`BQLQuery` is used for [[Urls Filtering;usage-query-urls]] to define fields selection, filter to operate and sort to apply on result.

## Format
```JSON
{
  "fields": Array<string>,
  "sort": ?Array<BQLSort>,
  "filters": ?BQLFilter
}
```

### `fields: Array<string>`

The fields to fetch. Default field is `url`. This is equivalent to the `select` clause in SQL. List of fields in [[URLs Datamodel;urls-datamodel]].

**Example:**
```JSON
[ "url", "http_code" ]
```

### `sort: Array<BQLSort>`

Requires the result to be sorted on a certain set of fields. Sort criteria are not necessarily part of the fetched fields.

**Example:**
```JSON
[
  {
    "http_code": {
      "order": "desc"
    }
  }
]
```

### `filters: BQLFilter`

Please refer to [[BQLFilter;bql-filter]] documentation.


## Example
Full example in [[Urls Filtering documentation;usage-query-urls#example]].

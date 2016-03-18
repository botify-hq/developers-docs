# BQLQuery

`BQLQuery` is used for [[Urls Filtering;analysis-search-for-urls]] to define fields selection, filter to operate and sort to apply on result.

## Format
```JSON
{
  "fields": Array<string>,
  "sort": ?Array<BQLSort>,
  "filters": ?BQLFilter
}
```

### Fields

The fields to fetch. Default field is `url`. This is equivalent to the `select` clause in SQL. List of selectable fields in [[URLs Datamodel;analysis-urls-datamodel?filter=select]].

**Example:**
```JSON
[ "url", "http_code" ]
```

### Sort

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

### Filters

Please refer to [[BQLFilter;bql-filter]] documentation.


## Example
Full example in [[Urls Filtering documentation;analysis-search-for-urls#example]].

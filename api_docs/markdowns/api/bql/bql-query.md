# BQLQuery

`BQLQuery` is used for [[Urls listing and filtering;analysis-list-urls]] to define field selection, filter to operate and sort to apply on the result.

## Format
```JSON
{
  "fields": Array<string>,
  "sort": ?Array<BQLSort>,
  "filters": ?BQLFilter
}
```

### Fields

The fields to fetch. Default field is `url`. This is equivalent to the `select` clause in SQL. List of selectable fields in [[Analysis Datamodel;analysis-datamodel?filter=select]].

**Example:**
```JSON
[ "url", "http_code" ]
```

### Sort

Requires the result to be sorted on a certain set of fields. Sort criteria are not necessarily part of the fetched fields.
Order can be either `desc` or `asc`.

**Example:**
```JSON
[
  { "http_code": { "order": "desc" } }
]
```

### Filters

Please refer to [[BQLFilter;bql-filter]] documentation.


## Example
Full example in [[List and Filter URLs documentation;analysis-list-urls#example]].

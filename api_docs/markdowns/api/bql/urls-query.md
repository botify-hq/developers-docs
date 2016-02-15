# UrlsQuery

```JS
{
  "fields": Array<string>, // optional
  "sort": Array<UrlsSort>, // optional
  "filters": UrlsFilter, // optionnal
}
```

#### `fields: Array<string>`

The fields to fetch. Default field is `url`. This is equivalent to the `select` clause in SQL. List of fields is available in [[Datamodel;urls-datamodel]].

Example: `['url, 'http_code']`


#### `sort: Array<UrlsSort>`

Requires the result to be sorted on a certain set of fields. Sort criteria are not necessarily part of the fetched fields.

Example: `[ {"http_code": {"order": "desc"}} ]`


#### `filters: UrlsFilter`

Please refer to [UrlsFilter](#urlsfilter) documentation.

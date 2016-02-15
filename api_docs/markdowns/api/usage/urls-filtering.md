# URLs Filtering

Botify API allows you to filter the dataset of URLs of your analysis and return any available information. **Full list of requestable fields** can be found in [[Urls Datamodel;urls-datamodel]].


## Endpoint

- Operation: [[getUrls;reference#Analysis_getUrls]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls`
- HTTP Verb: POST
- Body : `Array<UrlsQuery>`
- Response: `Array<UrlsResult>`

Please refer to [[UrlsQuery;bql-urls-query]] documentation for information about input.

```SH
curl 'https://api.botify.com/analyses/${username}/${project_slug}/${analysis_slug}/urls' \
     -X POST \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json' \
     --data-binary '${UrlsQuery}'
```

## Example

The following example of [[UrlsQuery;bql-urls-query]] fetches `url` and `metadata.title.nb` fields and filters the dataset on new URLs that respond with a 2xx HTTP code. The result is sorted on descending number of titles.

```JSON
{
  "fields": ["url", "metadata.title.nb"],
  "filters": {
    "and": [
      {
        "field": "http_code",
        "value": [200, 300],
        "predicate": "between"
      },
      {
        "not": {
          "field": "previous",
          "predicate": "exists"
        }
      }
    ]
  },
  "sort": [
    { "metadata.title.nb": { "order": "desc" } }
  ]
}
```

A sample result would be:
```JSON
[
  {
    "url": "www.abc.com/1",
    "metadata": {
      "title": {
        "nb": 15
      }
    }
  },
  {
    "url": "www.abc.com/2",
    "metadata": {
      "title": {
        "nb": 9
      }
    }
  }
]
```

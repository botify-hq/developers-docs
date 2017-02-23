# Get Summary

Botify API allow you to get metadata of an logs project, including the **first and last dates of logs data** available, segments names and search engines' bots list.

## Request

- Operation: [[getLogsSummary;reference#/Logs/getLogsSummary]]
- Path: `logs/{username}/{project_slug}`
- HTTP Verb: GET
- Response: `Logs`

```SH
curl "https://api.botify.com/v1/logs/${username}/${project_slug}" \
     -X GET \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json"
```

## Response

The response has the following format.
Note any other Logs API operation requires a range of dates to work on, `date_start` and `date_end` are the limits you can use, anything outside would result to an error as data isn't available.

```JSON
{
  "date_start": "2016-11-06",
  "date_end": "2016-12-21",
  "segments_namespaces": [
    "pagetype",
    "lang"
  ],
  "search_engines": [
    {
      "name": "Google",
      "slug": "google",
      "bots": [
        {
          "name": "Google Search",
          "slug": "search"
        },
        ...
      ],
    },
    {
      "name": "Bing",
      "slug": "bing",
      "bots": [
        {
          "name": "Bing Search",
          "slug": "search"
        }
      ]
    }
  ]
}
```


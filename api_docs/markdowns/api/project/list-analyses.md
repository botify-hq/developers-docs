# List Project's Analyses

Botify API can return the list of analyses for a given project.

## Endpoint

- Operation: [[getProjectAnalyses;reference#/Project/getProjectAnalyses]]
- Path: `analyses/{username}/{project_slug}`
- HTTP Verb: GET
- Response: `Array<Analysis>`

```SH
curl 'https://api.botify.com/v1/analyses/${username}/${project_slug}' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}'
```

## Example of response
The response contains the list of analyses which belongs to the project. For each analysis, information is given, including their **slug**, **status**, start and finish date, and list of **enabled features**. For more information please refer to [[Analysis summary documentation;analysis-get-summary]].

Analysis slug is the key to get any data related to. Please note that most of API analysis operations are available only for analyses with the status `success`. Analysis's status can be one of `preparing`, `crawling`, `crawling_paused`, `analyzing`, `success`, `failed`.

```JSON
{
  "count": 1,
  "page": 1,
  "size": 1,
  "results": [
    {
      "id": 88765,
      "slug": "20161208",
      "name": "2016 Dec. 8th",
      "status": "success",
      "url": "https://app.botify.com/zallek/botify-developers/20161208/",
      "urls_done": 39,
      "urls_in_queue": 0,
      "date_launched": "2016-12-08T14:45:25.879995Z",
      "date_finished": "2016-12-08T14:52:48.145643Z",
      "date_last_modified": "2016-12-08T14:52:48.145667Z",
      "user": {...},
      "features": {
        "main": {...},
        "links": {...},
        "segments": {...},
        "visits": {...},
        "search_engines": {...},
        "sitemaps": {...},
        "extract": {...},
        "rel": {...},
        "comparison": {...}
      },
      "failures": [...],
      "config": {
        "scope": {...},
        "crawler": {...},
        "google_analytics": {...},
        "google_analytics_premium": {...},
        "sitemaps": {...},
      },
      "red_button_domain": null
    }
  ]
}
```

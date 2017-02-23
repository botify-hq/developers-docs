# Get Summary

Botify API allow you to get metadata of an analysis, including analysis **slug**, status, start and finish date, owner, crawl configuration and list of enabled **features** with their configuration.

## Request

- Operation: [[getAnalysisSummary;reference#/Analysis/getAnalysisSummary]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}`
- HTTP Verb: GET
- Response: `Analysis`

```SH
curl "https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}" \
     -X GET \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json"
```

## Response

The response will have the following format.

```JSON
{
  "id": 88765,
  "slug": "20161208",
  "name": "2016 Dec. 8th",
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
```

- `urls_done` is the number of **crawled URLs**.
- `urls_in_queue` is the number of URLs which would have been crawled if the analysis wouldn't have been interrupted. An analysis can be interrupted for many raisons, project owner can manually stop the crawl in the application or the limit of crawlable URLs may have been reached (cf `config.crawler.max_nb_pages`) or the owner of the website may have asked to stop crawling his website. Note that in Botify Analytics, 'Known URLs' is the sum of crawled URLs and URLs in queue.
- `user` is the **owner** of the analysis's project.
- `features` is the **list of enabled features** and their configuration. For more information about features, please refer to the [[Features;analysis-features]] documentation.
- `failures` is the list of failed features (by name).
- `config` contains project configuration as set up in Project Advanced Settings including **scope** (start URL(s), allowed domains, robot.txt, max number of URLs) and **crawler configuration** (speed, authentication, headers) and **integrations** (Google Analytics, Sitemaps, etc).

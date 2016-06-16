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
The response contains the list of analyses which belongs to the project. For each analysis, information is given, including analysis slug, launch and finished date, related user, list of enabled **features** and their options, crawl configuration.

Analysis statuses: `preparing`, `crawling`, `crawling_paused`, `analyzing`, `success`, `failed`

```JSON
{
  "count": 1,
  "page": 1,
  "size": 1,
  "results": [
    {
      "id": 35180,
      "slug": "20160115",
      "name": "2016 Jan. 15th",
      "status": "success",
      "url": "https://app.botify.com/adam_warlock/demo-project/20160115/",
      "urls_done": 500000,
      "urls_in_queue": 4915522,
      "date_created": "2016-01-15T16:58:56.431595Z",
      "date_launched": "2016-01-15T16:58:57.948913Z",
      "date_finished": "2016-01-17T02:25:24.559574Z",
      "date_last_modified": "2016-01-17T02:25:24.559585Z",
      "user": {
        "login": "annabelle",
        "email": "...",
        "is_organization": false,
        "url": "https://app.botify.com/annabelle/",
        "date_joined": "2014-04-09T05:51:27Z",
        "first_name": "",
        "last_name": "",
        "company_name": null
      },
      "features": {
        "duplicate_query_kvs": true,
        "main_image": null,
        "links": {
          "top_domains": true,
          "top_anchors": true,
          "page_rank": true,
          "prev_next": true,
          "links_to_non_canonical": true,
          "chains": true
        },
        "segments": {
          "rules_raw": "[segment:country]\n\n@ja\npath /ja/*\n\n@de\npath /de/*\n\n@fr\npath /fr/*\n\n@it\npath /it/*\n\n@zh\npath /zh/*\n\n@ru\npath /ru/*\n\n@tr\npath /tr/*\n\n@pt\npath /pt/*\n\n@sv\npath /sv/*\n\n@es\npath /es/*\n\n@pl\npath /pl/*\n\n@en\n\n[segment:pagetype]\n\n@home\nor (\npath /\npath rx:^/../$\n)\n\n@navigation/top\nor (\npath */dashboard\npath */events\npath */music\npath */features\npath */whatsnew\n)\n\n@navigation/tag\npath */tag/*\n\n@UGC/user/date_range\npath */user/*\nor (\nquery date_preset*\nquery *from*\n)\nflag warning\n\n@UGC/forum\npath */forum/*\n\n@UGC/post\npath */post/*\n\n\n@login\npath */login*\n\n@event\nor (\npath */event/*\npath */festival/*\n)\n\n@artist/tracks\npath rx:/music/[^/]+/\\+tracks$\n\n@artist/albums\npath rx:/music/[^/]+/\\+albums$\n\n@artist/other-tab\npath rx:/music/[^/]+/\\+\n\n@artist\npath rx:/music/[^/]+$\n\n@album\npath rx:/music/[^/]+/[^/]+$\n\n@album/tab\npath rx:/music/[^/]+/[^/]+/\\+\n\n@track\npath rx:/music/[^/]+/[^/]+/[^/]+$\n\n@track/tab\npath rx:/music/[^/]+/[^/]+/[^/]+/\\+",
          "names": [
            "country",
            "pagetype"
          ]
        },
        "sitemaps": {
          "urls": [
            "http://www.last.fm/sitemap-index.xml"
          ]
        },
        "rel": null,
        "main": {
          "lang": true,
          "segments": true
        },
        "extract": [
          {
            "regex": "<abbr class=\"intabbr\" title=\"(\\d+)[\\s,\\.]?(\\d+)?[\\s,\\.]?(\\d+)?\"",
            "ignore_case": true,
            "name": "ScrobbleCount",
            "aggregation": "first",
            "cast": "i",
            "match": "$1$2$3"
          },
          {
            "regex": "</abbr>.</td>.+?<abbr class=\"intabbr\" title=\"(\\d+)[\\s,\\.]?(\\d+)?[\\s,\\.]?(\\d+)?\"",
            "ignore_case": true,
            "name": "Listeners",
            "aggregation": "first",
            "cast": "i",
            "match": "$1$2$3"
          },
          {
            "regex": "namespace--([a-z\\_]+)",
            "ignore_case": true,
            "name": "Namespace",
            "aggregation": "first",
            "cast": "s",
            "match": "$1"
          },
          {
            "regex": "class=\"tag\".+?>([^<]+)</a>",
            "ignore_case": true,
            "name": "Tags",
            "aggregation": "list",
            "cast": "s",
            "match": "$1"
          }
        ],
        "semantic_metadata": {
          "length": true
        }
      },
      "config": {
        "start_urls": [
          "http://www.last.fm"
        ],
        "allowed_domains": [
          {
            "domain": "www.last.fm",
            "protocol": "both",
            "allow_subdomains": false
          }
        ],
        "virtual_robots_txt": null,
        "max_depth": null,
        "blacklisted_domains": null,
        "max_urls_per_sec": 5,
        "export_limit": 100000,
        "max_urls": 500000
      }
    }
  ]
}
```

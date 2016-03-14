# Google Analytics

Google Analytics is used to compute number of visits by URL, therefore whenever an URL is active or not. This data is mainly used for the **Visits** tab of Botify Analytics Report.
It also introduce Google Analytics orphan URLs which are URLs **not in your website structure** (or in the scope of your crawl) but which received visits according to Google Analytics.


## Get feature metadata

Google Analytics feature metadata includes:
- imported data timeframe.
- data sample info.
- orphans URLs counts.

### Request

- Operation: [[getAnalysisSummary;reference#/Analysis/getAnalysisSummary]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}`
- HTTP Verb: GET
- Response: `Analysis`

```SH
curl 'https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json'
```

### Response

An extract of the response could be the following.
**Note:** If feature is not enabled, `features.ganalytics` resolves to `null`.

In the response, you can find the imported google analytics timeframe with `date_start` and `date_end` properties.
Plus, you can get orphan URLs count with the `unknown` property. For instance, the number of orphan URLs for Google can be found at `features.ganalytics.unknown.organic.google.nb_urls`.

```JSON
{
  "features": {
    "ganalytics": {
      "ganalytics_site_id": 111513424,
      "date_start": "2016-02-08",
      "date_end": "2016-03-09",
      "sampled": true,
      "sample_size": 30227156,
      "sample_percent": "72.89999999999999",
      "unknown": {
        "organic": {
          "all": {
            "nb_urls": 1390,
            "nb_visits": 438020
          },
          "google": {
            "nb_urls": 1334,
            "nb_visits": 437022
          },
          "bing": {
            "nb_urls": 36,
            "nb_visits": 221
          },
          "baidu": {
            "nb_urls": 1,
            "nb_visits": 2
          },
          ...
        },
        "social": {
          "all": {
            "nb_urls": 1241,
            "nb_visits": 54604
          },
          "facebook": {
            "nb_urls": 300,
            "nb_visits": 38437
          },
          "twitter": {
            "nb_urls": 48,
            "nb_visits": 525
          },
          ...
        }
      }
    }
  }
}
```



### Get sample of Orphan URLs

- Operation: [[getGanalyticsOrphanURLs;reference#/Analysis/getGanalyticsOrphanURLs]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/features/ganalytics/orphan_urls/{medium}/{source}`
- HTTP Verb: GET
- Response: `Pagination<OrphanURL>`

```SH
curl 'https://api.botify.com/v1/analyses/{username}/{project_slug}/{analysis_slug}/features/ganalytics/orphan_urls/{medium}/{source}' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json'
```

The response could be the following. You can at most get a sample of 1000 orphan URLs. The second number for each URL is the total number of visits.

```JSON
{
  "count": 1000,
  "page": 1,
  "size": 100,
  "results": [
    [
      "http://example.domain.com/2016/02/103982/fuller-house-season-one",
      "55986"
    ],
    [
      "http://example2.domain.com",
      "23888"
    ],
    [
      "http://example2.domain.com/2016/02/104206/oscars-2016-stacey-dash",
      "22319"
    ],
    [
      "http://example.domain.com/2016/03/104051/republican-primary-winners-election-results-2016",
      "13636"
    ]
  ]
}
```

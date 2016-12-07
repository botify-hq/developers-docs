# Visits

Google Analytics is used to compute the number of visits by URL, therefore whenever an URL is active or not. This data is mainly used for the **Visits** tab of the Botify Analytics Report.
Visits Orphan URLs are URLs **not in your website structure** (or in the scope of your crawl) but which received visits according to Google Analytics.


## URLs datamodel fields

[[Visits feature's fields;analysis-urls-datamodel?feature=visits]].


## Examples of Aggregation

The following examples use [[URLs aggregation;analysis-aggregate-urls]] to metrics regarding main data.
**Note**: All the following results are only computed on analyzed URLs (URLs crawled by Botify)

### Number of active URLs

```JSON
{
  "filters": {
    "field": "visits.organic.all.nb",
    "predicate": "gt",
    "value": 0
  }
}
```

### Average follow inlinks for active or not active URLs

```JSON
{
  "aggs": [
    {
      "group_by": [
         "visits.organic.all.active"
      ],
      "metrics": [
        {
          "avg": "inlinks_internal.nb.follow.unique"
        }
      ]
    }
  ]
}
```

### Number of active/not active URLs by depth

```JSON
{
  "aggs": [
    {
      "group_by": [
        "depth",
        "visits.organic.all.active"
      ]
    }
  ]
}
```

## Get metadata

Visits feature metadata includes:
- imported **data timeframe**.
- data sample info.
- **orphans URLs counts**.

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

In the response, you can find the imported visits timeframe with `date_start` and `date_end` properties.
Plus, you can get the number of orphan URLs with the `unknown` property. For instance, the number of orphan URLs for Google can be found in `features.visits.unknown.organic.google.nb_urls`.
**Note:** If feature is not enabled, `features.visits` resolves to `null`.
**Note:** For analyses prior to August 2016, the feature is named ganalytics. Related information can be found in `features.ganalytics`.

An extract of the response could be the following.

```JSON
{
  "features": {
    "visits": {
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



### Get a sample of the Orphan URLs

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

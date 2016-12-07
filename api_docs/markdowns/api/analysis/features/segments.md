# Segments

This feature allows you to deeply segment your website pages into several sections such as page type, in which we could define article pages, navigation pages, user pages, etc.
The segments can be configured in your project settings.


## URLs datamodel fields

[[Segment feature's fields;analysis-urls-datamodel?feature=segments]].
The segments feature provides 4 main fields:

- segments.segment_X.value
- segments.segment_X.depth_1
- segments.segment_X.depth_2
- segments.segment_X.depth_3

**Note:** `X` refers to the segment number, `segment_1` would be `pagetype` in the previous example whereas `segments_2` would be `lang`.

`depth_X` fields are meant to be used to aggregate on the first, second and third depth of their value.

### Example

Remember that segments can be defined in deep, for instance the `pagetype` could take the following values: books/arts, books/food, books/novel, books/law, home, ads.

So for an URL with a pagetype `books/food` the field would have the following values:

- **segments.segment_X.value:** `books/food` (full value)
- **segments.segment_1.depth_1:** `books`
- **segments.segment_1.depth_2:** `food`
- **segments.segment_1.depth_3:** `null` (no depth 3)


## Examples of Aggregation

The following examples use [[URLs aggregation;analysis-aggregate-urls]] to metrics regarding segments.
In the following example, we assume that the first segment is pagetype.

### Number of URLs by pagetype

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "segments.segment_1.value"
        ]
      }
    ]
  }
]
```

### Total number of visits by main pagetype

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "segments.segment_1.depth_1",
        ],
        "metrics": [
          {
            "sum": "visits.organic.all.nb"
          }
        ]
      }
    ]
  }
]
```

### Number of crawled/not crawled URLs by Google by main pagetype

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          "segments.segment_1.depth_1",
          {
            "range": {
              "field": "search_engines.google.crawls.count",
              "ranges": [
                { "from": 1 }, // Crawled
                { "from": 0, "to": 1 } // Not Crawled
              ]
            }
          }
        ]
      }
    ]
  }
]
```


## Get metadata

Segments feature metadata includes:
- **list of configured segments** (limited to the first two because Botify Analytics can only handle two segments at most).
- segment config

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
**Note:** If feature is not enabled, `features.segments` resolves to `null`.

You can find the list of the segment names at `features.segments.names`.

```JSON
{
  "features": {
    "segments": {
      "rules_raw": "[dim:pagetype]\n\n@articles\n\n[dim:lang]\n\n@us",
      "names": ["pagetype", "lang"]
    },
    ...
  },
  ...
}
```

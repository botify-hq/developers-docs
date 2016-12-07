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

**Note:** `X` is the segment number as defined in your project configuration (refers to [Get Metadata](#get-metadata))
**Note:** `depth_X` fields are meant to be used to aggregate on the first, second and third depth of their value.

### Example

If `pagetype` is your first segment, an URL with a pagetype `books/food` would have the following field values: 

- **segments.segment_1.value:** `books/food` (full value)
- **segments.segment_1.depth_1:** `books`
- **segments.segment_1.depth_2:** `food`
- **segments.segment_1.depth_3:** `null` (no depth 3)


## Examples of Aggregation

The following examples use [[URLs aggregation;analysis-aggregate-urls]] to compute metrics on segments.
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
- **list of configured segments** (limited to two).
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

You can find the list of the segment names at `features.segments.names` and the config in `features.segments.rules_raw`.
**Note:** If feature is not enabled, `features.segments` resolves to `null`.

An extract of the response could be the following.

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

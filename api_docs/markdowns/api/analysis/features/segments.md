# Segments

This feature allows you to deeply segment your website pages into several sections (ie: in the segment pagetype, we could have article pages, navigation pages, user pages etc).
The segments can be configured in your project settings.


## Get metadata

Google Analytics feature metadata includes:
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

You can find the list of set up segments name at `features.segments.names`.

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


## Segments fields

Segment features provides 4* main fields in the [[URL datamodel;analysis-urls-datamodel?group=segments]]:

- segments.segment_X.value
- segments.segment_X.depth_1
- segments.segment_X.depth_2
- segments.segment_X.depth_3

**Note:** `X` refers to the segment number, `segment_1` would be `pagetype` in the previous example whereas `segments_2` would be `lang`.

`depth_X` fields are meant to be used to aggregate on first/second/third depth of segments values.

### Example

Remember that segments can be defined in deep, for instance the `pagetype` could take the following values: books/arts, books/food, books/novel, books/law, home, ads.

So for an URL with a pagetype `books/food` the field would have the following values:

- **segments.segment_X.value:** `books/food` (full value)
- **segments.segment_1.depth_1:** `books`
- **segments.segment_1.depth_2:** `food`
- **segments.segment_1.depth_3:** `null` (no depth 3)


## Examples of Aggregation

The following examples uses [[URLs aggregation;analysis-aggregate-urls]] to metrics regarding segments.
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

### Total number of visits by pagetype (only on first depth)

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

### Number of compliant URLs by pagetype by depth

```JSON
[
  {
    "aggs": [
      {
        "group_by": [
          {
            "range": {
              "field": "depth",
              "ranges": [
                { "from": 0, "to": 1 },
                { "from": 1, "to": 2 },
                { "from": 2, "to": 3 },
                { "from": 3, "to": 4 },
                { "from": 4, "to": 5 },
                { "from": 5 }
              ]
            }
          },
          "segments.segment_1.depth_1"
        ]
      }
    ],
    "filters": {
      "field": "compliant.is_compliant",
      "predicate": "eq",
      "value": true
    }
  }
]
```

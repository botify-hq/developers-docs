# URLs Data Model Introspection

## Endpoint

- Operation: [[getUrlsDatamodel;reference#Analysis_getUrlsDatamodel]]
- Path: `analyses/${username}/${project_slug}/${analysis_slug}/urls/datamodel`
- HTTP Verb: POST
- Response: `DataModel`

Please refer to [[DataModel;datamodel]] documentation for information about `DataModel` object.

```SH
curl 'https://api.botify.com/analyses/${username}/${project_slug}/${analysis_slug}/urls/datamodel' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}' \
```

**Result may differ from an analysis to another** because all features are not enabled on all analyses.


## List of fields

@TODO: Add script to fetch data model


## Area

In almost every **analysis** endpoint dealing with URL Data model, an **area parameter** is present (its default value is `current`). It refers to the subset of URL to compute on:

![screenshot from 2016-01-08 11 49 14](https://cloud.githubusercontent.com/assets/1886834/12196436/df1d2632-b5fe-11e5-9f7a-04197d49a49f.png)
*URLs distribution chart available in movements tab of analysis report.*

- **current**: URLs that were crawled in the current analysis (blue and purple part)
- **new**: URLs crawled in the current analysis but not in the previous analysis (blue part)
- **disappeared**: URLs crawled in the previous analysis but not in the current analysis (red part)


## Data Types

**data_type** describes the type of the data stored. It allows to know which type of input to use or which [predicates](#predicates) are available.

Data types are `string`, `integer`, `long`, `float`, `double`, `boolean`, `struct`, `date`, `datetime`, `tree`.


## Fields Types

**field_type** describes the concept represented by the field. Sample concepts are `UrlStatus` or `TimeMilliseconds`. If the field doesn't represent any specific concept, `field_type` is the same as `data_type`. It allows to know how to render the field data.


### `url`
Standalone URL
```JS
string
```

### `image_url`
Url of an image
```JS
string
```

### `url_status`
Url with its crawled state. If not crawled, no information can be obtained using the URLs endpoint.
```JS
{
  "url": string,
  "crawled": boolean
}
```

### `url_link_status`
Url with its crawled state and its follow/nofollow status
```JS
{
  "status": string,
  "url": {
    "url": string,
    "crawled": boolean
  },
}
```

### `url_http_code`
Url with its HTTP status code
```JS
[string, string] // [URL, HTTP Status Code]
```

### `string_nb_map`
List of strings with their number of occurrences.
```JS
[
  {
    "text": string,
    "nb": integer,
  }
]
```

### `time_millisec`
Number of milliseconds (duration)
```JS
integer
```

### `hreflang_valid_values`

```JS
{
    "url": {
        "url": Url,
        "crawled": boolean
    },
    "warning": Array<string> // warning ids
    "value": string,
},
```

Warning Id | Message
--- | ---
WARNING_DEST_BLOCKED_ROBOTS_TXT | URL referenced by hreflang tag is blocked by (virtual) robots.txt.
WARNING_DEST_BLOCKED_CONFIG | URL referenced by hreflang tag was not crawled due to project settings.
WARNING_DEST_NOT_CRAWLED | URL referenced by hreflang tag was not crawled.

### `hreflang_error_values`

```JS
{
    "url": {
        "url": Url,
        "crawled": boolean
    },
    "errors": Array<string> // errors ids
    "value": string,
},
```

Error Id | Message
--- | ---
ERROR_LANG_NOT_SET | Language is not set in the HTML tag.
ERROR_NOT_COMPLIANT | URL is not compliant
ERROR_LANG_NOT_EQUAL | Language in hreflang tag does not match the language of referenced URL.
ERROR_LANG_NOT_RECOGNIZED | Language in hreflang tag does not exist or is not supported.
ERROR_REGION_NOT_RECOGNIZED | Region in hreflang tag does not exist or is not supported.
ERROR_REGION_NOT_EQUAL | Region in hreflang tag does not match the region of referenced URL.
ERROR_DEST_NOT_COMPLIANT | URL referenced by hreflang tag is not compliant.

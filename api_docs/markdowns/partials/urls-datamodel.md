## Area

In almost every **analysis** endpoint dealing with URL Data model, an **area parameter** is present (its default value is `current`). It refers to the subset of URL to compute on:

![screenshot from 2016-01-08 11 49 14](https://cloud.githubusercontent.com/assets/1886834/12196436/df1d2632-b5fe-11e5-9f7a-04197d49a49f.png)
*URLs distribution chart available in movements tab of analysis report.*

- **current**: URLs that were crawled in the current analysis (blue and purple part)
- **new**: URLs crawled in the current analysis but not in the previous analysis (blue part)
- **disappeared**: URLs crawled in the previous analysis but not in the current analysis (red part)

**name** identifies fields.

**data type** describe the type of the data stored. It allows to know which type of input to use or which [predicates](#predicates) are available.

Data Type | Value Type
--- | ---
`integer` | Numerical
`long` | Numerical
`float` | Numerical
`double` | Numerical
`date` | Numerical
`datetime` | Numerical
`string` | Categorical
`boolean` | Categorical
`tree` | Categorical
`struct` | N/A

**field type** describes the concept represented by the field like `url_status` or `time_sec`. If the field doesn't represent any specific concept, `field_type` equals `data_type`. List of field types may depend on the data model type. It allows to know how to render the field data.

**multiple** is set to `true` whenever the value is a **list**. For instance, `query_string_keys` contains a list of query string keys. Example: `['page', 'length']` on a paginated url.

**is_able** is set to `true` if the field can be used in [UrlsQuery](#urlsquery) `sort`.

**rights** is the list of operations the field can be used for. The rights may include the following:
- `filters`: can be used in any [UrlsFilter](#urlsfilter)
- `filters_exist`: can **only** be used with a predicate [exists](#exists-predicate) in a [UrlsFilter](#urlsfilter)
- `select`: can be used in [UrlsQuery](#urlsquery) `fields`
- `top_values`: can be used by [[getUrlsFieldTopValues;reference#!/Analysis/getUrlsFieldTopValues]]
- `suggest`: can be used by [[getUrlsFieldSuggest;reference#!/Analysis/getUrlsFieldSuggest]]
- agg:numerical
- agg:categorical
- **sort**: 

## Type

**type** describes the type of the data stored. It allows to know which type of input to use or which [predicates](#predicates) are available.

Data types are `string`, `integer`, `long`, `float`, `double`, `boolean`, `struct`, `date`, `datetime`, `tree`.


## SubType

**subtype** describes the concept represented by the field. Sample concepts are `UrlStatus` or `TimeMilliseconds`. If the field doesn't represent any specific concept, `field_type` is the same as `data_type`. It allows to know how to render the field data.


### `url`
Standalone URL
```JSON
string
```

### `image_url`
Url of an image
```JSON
string
```

### `url_status`
Url with its crawled state. If not crawled, no information can be obtained using the URLs endpoint.
```JSON
{
  "url": string,
  "crawled": boolean
}
```

### `url_link_status`
Url with its crawled state and its follow/nofollow status
```JSON
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
```JSON
[string, string] // [URL, HTTP Status Code]
```

### `string_nb_map`
List of strings with their number of occurrences.
```JSON
[
  {
    "text": string,
    "nb": integer,
  }
]
```

### `time_millisec`
Number of milliseconds (duration)
```JSON
integer
```

### `hreflang_valid_values`

```JSON
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

```JSON
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

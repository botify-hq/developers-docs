## Permissions
Describes the list of operations the field can be used for. The rights may include the following:
- **select:** can be used in [[BQLQuery;bql-query]] fields.
- **filters:** can be used in [[BQLFilter;bql-filter]].
- **filters_exist:** can **only** be used with a [[exist predicate;bql-filter#exists-predicate]] in a BQLFilter.
- **sort:** can be used in BQLFilter [[sort;bql-query]].
- **agg:categorical:** can be used in BQLAggsQuery [[groupby;bql-aggs-query#simple-groupby]].
- **agg:numerical:** can be used in BQLAggsQuery [[range groupby;bql-aggs-query#range-groupby]].


## Type
Describes the basic type of the data as it is stored. It allows which [[predicates;bql-filter#predicates]] are available and which type of input to use.


## SubType

Describes the concept represented by the field, such as `url_status` or `time_millisec`. If the field doesn't represent any specific concept, `subtype` is the same as `type`. List of subtypes may depend on the datamodel. It allows to know how to render the field data.


### url
Standalone URL
```JSON
string
```

### image_url
URL of an image
```JSON
string
```

### url_status
URL with its crawled state. If not crawled, no information can be obtained using the URLs endpoint.
```JSON
{
  "url": string,
  "crawled": boolean
}
```

### url_link_status
URL with its crawled state and its follow/nofollow status
```JSON
{
  "status": string,
  "url": {
    "url": string,
    "crawled": boolean
  },
}
```

### url_http_code
URL with its HTTP status code
```JSON
[string, string] // [URL, HTTP Status Code]
```

### string_nb_map
List of strings with their number of occurrences.
```JSON
[
  {
    "text": string,
    "nb": integer,
  }
]
```

### time_millisec
Number of milliseconds (duration)
```JSON
integer
```

### hreflang_valid_values

```JSON
{
    "url": {
        "url": string,
        "crawled": boolean
    },
    "warning": Array<string>,
    "value": string,
},
```

Warning | Description
--- | ---
WARNING_DEST_BLOCKED_ROBOTS_TXT | URL referenced by hreflang tag is blocked by (virtual) robots.txt.
WARNING_DEST_BLOCKED_CONFIG | URL referenced by hreflang tag was not crawled due to project settings.
WARNING_DEST_NOT_CRAWLED | URL referenced by hreflang tag was not crawled.

### hreflang_error_values

```JSON
{
    "url": {
        "url": string,
        "crawled": boolean
    },
    "errors": Array<string>,
    "value": string,
},
```

Error | Description
--- | ---
ERROR_LANG_NOT_SET | Language is not set in the HTML tag.
ERROR_NOT_COMPLIANT | URL is not compliant
ERROR_LANG_NOT_EQUAL | Language in hreflang tag does not match the language of referenced URL.
ERROR_LANG_NOT_RECOGNIZED | Language in hreflang tag does not exist or is not supported.
ERROR_REGION_NOT_RECOGNIZED | Region in hreflang tag does not exist or is not supported.
ERROR_REGION_NOT_EQUAL | Region in hreflang tag does not match the region of referenced URL.
ERROR_DEST_NOT_COMPLIANT | URL referenced by hreflang tag is not compliant.


## Multiple
Some fields can contain a list of values, they are called **multiple** fields. For instance, `query_string_keys` could be equal to `['page', 'length']` on a URL with pagination.


## Area
In almost every **analysis** operation dealing with URL Data model, an **area parameter** is present (its default value is `current`). It refers to the subset of URL to compute on:

![URLs distribution between areas](https://cloud.githubusercontent.com/assets/1886834/12196436/df1d2632-b5fe-11e5-9f7a-04197d49a49f.png)
*URLs distribution chart available in movements tab of the analysis report.*

- **current**: URLs that were crawled in the current analysis (blue and purple part)
- **new**: URLs crawled in the current analysis but not in the previous analysis (blue part)
- **disappeared**: URLs crawled in the previous analysis but not in the current analysis (red part)

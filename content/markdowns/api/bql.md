# BQL

Botify Query DSL (BQL) simplifies the interaction between API users and Botify backend systems by providing an intermediate abstraction. It also facilitates the evolution of our data system since it helps decouple the API and the backends.

BQL provides following search/aggregation abilities on a per-URL basis on the analysis dataset:
  - Retrieve data fields
  - Filtering URL documents based on data fields
  - Sorting on retrieved results
  - Aggregation and nested-aggregation
  - Data models introspection


## Usage

- [URLs Data Fetching](./urls-data-fetching.md)
- [URLs Data Aggregation](./urls-data-aggregation.md)
- [URLs Data Model Introspection](./urls-datamodel-introspection.md)


## Reference

### UrlsQuery

```JS
{
  "fields": Array<string>, // optional
  "sort": Array<UrlsSort>, // optional
  "filters": UrlsFilter, // optionnal
}
```

#### `fields: Array<string>`

The fields to fetch. Default field is `url`. This is equivalent to the `select` clause in SQL. List of fields is available in [datamodel](#datamodel).

Example: `['url, 'http_code']`


#### `sort: Array<UrlsSort>`

Requires the result to be sorted on a certain set of fields. Sort criteria are not necessarily part of the fetched fields.

Example: `[ {"http_code": {"order": "desc"}} ]`


#### `filters: UrlsFilter`

Please refer to [UrlsFilter](#urlsfilter) documentation.


### UrlsAggsQuery

```JS
{
  "aggs": [
    {
      "group_by": Array<GroupBy>,
      "metrics": Array<Metric>
    }
  ],
  "filters": UrlFilters
}
```

A `UrlsAggsQuery` is composed a set of `Aggregate`s and an optional `Filters`.

#### `aggs: Array<Aggregate>`
An `Aggregate` can define some `metric` to compute on a set of `groupby`s.

##### GroupBy
A `groupby` is defined by.
  - a `field` on which the group-by is performed.
  - some optional `ranges` that define buckets for the group-by operation. Ranges are only available for **numerical fields**.

Examples

`'http_code'` allows to group-by each occurence of `http_code`

The following allows to group-by two ranges of `delay_last_byte` (fast and slow URLs)
```JSON
{
  "range": {
    "field": "delay_last_byte",
    "ranges": [
      {
        "from": 0,
        "to": 1000
      },
      {
        "from": 1000
      }
    ]
  }
}
```

##### Metric
Defines the operation to compute. Available metrics are:
- `count`
- `sum`
- `avg`
- `min`
- `max`

Except for `count`, a field on which the metric is applied must be provided.

Examples: `'count'` or `{ "sum": "inlinks_internal.nb.follow.total" }`

The default metric is `count`.

#### `filters: UrlsFilter`

Please refer to [UrlsFilter](#urlsfilter) documentation.


### UrlsFilter

`UrlsFilter` allows to define filtering condition on data fields (FieldFilter) that can be composed using boolean conditions (and, or, not)

#### FieldFilter
A field filter allows to describe a predicate to apply on a given field
```JS
{
  "predicate": string,
  "field": string,
  "value": any,
}
```

#### Predicates
According to the field type, several predicates can be applied.
*Note: List of fields is available in data model.*

##### Numerical Predicates
Numerical fields have continuous values. Numerical fields include `integer`, `long`, `float`, `double`, `date` and `datetime` fields.

###### eq: Equals
Example: `{ field: 'http_code', predicate: 'eq', value: 200 }`

###### gt: Greather than
Example: `{ field: 'http_code', predicate: 'gt', value: 200 }`

###### gte: Greather than or equal
Example: `{ field: 'http_code', predicate: 'gte', value: 200 }`

###### lt: Lower than
Example: `{ field: 'http_code', predicate: 'lt', value: 200 }`

###### lte: Lower than or equal
Example: `{ field: 'http_code', predicate: 'lte', value: 200 }`

###### between: Between
Example: `{ field: 'http_code', predicate: 'between', value: [200, 300] }`
**Note**: Lower bondary is inclusive whereas **upper bondary is exclusive**, ie the above example means `200 <= http_code < 300`.


##### Categorical Predicates
Categorical fields have discrete values. Categorical fields include `string`, `boolean` and `tree` fields.

###### eq: Equals
Example: `{ field: 'url', predicate: 'eq', value: 'https://botify.com' }`

###### contains: Contains
Example: `{ field: 'url', predicate: 'contains', value: 'botify' }`

###### starts: Starts with
Example: `{ field: 'url', predicate: 'start', value: 'https' }`

###### ends: Ends with
Example: `{ field: 'url', predicate: 'ends', value: 'hifi' }`

###### re: Match Regex
Example: `{ field: 'url', predicate: 're', value: 'https.*hifi' }`


##### Tree Predicates
Tree fields can use both categorical predicates and some extra predicates making them easier to use. Tree fields are stored as flat strings like `for/bar`. Tree predicates make it easy to filter on children.

###### with_children
Returns given value and all its children.
Example: `{ field: 'segments.segment_1.value', predicate: 'with_children', value: 'foo' }` could return `foo`, `foo/bar`, `foo/baz`.

###### without_children
Example: `{ field: 'segments.segment_1.value', predicate: 'without_children', value: 'foo' }` could return `foo`.

###### only_children
Example: `{ field: 'segments.segment_1.value', predicate: 'only_children', value: 'foo' }` could return `foo/bar`, `foo/baz`.


##### Exists Predicate
The `exists` predicate takes no value and tests if the field exists in the document. Some fields don't exist because the related feature wasn't enabled or failed during analysis. For instance, previous fields do not exist if the comparison feature is not enabled.

Example: `{ field: 'previous', predicate: 'exists' }`


##### Multiple Prefix Predicates
Some fields like `query_string_keys` are 'multiple' fields, meaning they have a list of values. For instance, `query_string_keys` could be equal to `['page', 'length']` on a URL with pagination.

For this purpose, these fields predicates must be prefixed by `any.`

Example: `any.eq`, `any.contains` meaning any equal to, any contains.


#### FieldFilter composition
FieldFilter can be composed with a boolean condition:

###### and
`{ "and: [FILTER_1, FILTER_2, ...] }`

###### or
`{ "or: [FILTER_1, FILTER_2, ...] }`

###### not
`{ "not: FILTER }`


#### Example
The following `UrlsFilter` filters the analysis URLs dataset on new URLs which are compliant and have no title.
```JSON
{
  "and": [
    {
      "field": "strategic.is_strategic",
      "value": true
    },
    {
      "field": "metadata.title.nb",
      "predicate": "eq",
      "value": 0
    },
    {
      "not": {
        "field": "previous",
        "predicate": "exists"
      }
    }
  ]
}
```

### DataModel

```JS
{
  "fields": [
    {
      "value": string,
      "name": string,
      "data_type": string,
      "field_type": string,
      "multiple": boolean,
      "group": string,
      "rights": Array<string>,
      "is_sortable": boolean,
    }
  ],
  "groups": [
    {
      "id": string,
      "name": string
    }
  ]
}
```

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

**is_sortable** is set to `true` if the field can be used in [UrlsQuery](#urlsquery) `sort`.

**rights** is the list of operations the field can be used for. The rights may include the following:
- `filters`: can be used in any [UrlsFilter](#urlsfilter)
- `filters_exist`: can **only** be used with a predicate [exists](#exists-predicate) in a [UrlsFilter](#urlsfilter)`
- `select`: can be used in [UrlsQuery](#urlsquery) `fields`
- `top_values`: can be used by [getUrlsFieldTopValues](./reference#Analysis_getUrlsFieldTopValues)
- `suggest`: can be used by [getUrlsFieldSuggest](./reference#Analysis_getUrlsFieldSuggest)

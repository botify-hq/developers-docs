# UrlsFilter

`UrlsFilter` allows to define filtering condition on data fields (FieldFilter) that can be composed using boolean conditions (and, or, not)

## FieldFilter
A field filter allows to describe a predicate to apply on a given field
```JS
{
  "predicate": string,
  "field": string,
  "value": any,
}
```

## Predicates
According to the field type, several predicates can be applied.
*Note: List of fields is available in data model.*

### Numerical Predicates
Numerical fields have continuous values. Numerical fields include `integer`, `long`, `float`, `double`, `date` and `datetime` fields.

#### eq: Equals
Example: `{ field: 'http_code', predicate: 'eq', value: 200 }`

#### gt: Greather than
Example: `{ field: 'http_code', predicate: 'gt', value: 200 }`

#### gte: Greather than or equal
Example: `{ field: 'http_code', predicate: 'gte', value: 200 }`

#### lt: Lower than
Example: `{ field: 'http_code', predicate: 'lt', value: 200 }`

#### lte: Lower than or equal
Example: `{ field: 'http_code', predicate: 'lte', value: 200 }`

#### between: Between
Example: `{ field: 'http_code', predicate: 'between', value: [200, 300] }`
**Note**: Lower bondary is inclusive whereas **upper bondary is exclusive**, ie the above example means `200 <= http_code < 300`.


### Categorical Predicates
Categorical fields have discrete values. Categorical fields include `string`, `boolean` and `tree` fields.

#### eq: Equals
Example: `{ field: 'url', predicate: 'eq', value: 'https://botify.com' }`

#### contains: Contains
Example: `{ field: 'url', predicate: 'contains', value: 'botify' }`

#### starts: Starts with
Example: `{ field: 'url', predicate: 'start', value: 'https' }`

#### ends: Ends with
Example: `{ field: 'url', predicate: 'ends', value: 'hifi' }`

#### re: Match Regex
Example: `{ field: 'url', predicate: 're', value: 'https.*hifi' }`


### Tree Predicates
Tree fields can use both categorical predicates and some extra predicates making them easier to use. Tree fields are stored as flat strings like `for/bar`. Tree predicates make it easy to filter on children.

#### with_children
Returns given value and all its children.
Example: `{ field: 'segments.segment_1.value', predicate: 'with_children', value: 'foo' }` could return `foo`, `foo/bar`, `foo/baz`.

#### without_children
Example: `{ field: 'segments.segment_1.value', predicate: 'without_children', value: 'foo' }` could return `foo`.

#### only_children
Example: `{ field: 'segments.segment_1.value', predicate: 'only_children', value: 'foo' }` could return `foo/bar`, `foo/baz`.


### Exists Predicate
The `exists` predicate takes no value and tests if the field exists in the document. Some fields don't exist because the related feature wasn't enabled or failed during analysis. For instance, previous fields do not exist if the comparison feature is not enabled.

Example: `{ field: 'previous', predicate: 'exists' }`


### Multiple Prefix Predicates
Some fields like `query_string_keys` are 'multiple' fields, meaning they have a list of values. For instance, `query_string_keys` could be equal to `['page', 'length']` on a URL with pagination.

For this purpose, these fields predicates must be prefixed by `any.`

Example: `any.eq`, `any.contains` meaning any equal to, any contains.


## FieldFilter composition
FieldFilter can be composed with a boolean condition:

#### and
`{ "and: [FILTER_1, FILTER_2, ...] }`

#### or
`{ "or: [FILTER_1, FILTER_2, ...] }`

#### not
`{ "not: FILTER }`


## Example
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

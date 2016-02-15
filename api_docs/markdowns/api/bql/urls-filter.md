# UrlsFilter

`UrlsFilter` allows to define the filter to perform on URLs fields. It can be composed using boolean conditions (and, or, not).

## FieldFilter
A field filter allows to describe a predicate to apply on a given field.
```JSON
{
  "predicate": string,
  "field": string,
  "value": ?any,
}
```

## Predicates
According to the field type, several predicates can be applied. **Full list of fields** can be found in [[URLs Datamodel;urls-datamodel]].

### Numerical Predicates
Numerical fields have continuous values. Numerical fields include `integer`, `long`, `float`, `double`, `date` and `datetime` fields.

#### eq: Equals
```JSON
{ "predicate": "eq", "field": "http_code", "value": 200 }
```

#### gt: Greather than
```JSON
{ "predicate": "gt", "field": "http_code", "value": 200 }
```

#### gte: Greather than or equal
```JSON
{ "predicate": "gte", "field": "http_code", "value": 200 }
```

#### lt: Lower than
```JSON
{ "predicate": "lt", "field": "http_code", "value": 200 }
```

#### lte: Lower than or equal
```JSON
{ "predicate": "lte", "field": "http_code", "value": 200 }
```

#### between: Between
```JSON
{ "predicate": "between", "field": "http_code", "value": [200, 300] }
```
**Note**: Lower bondary is inclusive whereas **upper bondary is exclusive**, ie the above example means `200 <= http_code < 300`.


### Categorical Predicates
Categorical fields have discrete values. Categorical fields include `string`, `boolean` and `tree` fields.

#### eq: Equals
```JSON
{ "predicate": "eq", "field": "url", "value": 'https://botify.com' }
```

#### contains: Contains
```JSON
{ "predicate": "contains", "field": "url", "value": 'botify' }
```

#### starts: Starts with
```JSON
{ "predicate": "start", "field": "url", "value": 'https' }
```

#### ends: Ends with
```JSON
{ "predicate": "ends", "field": "url", "value": 'hifi' }
```

#### re: Match Regex
```JSON
{ "predicate": "re", "field": "url", "value": 'https.*hifi' }
```


### Tree Predicates
Tree fields can use both categorical predicates and some extra predicates making them easier to use. Tree fields are stored as flat strings like `for/bar`. Tree predicates make it easy to filter on children.

#### with_children
Returns given value and all its children.
```JSON
"segments"segment_1."value"',, { "field": " "predicate: 'with_childr', value: 'foo' }` could return `foo`, `foo/bar`, `foo/baz`.

#### without_children
```JSON
"segments"segment_1."value"',, { "field": " "predicate: 'without_childr', value: 'foo' }` could return `foo`.

#### only_children
```JSON
"segments"segment_1."value"',, { "field": " "predicate: 'only_childr', value: 'foo' }` could return `foo/bar`, `foo/baz`.


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

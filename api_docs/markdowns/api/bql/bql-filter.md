# BQLFilter

`BQLFilter` allows to define the filter to perform on URLs fields. It can be composed using boolean conditions (and, or, not).

## FieldFilter
A field filter allows to describe a predicate to apply on a given field. **Full list of fields** can be found in [[URLs Datamodel;urls-datamodel]].
```JSON
{
  "predicate": string,
  "field": string,
  "value": ?any,
}
```

## Predicates
According to the field type, several predicates can be applied.

### Numerical Predicates
Can be aplied on numerical fields including `integer`, `long`, `float`, `double`, `date` and `datetime` fields.

#### Equals
```JSON
{
  "predicate": "eq",
  "field": "http_code",
  "value": 200
}
```

#### Greather than
```JSON
{
  "predicate": "gt",
  "field": "http_code",
  "value": 200
}
```

#### Greather than or equal
```JSON
{
  "predicate": "gte",
  "field": "http_code",
  "value": 200
}
```

#### Lower than
```JSON
{
  "predicate": "lt",
  "field": "http_code",
  "value": 200
}
```

#### Lower than or equal
```JSON
{
  "predicate": "lte",
  "field": "http_code",
  "value": 200
}
```

#### Between
```JSON
{
  "predicate": "between",
  "field": "http_code",
  "value": [200, 300]
}
```
**Note**: Lower bondary is inclusive whereas **upper bondary is exclusive**, ie the above example means `200 <= http_code < 300`.


### Categorical Predicates
Can be applied on categorical fields including `string`, `boolean` and `tree` fields.

#### Equals
```JSON
{
  "predicate": "eq",
  "field": "url",
  "value": "https://botify.com"
}
```

#### Contains
```JSON
{
  "predicate": "contains",
  "field": "url",
  "value": "botify"
}
```

#### Starts with
```JSON
{
  "predicate": "start",
  "field": "url",
  "value": "https"
}
```

#### Ends with
```JSON
{
  "predicate": "ends",
  "field": "url",
  "value": "hifi"
}
```

#### Match regex
```JSON
{
  "predicate": "re",
  "field": "url",
  "value": "https.*hifi"
}
```


### Tree Predicates
`tree` fields can use both categorical predicates and some extra predicates making it easy to filter on their children. Tree fields are saved as flat strings like `for/bar`.

#### With children
Returns given value and all its children. For instance, the following could  returns `foo`, `foo/bar`, `foo/baz`.
```JSON
{
  "predicate": "with_childre",
  "field": "segment.segment_1.value",
  "value": "foo"
}
```

#### Without children
Returns matching value excludind children. For instance, the following could  only returns `foo`.
```JSON
{
  "predicate": "without_children",
  "field": "segment.segment_1.value",
  "value": "foo"
}
```

#### Only children
Returns matching children excluding parent. For instance, the following could  returns `foo/bar`, `foo/baz`.
```JSON
{
  "predicate": "only_children",
  "field": "segment.segment_1.value",
  "value": "foo"
}
```

### Exists Predicate
The `exists` predicate takes no value and tests if the field exists in the document. Some fields don't exist because the related feature wasn't enabled or failed during analysis. For instance, previous fields do not exist if the comparison feature is not enabled.
```JSON
{
  "predicate": "exists",
  "field": "previous"
}
```

### Multiple Prefix Predicates
Some fields can contains a list of values, they are called **multiple** fields. For instance, `query_string_keys` could be equal to `['page', 'length']` on a URL with pagination.

To filter on these fields, **predicates must be prefixed** by `any.` For instance, the following filters URLs on these having a query string key that is equal to "page".

```JSON
{
  "predicate": "any.eq",
  "field": "query_string_keys",
  "value": "page"
}
```


## FieldFilter composition
`FieldFilter` can be composed with some boolean condition.

### AND
```JSON
{
  "and": [
    FILTER_1,
    FILTER_2,
    ...
  ]
}
```

### OR
```JSON
{
  "or": [
    FILTER_1,
    FILTER_2,
    ...
  ]
}
```

### NOT
```JSON
{
  "not": FILTER
}
```


## Example
The following `BQLFilter` filters the analysis URLs dataset on new URLs which are compliant and have no title.
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

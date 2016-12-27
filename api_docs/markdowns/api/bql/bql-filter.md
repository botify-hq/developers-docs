# BQLFilter

`BQLFilter` allows to define the filter to perform on URLs fields. It can be composed using boolean conditions (and, or, not).

## FieldFilter
A field filter allows to describe a predicate to apply for a given field. **Full list of filterable fields** can be found in [[Analysis Datamodel;analysis-datamodel?filter=filters]].
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
Can be applied to numerical fields, including `integer`, `long`, `float`, `double`, `date` and `datetime` fields.

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
**Note**: Lower boundary is inclusive whereas **upper boundary is exclusive**. For instance the above example means `200 <= http_code < 300`.


### Categorical Predicates
Can be applied to categorical fields, including `string`, `boolean` and `tree` fields.

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
  "predicate": "starts",
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
Returns given value and all its children. For instance, the following filter could returns `foo`, `foo/bar` and `foo/baz`.
```JSON
{
  "predicate": "with_children",
  "field": "segments.segment_1.value",
  "value": "foo"
}
```

#### Without children
Returns matching value excluding children. For instance, the following filter could only returns `foo`.
```JSON
{
  "predicate": "without_children",
  "field": "segments.segment_1.value",
  "value": "foo"
}
```

#### Only children
Returns matching children excluding parent. For instance, the following filter could returns `foo/bar` and `foo/baz`.
```JSON
{
  "predicate": "only_children",
  "field": "segments.segment_1.value",
  "value": "foo"
}
```


### Timeseries predicates
`timeseries` fields contains a sequence of values for each day. Those fields are any available in the Logs API, where you need to define a range of dates you want to work on.
For instance, if you want to list the number of crawls by URL from the 1st of January to the 7th, `crawls.google.count_by_day` is a list, the first item is the number of crawls on Jan. 1st, the last item is the number of crawl on Jan. 7th.

#### On every dates
This example filters URLs that have been crawled at least once **every day on the period**. Note that you can use all numerical predicates (`all.eq`, `all.gte`, `all.gt`, `all.lt`, `all.lte` or `all.between`)
```JSON
{
  "field": "crawls.google.count_by_day",
  "predicate": "all.gte",
  "value": "1"
}
```

#### On any date
This example filters URLs that have been crawled at least once **whenever on the period**. Note that you can use any numerical predicates (`any.eq`, `any.gte`, `any.gt`, `any.lt`, `any.lte` or `any.between`)
```JSON
{
  "field": "crawls.google.count_by_day",
  "predicate": "any.gte",
  "value": "1"
}
```

#### On a date
This example filters URLs that have been crawled at least once the **first day on the period**. If you want the ones that have been crawled the second day, you would replace `[0]` by `[1]`.
```JSON
{
  "field": "crawls.google.count_by_day[0]",
  "predicate": "gte",
  "value": "1"
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
Some fields can contain a list of values, they are called **multiple** fields. For instance, `query_string_keys` could be equal to `['page', 'length']` on a URL with pagination.

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
      "field": "compliant.is_compliant",
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

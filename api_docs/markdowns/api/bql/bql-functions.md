# BQLFunction

## Usage

Using BQL, function calls can have different formats.
For a function with only one argument, it can be called as:
```JSON
{"function_name": "field_name"}
```
For functions with more than one argument, the `"function"` and `"args"` 
keywords must be used:
```JSON
{
    "function": "function_name",
    "args": [
        "field_name_1",
        "field_name_2"
    ]
}
```

### Handling literal values

Function arguments are generally taken as field names, with few exceptions.
Literal numerical values, boolean values, and `NULL` are recognized. Literal
string can be specified with:
```json
{"literal": "a string"}
```

## Functions

### Mathematical Functions

The Mathematical Functions output a numerical value or `null`.

- `add`
    - Input: any number of numerical values
- `sub`
    - Input: any number of numerical values
- `mul`
    - Input: any number of numerical values
- `div`
    - Input: 2 numerical values

Example:
```JSON
{
    "function": "sub",
    "args": [
        "search_console.period_1.count_clicks",
        "search_console.period_0.count_clicks"
    ]
}
```

### Date Functions

All BQL Date Functions take one input parameter.

- `first_day_of_week`
    - Input: Date or Datetime
    - Output: Date
- `first_day_of_month`
    - Input: Date or Datetime
    - Output: Date
- `date`
    - Input: Datetime
    - Output: Date
- `year`
    - Input: Date or Datetime
    - Output: Integer
- `month`
    - Input: Date or Datetime
    - Output: Integer
- `year_month`
    - Input: Date or Datetime
    - Output: String
- `year_week_number_starting_monday`
    - Input: Date or Datetime
    - Output: String
- `year_week_number_starting_sunday`
    - Input: Date or Datetime
    - Output: String

Example:
```JSON
{"first_day_of_week": "search_console.period_0.date"}
```

### Count Functions

* `count`
* `count_true`
* `count_false`
* `count_null`
* `count_distinct`
* `count_distinct_approx`

Conditional counts: these are shortcuts to applying `count_true` to the corresponding boolean function.

* `count_eq`
* `count_gt`
* `count_gte`
* `count_lt`
* `count_lte`
  
### HTTP Code Functions

- `http_code_family`
    - Input: Integer
    - Output: String formatted as "2xx", "3xx", ... or "exx"
- `http_code_quality`
    - Input: Integer
    - Output: String "good" or "bad"

### JSON Functions

BQL supports retrieving any kind of field as a JSON-formatted string.

- `to_json_string`
    - Input: 1 argument of any type
    - Output: String

### Multiple Functions

- `first`
    - Input: 1 multiple value
    - Output: Type of first value


### Boolean Functions

- `eq`
- `ne`
- `lt`
- `lte`
- `gt`
- `gte`
- `and`
- `or`
- `not`
- `exists`
- `not_exists`

### Logical Functions

- `if`: returns one of two values according to a boolean condition.

    - input: Boolean, Any, Any
    - output: Any

    The two possible return values must be the same type.

    Example:

```json
{
    "function": "if",
    "args": [
        {
            "function": "exists",
            "args": [
                "segments.pagetype.depth_2"
            ]
        },
        "segments.pagetype.depth_2",
        {"literal": "#empty"}
    ]
}
```

- `if_not_exists`: returns the first field's value if it exists, the second field's value otherwise. 
    - input: Any, Any
    - output Any

    The two possible return values must be the same type.
    
    This is a shortcut for the previous example:

```json
{
    "function": "if_not_exists",
    "args": [
        "segments.pagetype.depth_2",
        {"literal": "#empty"}
    ]
}
```

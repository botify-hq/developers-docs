# BQLFunction

## Usage

Using BQL, function calls can have different formats.
For a function with only one argument, it can be called as:
```JSON
{"function_name": "field_name"}
```
For functions with more than one argument, the keywords `"function"` and `"args"` must be used:
```JSON
{
    "function": "function_name",
    "args": [
        "field_name_1",
        "field_name_2"
    ]
}
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

Example:
```JSON
{"first_day_of_week": "period_0.date"}
```

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

# Get URL Detail

Botify API allows you to get in information collected by Botify on analysed URLs. **Full list of requestable fields** can be found in [[URLs Datamodel;urls-datamodel]].

## Endpoint

- Operation: [[getUrlDetail;reference#!/Analysis/getUrlDetail]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls/{url}`
- HTTP Verb: GET
- Response: `Object`

```SH
curl 'https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}/urls/${url}?fields=${fields}' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json'
```

## Example

The following url returns the fields `http_code`, `delay_last_byte` and `outlinks_internal` of the url `http://www.nytimes.com/` (note that the url needs to be encoded).

```SH
https://api.botify.com/analyses/adam_warlock/demo-project/20150929/urls/http%3A%2F%2Fwww.nytimes.com%2F?fields=http_code,delay_last_byte,outlinks_internal
```

A sample result would be the following. Requested fields and their children are returned. If would have only needed to get the number of unique internal outlinks, we should have requested `outlinks_internal.nb.unique` in the fields list instead of the parent `outlinks_internal`.
```JSON
{
  "delay_last_byte": 254,
  "http_code": 200,
  "outlinks_internal": {
    "nb": {
      "follow": {
        "unique": 29,
        "total": 31
      },
      "unique": 29,
      "total": 31,
      "nofollow": {
        "combinations": {
          "link_meta_robots": 0,
          "robots": 0,
          "meta": 0,
          "link": 0,
          "link_meta": 0,
          "meta_robots": 0,
          "link_robots": 0
        },
        "unique": 0,
        "total": 0
      }
    }
  }
}
```

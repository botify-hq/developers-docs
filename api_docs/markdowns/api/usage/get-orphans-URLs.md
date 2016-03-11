# Get Orphans URLs

Orphans URLs are URLs which are **not in your website structure** (or in the scope of the crawl) but which were **crawled by a search engine** or **received visits**.


## Google Analytics Orphans URLs

## Endpoint

- Operation: [[getUrlDetail;reference#/Analysis/getUrlDetail]]
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
https://api.botify.com/v1/analyses/adam_warlock/demo-project/20150929/urls/http%3A%2F%2Fwww.nytimes.com%2F?fields=http_code,delay_last_byte,outlinks_internal

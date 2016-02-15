# List analyses

Botify API can returns your list of project of a given user.

## Endpoint

- Operation: [[getProjects;reference#Project_getProjects]]
- Path: `analyses/{username}/{project_slug}`
- HTTP Verb: GET
- Response: `Array<Project>`

```SH
curl 'https://api.botify.com/v1/projects/${username}' \
     -X GET \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json'
```

## Example of response
The response contains the list of project which belongs to the user. For each project, several information are given including project slug, related user and project settings.

```JSON
{
  "count": 1,
  "page": 1,
  "size": 1,
  "results": [
    {
      "name": "techcrunch.com",
      "slug": "techcrunch.com",
      "active": true,
      "date_created": "2014-12-23T17:56:02.655Z",
      "user": {
        "login": "annabelle",
        "email": "...",
        "is_organization": false,
        "url": "https://app.botify.com/annabelle/",
        "date_joined": "2014-04-09T05:51:27Z",
        "first_name": "",
        "last_name": "",
        "company_name": null
      },
      "current_settings": {
        "start_urls": [
          "http://techcrunch.com"
        ],
        "max_nb_pages": 20000,
        "max_depth": null,
        "compare_crawl": true,
        "blacklisted_domains": null,
        "allowed_domains": [
          {
            "domain": "techcrunch.com",
            "protocol": "both",
            "allow_subdomains": true
          }
        ],
        "respect_nofollow": true,
        "crawl_gzip": true,
        "has_robots_txt": false,
        "user_agent": "Mozilla/5.0 (compatible; botify; http://botify.com)",
        "max_pages_per_sec": 3,
        "extra_headers": null,
        "google_social_auth_id": null,
        "google_analytics_site_id": null,
        "google_analytics_account_email": null,
        "google_analytics_nb_days": 30,
        "sitemaps": null,
        "header_settings": null
      }
    }
  ]
}
```

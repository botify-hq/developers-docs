# Analysis Features

According to analysis configuration and set up integrations, some features can be enabled or not (for instance Search Engines feature is only available if you subscribe to the Log Analyzer option).

Features include:

- [[**main**;analysis-features-main]]: Depth, Load Time, HTTP Codes, HTML Tags
- [[**links**;analysis-features-links]]: Inlinks/Outlinks, Internal Pagerank, Top Domains, Prev/next
- [[**segments**;analysis-features-segments]]: Custom website segmentation (by pagetype, etc.)
- [[**visits**;analysis-features-visits]]: Data imported from Google Analytics to compute visits
- [[**search_engines**;analysis-features-search-engines]]: Data imported from Logs to compute search engines' crawl and organic visits.
- **content_quality**: Pages' content quality (unicity, similarity)
- **sitemaps**: Data imported from your sitemaps
- **extract**: HTML Extract
- **rel:** Hreflang tags
- **comparison**: Comparison to previous analysis


## List enabled features

To list enabled features, you need to request the [[analysis summary;analysis-get-summary]]. The response contains the list of enabled features with their configuration.

If a feature is enabled, the feature property is present and not equal to `null`. For most of features, additional data (like **configuration or prefetch results**) is available in feature value. For more details, please refer to the related documentation section.

```JSON
{
  "features": {
    "main": ?Object,
    "links": ?Object,
    "segments": ?Object,
    "visits": ?Object,
    "search_engines": ?Object,
    "sitemaps": ?Object,
    "extract": ?Object,
    "rel": ?Boolean,
    "comparison": ?Object
  },
  ...
}
```

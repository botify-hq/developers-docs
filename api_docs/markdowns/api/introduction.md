# Introduction

Botify provides a REST API to integrate Botify into third-party applications and allow to use almost any data available in the Botify interface or via the Botify Chrome Extension.

## Use cases
The basic idea of the API is to give you the pieces you need to **integrate Botify into your own solutions** to keep your website optimized and your team focussed on improving your SEO performance.

- **Go deeper into the analysis** of your website as the API allows you to get the metrics YOU want that could be not available in the Botify application.
- **Keep your internal dashboards up-to-date** with the most recent data on your website.
- Get an **overview of all your websites**.
- **Complement Botify data with other sources** like Google Search Console, Majestic SEO or even sales results, product inventory, etc.
- **Show alerts in your CMS** regarding some page's content to keep your SEO optimized.
- **Create reports** for your marketing, product or engineering team.
- Automatically **generate sitemaps** to make Google awared of new URLs or newly updated or fixed URLs.
- **Rise some alerts** in internal monitoring solutions when new issues occurs on your website (increase of errors, unexpected changes in internal linking, etc).
- Develop some **non regression systems** to ensure that evolutions on your website won't effect your SEO performance.
- ... and more, it's up to you!

## Possibilities
For now, the Botify API is **only pulling data from Botify Analytics**, meaning that **you can get any data related to an analysis**.
Current technical possibilities of the Botify API include:

- **List** your Botify Analytics **projects and analyses**.
- Get **live statistics** while Botify Analytics is crawling your website.
- **Compute insights**: i.e. number of compliant URLs, number of active URLs, number of pages crawled by Google, average depth, etc.
- **Aggregate URLs data** to create custom charts and metrics.
- **Search for URLs** matching a filter, based on any indicator or URL patterns.
- Get **information about any URL crawled by Botify Analytics**: HTTP status code, load  time performance, number of inlinks, of outlinks, of organic visits, presence in sitemaps, internal pagerank, etc.
- Get **information about** other URLs including **orphan URLs**, **top external domains** your website links to, **URLs found in your sitemaps**.
- **Export URLs**
- ... and more

#### Current limitations
It is not possible to get data from the Botify Log Analyzer dashboard **yet**, thus you can't get the number of unique/total crawls day by day for now.
However, you can get search engines crawl data as shown in the Botify Analytics report's Search Engines tab. This data is computed on the last of 30 days of logs and is available only for analyzed URLs (URLs in your Botify Analytics project's crawl scope).

#### Data Aggregation
The Botify API isn't working in a way where you would request a specific chart. Instead, you'll use **[[BQL;bql]]** (Botify Query Language) to perform aggregations and filters on analyzed URLs.
It means that **it's much more powerful** because you are able to **compute any metric and generate any chart you want** including some that aren't in the Botify interface.

## Demo
You can find a demo of the API [there](https://jsfiddle.net/8k20pbua/12/).
But the best API demo is the **Botify Analytics Application** itself, as it is using the API to display/modify (almost) everything.

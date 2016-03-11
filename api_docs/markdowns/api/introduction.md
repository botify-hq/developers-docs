# Getting started

Botify provides a REST API to integrate Botify into third-party applications and allow to use almost any data available in the Botify interface or via the Botify Chrome Extension.

<a href="https://docs.google.com/forms/d/1T6D588024flDKHS6q_IMlVMS-q8rmRvgzBIc8EZdyDo/viewform" class="inscription-button" target="_blank">Request access to the alpha version of the Botify API</a>

## Use examples
- **Integrate Botify Data into existing dashboards**.
- Create dashboards showing an **overview of all your websites**.
- Create **reporting for the product or engineering team**
- **Complement Botify data with other sources** like Google Search Console, Majestic SEO or even sales results, products inventory, etc.
- **Automate exports** after each crawl to get list of error pages (404, 500, ...), most visited pages, extracted data, etc.
- ... What are your own ideas?

## Possibilities
For now, the Botify API is **only pulling data from Botify Analytics**, meaning that **you can get any data related to an analysis**.

Current technical possibilities of the Botify API includes:
- **List** your Botify Analytics **projects and analyses**.
- Get **live statistics** while Botify Analytics is crawling your website.
- **Compute insights**: ie: number of compliant URLs, number of active URLs, number of pages crawled by Google, average depth, etc.
- **Aggregate URLs data** to create custom charts and metrics.
- **Search for URLs** matching a filter, based on any indicator or URL patterns.
- Get **information about any URL crawled by Botify Analytics**: HTTP status code, load  time performance, number of inlinks, of outlinks, of organic visits, presence in sitemaps, internal pagerank, etc.
- Get **information about** other URLs including:
&nbsp;&nbsp;- **orphan URLs**: URLs which are **not in your website structure** (or in the scope of the crawl) but which were **crawled by a search engine** or **received visits**.
&nbsp;&nbsp;- **top external domains** your website links to.
&nbsp;&nbsp;- **URLs found in your sitemaps**.
- **Export URLs**
- ... and more

#### Current limitations
It is not possible to get data from the Botify Log Analyzer dashboard **yet**, thus you can't get the number of unique/total crawls day by day for now.
However, you can get search engines crawl data as shown in the Botify Analytics report's Search Engines tab. This data is computed on the last of 30 days of logs and is avalaible only for analyzed URLs (URLs in your Botify Analytics project's crawl scope).

#### Data Aggregation
The Botify API isn't working in a way where you would request a specific chart. Instead you'll use **[[BQL;bql]]** (Botify Query Language) to perform aggregations and filters on analyzed URLs.
It means that **it's much more powerful** because you are able to **compute any metric and generate any chart you want** including some that aren't in the Botify interface.

## Coming soon
- Allow to get **daily search engine crawl and organic visits data** (from Botify Log Analyzer)
- Allow to launch Botify Analytics crawls
- SDKs for other languages


## Demo
You can find a little demo of the API [there](https://jsfiddle.net/8k20pbua/12/).
But the best API demo is the **Botify Analytics Application** itself, as it is using the API to display/modify (almost) everything.

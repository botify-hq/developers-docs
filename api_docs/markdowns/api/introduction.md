# Getting started

Botify provides a REST API to integrate Botify into third-party applications and allow to use almost any data available in the Botify interface or via the Botify Chrome Extension.

<a href="https://docs.google.com/forms/d/1T6D588024flDKHS6q_IMlVMS-q8rmRvgzBIc8EZdyDo/viewform" class="inscription-button" target="_blank">Request access to the alpha version of the Botify API</a>

## Use examples
- Build your own graphs and integrate them into existing dashboards
- Get the list of all your projects and analyses
- Get crawl statistics while Botify is exploring your website
- Search for URLs matching complex filters, based on any indicator or URL patterns
- Perform complex data aggregations using our URL data model
- Get information about any URL crawled by Botify: HTTP status code, load  time performance, number of inlinks, of outlinks, of organic visits, presence in sitemaps, internal pagerank, etc.
- Get information about other URLs found in the report: top external domains your website links to, orphan URLs (found in Google analytics data but not found through links on your website)
- Create automated CSV exports
- ... and much more

## Topics
- [[Authentication;authentication]]
- [[Usage;usage]]
- [[Reference;reference]]
- [[URLs Datamodel;urls-datamodel]]
- [[BQL;bql]]
- [[Error Codes;error-codes]]
- [[Rate Limit;rate-limit]]
- [[Jobs;jobs]]
- [[SDKs;sdks]]

## Demo
You can find a little demo of the API [there](https://jsfiddle.net/8k20pbua/11/).
But the best API demo you can have is the **Botify Analytics Application**, as it is using the API to display/modify (almost) every thing.

## Complex aggregations and filtering
Complex aggregation and filtering can be performed on analyzed URLs data. For that purpose, we developed a query language named **BQL** (Botify Query Language). Please read this page for [[more information on BQL;bql]]


# Getting started

The purpose of this page is to guide you in the Botify API capabilities.

- [Get your token](#get-your-token)
- [Get my projects and analyses](#get-my-projects-and-analyses)
- [Get some data about my analyses](#get-some-data-about-my-analyses)
- [Futher reading](#further-reading)
- [SDK](#sdk)


## Get your token

To use the API, you need an active user account with the API feature enabled. Once the API enabled you can get your token in your [profile settings](https://app.botify.com/account).


## Get my projects and analyses

- List your projects: [[getUserProjects;user-list-projects]]
- List your project's analyses: [[getProjectAnalyses;project-list-analyses]]


## Get some data about my analyses

In the Botify API, you use **[[BQL;bql]]** (Botify Query Language) to perform operations on analyzed URLs.
This language allow you define fields you want to **compute metrics on**, **group on**, **filter on**, or **select**. List of fields is available in [[Urls Datamodel;analysis-urls-datamodel]].

- Get some metrics (ex: number of visits, links) for an analysis: [[getUrlsAggs;analysis-aggregate-urls]]
- Get the evolution of metrics on your last analyses: [[getProjectUrlsAggs;analysis-aggregate-urls]]
- Find some URLs matching a filter: [[getUrls;analysis-list-urls]]
- Get information on an URL: [[getUrlDetails;analysis-get-url-info]]
- Export all my URLs: [[createUrlsExport;analysis-csv-export]]

Note that **exporting all your URLs is only recommended if you want to cross Botify data to others sources** (by matching URL to URL data sources). Indeed using URL aggregation to compute metrics or URL searching is way faster. Plus, according to your plan, csv export can be limited in volume, leading to imcomplete results.


## Futher reading

- [[API Reference;reference]]
- [[URL Datamodel;analysis-urls-datamodel]]
- [[Analysis;analysis]]
- [[Analysis Features;analysis-features]]
- [[Project;project]]
- [[BQL;bql]]


## SDK

We provide API clients to allow you to start using the Botify API within minutes! If you'd like us to provide others SDKs, tell us on.

# Getting started

The purpose of this page is to guide you in the Botify API capabilities.

- [Get API access](#get-api-access)
- [Get your token](#get-your-token)
- [List my projects and analyses](#list-my-projects-and-analyses)
- [Get data about my analyses](#get-data-about-my-analyses)
- [Demo](#demo)
- [Further reading](#further-reading)


## Get API access

To use the API, you need an active **user account with the API feature enabled**. To do so, either contact your account manager or [start a free trial](https://app.botify.com/request_free_trial/).


## Get your token

Once the API is enabled, you can get your token in your [profile settings](https://app.botify.com/account).


## List my projects and analyses

- List your projects: [[getUserProjects;user-list-projects]]
- List your project's analyses: [[getProjectAnalyses;project-list-analyses]]


## Get data about my analyses

In the Botify API, you use **[[BQL;bql]]** (Botify Query Language) to perform operations on analyzed URLs.
This language allow you define fields you want to **compute metrics on**, **group on**, **filter on**, or **select**. List of fields is available in [[Analysis Datamodel;analysis-datamodel]].

- Get some metrics (ex: number of visits, links) for an analysis: [[getUrlsAggs;analysis-aggregate-urls]]
- Get the evolution of metrics on your last analyses: [[getProjectUrlsAggs;analysis-aggregate-urls]]
- Find some URLs matching a filter: [[getUrls;analysis-list-urls]]
- Get information on an URL: [[getUrlDetails;analysis-get-url-info]]
- Export all my URLs: [[createUrlsExport;analysis-csv-export]]

Note that **exporting all your URLs is only recommended if you want to cross Botify data to others sources** (by matching URL to URL data sources). Indeed using URL aggregation to compute metrics or URL searching is way faster. Plus, according to your plan, csv export can be limited in volume, leading to imcomplete results.

## Further reading

- [[API Reference;reference]]
- [[Analysis;analysis]]
- [[Analysis Features;analysis-features]]
- [[Analysis Datamodel;analysis-datamodel]]
- [[Project;project]]
- [[BQL;bql]]

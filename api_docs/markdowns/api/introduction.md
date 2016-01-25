# Introduction

Botify provides a REST API to integrate Botify in third-party applications and use almost everything available in the Botify Analytics App and its Chrome Extension.

## Topics
- [Authentication](./authentication.md)
- [URLs Data Fetching](./urls-data-fetching.md)
- [URLs Data Aggregation](./urls-data-aggregation.md)
- [URLs Data Model Introspection](./urls-datamodel-introspection.md)
- [BQL](./bql.md)
- [Reference](./reference.md)
- [Error Codes](./error-codes.md)
- [Rate Limit](./rate-limit.md)
- [SDK](./sdk.md)

## Examples of use
- Get the list of your projects and analyses.
- Get crawl statistics.
- Search for URL matching complex filters.
- Perform complex aggregations on analysis URL model.
- Get information on any analysed URL: status, performance, inlinks, outlinks, visits, presence in sitemaps, pagerank, etc
- Get information about top external domains, orphan URLs, lost pagerank, sitemaps, etc.
- Create CSV Exports.
- ... and much more

## Complex aggregations
Complex aggregation can be performed on analysed URLs data. For that purpose, we developed a query language named **BQL** (Botify Query Language). Please read this page for [more information on BQL](./bql.md).


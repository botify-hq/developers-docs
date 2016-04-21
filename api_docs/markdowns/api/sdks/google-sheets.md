# Botify for Google Sheets

**Botify for Google Sheets** allows you to easily get Botify data in your spreadsheets.
Note that, currently only a small subset of the API is supported by this SDK. Feel free to customize our macros or contributing to the project.


## Install

- Open the [addon page](https://chrome.google.com/webstore/detail/botify-for-google-sheets/albleinfohecbdikaabneehekfmdgimk?authuser=0).
- Click on Add


## Macros

Every macro is prefixed by Botify, thus typing `=BOTIFY` in a cell formula  should show you the available macros thanks to the autocompletion.

### Get latest project's analyses
```
/**
 * Return the latest analyses of a given project.
 * @param {String} apiToken Botify API token
 * @param {String} username Username of the project owner
 * @param {String} projectSlug Project's slug
 * @param {Number} nbAnalyses Number of analyses to get
 * @return {Array} The list of analyses.
 * @customfunction
 */
BOTIFY_PROJECT_LIST_ANALYSES(apiToken, username, projectSlug, nbAnalyses) {
```

##### Example
![image](https://cloud.githubusercontent.com/assets/1886834/14710250/ec3efac0-07d4-11e6-83fb-a202a5cc2558.png)


### Aggregate analysis URLs data
```JS
/**
 * Return the result of the aggregation on URLs of a given analyses
 * @param {String} apiToken Botify API token
 * @param {String} username Username of the project owner
 * @param {String} projectSlug Project's slug of the analysis
 * @param {String} analysisSlug Analysis's slug
 * @param {BQLAggsQuery} urlsAggsQuery BQL Aggregation Query to perform
 * @param {Boolean} showHeaders Show Groups and Metrics headers (default to true)
 * @return {Array} The result of the aggregation.
 */
BOTIFY_ANALYSIS_AGGREGATE_URLS(apiToken, username, projectSlug, analysisSlug, urlsAggsQuery, showHeaders)
```

For more information about how to define aggregation queries please refer to the [[BQLAggsQuery documentation;bql-aggs-query]].

##### Example
![image](https://cloud.githubusercontent.com/assets/1886834/14710196/ac0f7dda-07d4-11e6-8dcb-c624c597fb42.png)


### Get detail on a specific URL
```JS
/**
 * Return the requested fields of a given URL
 * @param {String} apiToken Botify API token
 * @param {String} username Username of the project owner
 * @param {String} projectSlug Project's slug of the analysis
 * @param {String} analysisSlug Analysis's slug
 * @param {String} url Url to get detail on
 * @param {Range}  Range of fields to fetch (ex A1:A4)
 * @param {Boolean} showHeaders Show Groups and Metrics headers (default to true)
 * @return {Array} The value of the fields
 */
BOTIFY_ANALYSIS_GET_URL_DETAIL(apiToken, username, projectSlug, analysisSlug, url, fields, showHeaders)
```

##### Example
![image](https://cloud.githubusercontent.com/assets/1886834/14710345/5ac5da54-07d5-11e6-8be2-36a318c0fdea.png)


## FAQ

### How to get my API token?
You can get your API token in your user account page as explained [[there;authentication#get-your-api-token]].

### How to get my projectSlug and analysisSlug?
An easy way to get your projectSlug and analysisSlug is with the URL of your analysis report.
In the following example, `adam_warlock` is the username, `demo-project` is the projectSlug and `20160308` is the analysisSlug.

![image](https://cloud.githubusercontent.com/assets/1886834/14709625/e8aadb52-07d1-11e6-92f0-21dda26a6331.png)

### How to get the list of available fields?
A full list of available fields to display or compute metrics on can be found in the [[Urls Datamodel;analysis-urls-datamodel]].

### How to get the source code of the macros?
The source code of the Botify Google Sheets addon is open source and available on [Github](https://github.com/botify-labs/botify-sdk-google-sheets). Feel free to customize our macros or contributing to the project.


## Troubleshooting

### I'm getting an #ERROR! with the code **429**

The HTTP Status Code 429 means that you reached the Botify API rate limit.
Keep in mind that each cell using a Botify Macro is requesting the Botify API on background, thus an excessive usage of Botify Macros may reach the limit.
Refer to [[Rate Limit documentation;rate-limit]] for more details.

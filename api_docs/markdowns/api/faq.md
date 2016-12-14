# FAQ

### What can I do with the Botify API

The basic idea of the API is to give you the pieces you need to integrate Botify into your own solutions or build specific program designed for you. There is plenty of things you can do with the Botify API, you can get some examples [[there;introduction#use-examples]] but it's mostly up to you and your company.

### How to get my API token?
You can get your API token on your user account page. Please refer to [[authentication;authentication]] section.


### I'd like to get some data about my analyses, where do I start ?
There are many ways to get data about your analyses. The [[Getting Started;getting-started#get-some-data-about-my-analyses]] section explains the main ones and when you should use one and not another.


### How to get my projectSlug and analysisSlug?
An easy way to get your project's slug and analysis's slug is by seeing the URL of your analysis report.

In the following example, `adam_warlock` is the username, `demo-project` is the projectSlug and `20160308` is the analysisSlug.
![image](https://cloud.githubusercontent.com/assets/1886834/14709625/e8aadb52-07d1-11e6-92f0-21dda26a6331.png)

An other way is by using [[getUserProjects;user-list-projects]] and [[getProjectAnalyses;project-list-analyses]] operations.


### How to get the list of available fields?
A full list of available fields to select, filter and compute metrics can be found in the [[Urls Datamodel;analysis-datamodel]].


### How pagination works ?
Every paginated operation uses a **page** and a **size** query string parameters.


### I'm not a developer, can I use the API?
Our [[Google Sheets Plugin;integrations-google-sheets]] allows you to get Botify data into your spreadsheets, and then using speadsheets capatilities to build dashboards with customs metrics and charts.
Though programing is not black magic science, **everyone can learn**! Really! Learning something new is always interesting and will allow you to develop your own programs according to your needs. We would recommend you to start with an easy to learn language like Javascript on [Code School](#https://www.codeschool.com/courses/javascript-road-trip-part-1) or [Code Academy](#https://www.codecademy.com/learn/javascript).

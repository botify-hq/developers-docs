# FAQ

### How to get my API token?
If you requested access to the Botify API, you can get your API token on your user account page as explained [[there;authentication]].

<a href="https://docs.google.com/forms/d/1T6D588024flDKHS6q_IMlVMS-q8rmRvgzBIc8EZdyDo/viewform" class="inscription-button" target="_blank">Request access to the alpha version of the Botify API</a>


### How to get my projectSlug and analysisSlug?
An easy way to get your projectSlug and analysisSlug is with the URL of your analysis report.

In the following example, `adam_warlock` is the username, `demo-project` is the projectSlug and `20160308` is the analysisSlug.
![image](https://cloud.githubusercontent.com/assets/1886834/14709625/e8aadb52-07d1-11e6-92f0-21dda26a6331.png)

An other way is by using [[getUserProjects;project-list-projects]] and [[getProjectAnalyses;analysis-list-analyses]] operations.


### How to get the list of available fields?
A full list of available fields to select, filter and compute metrics can be found in the [[Urls Datamodel;analysis-urls-datamodel]].


### How pagination works ?
Every paginated operation uses a **page** and a **size** query string parameters.


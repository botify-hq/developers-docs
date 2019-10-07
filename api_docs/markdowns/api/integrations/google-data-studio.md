# Google Data Studio Connector

Botify's **Google Data Studio Connector** allows you to easily get Botify data in your Google Data Studio Dashboards.

## Install
### Creating a new Data Studio Dashboard with your Botify data
- Open the [Data sources](https://datastudio.google.com/data?search=Botify) list on Google's Connector Gallery
- Find the "Botify API" Connector
- Click on "CREATE DATA SOURCE":
<img width="40%" src="/staticfiles/images/data-studio/botify-data-source.png"/> 
- Authorize the Connector in your Google account
<img width="40%" src="/staticfiles/images/data-studio/authorization-oauth.png"/> 
- Insert your Botify API Token (see [[here;authentication]] for information on how to retrieve it)
<img width="40%" src="/staticfiles/images/data-studio/authorization-token.png"/> 
- You can now select a Botify project from which to pull data. Enter the username and project slug for the project you wish to target.
<img width="40%" src="/staticfiles/images/data-studio/setup-target-project.png"/> 
- Your report will be created, with the full range of Botify's metrics on your project.

### Adding your Botify data into an existing Data Studio Dashboard
- While editing your Data Studio report, click on "Resource" => "Manage Added Data Sources"
<img width="40%" src="/staticfiles/images/data-studio/manage-data-sources.png"/> 
- Click on "Add A Data Source"
- Find the "Botify API" Connector
- Click on "ADD DATA SOURCE"
<img width="40%" src="/staticfiles/images/data-studio/botify-data-source.png"/> 
- Authorize the Connector in your Google account
<img width="40%" src="/staticfiles/images/data-studio/authorization-oauth.png"/> 
- Insert your Botify API Token (see [[here;authentication]] for information on how to retrieve it)
<img width="40%" src="/staticfiles/images/data-studio/authorization-token.png"/> 
- You can now select a Botify project from which to pull data. Enter the username and project slug for the project you wish to target.
<img width="40%" src="/staticfiles/images/data-studio/setup-target-project.png"/> 
- Your report will be created, with the full range of Botify's metrics on your project.

## FAQ

### How to get my API token?
You will find your API token in your user account page, as explained [[here;authentication]].

### How to get my username and project slugs?
The simplest way to get your username and project slugs is to access your project on the Botify platform: you'll find the slugs in the URL. 

### How to get the list of available fields?
A full list of available fields to display or compute metrics on can be found in the [[Analysis Datamodel;analysis-datamodel]].

## Troubleshooting

### I need to revoke my API Token used by the Connector
- Open the [Data sources](https://datastudio.google.com/data?search=Botify) list on Google's Connector Gallery
- Find the "Botify API" Connector
- Click on the "three-dot" menu icon
- Click on "Revoke Access"
<img width="40%" src="/staticfiles/images/data-studio/authorization-revoke.png"/> 




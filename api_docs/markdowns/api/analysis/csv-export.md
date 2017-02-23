# CSV Export

Botify API allows you to export your crawled URLs (and their metadata) as a CSV file. Crawled URLs can be filtered in order to export only a subset of URLs. Full list of requestable fields can be found in [[Analysis Datamodel;analysis-datamodel]].

Be noticed that CSV exports are **by default limited to 100,000 URLs**. Contact your account manager if you need to increase this limit.


## CSV Export are asynchronous

Some operations like creating a CSV export need to be done asynchronously because they can take more time than common timeouts can accept. To do so, we use a **[polling mechanism](https://en.wikipedia.org/wiki/Polling_(computer_science))**:

To create a CSV, you need to:
- First call [[createUrlsExport;reference#/Analysis/createUrlsExport]] which returns a job id.
- Then poll [[getUrlsExportStatus;reference#/Analysis/getUrlsExportStatus]] every X seconds (using that job id) till the export is done.

Note that the [Job middleware](https://github.com/botify-labs/botify-sdk-js-middlewares/blob/master/docs/middlewares/jobsMiddleware.docs.md) of the Javascript SDK implements this logic making it much easier to use asynchronous operations.


## Endpoints

### createUrlsExport

- Operation: [[createUrlsExport;reference#/Analysis/createUrlsExport]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls/export`
- HTTP Verb: POST
- Body : `Array<BQLQuery>`
- Response: `Pagination<BQLResult>`

Please refer to [[BQLQuery;bql-query]] documentation for information about how to define fields to select and filters.

```SH
curl "https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}/urls/export" \
     -X POST \
     -H "Authorization: Token ${API_KEY}" \
     -H "Content-type: application/json" \
     --data-binary "${BQLQuery}"
```

### getUrlsExportStatus

- Operation: [[getUrlsExportStatus;reference#/Analysis/getUrlsExportStatus]]
- Path: `analyses/{username}/{project_slug}/{analysis_slug}/urls/export/{url_export_id}`
- HTTP Verb: GET
- Response: `CsvExportStatus`

```SH
curl "https://api.botify.com/v1/analyses/${username}/${project_slug}/${analysis_slug}/urls/export" \
     -X GET \
     -H "Authorization: Token ${API_KEY}" \
```


## Example

### Prepare your request

The following example of [[BQLQuery;bql-query]] fetches `url` and `metadata.title.nb` fields and filters the dataset on new URLs that respond with a 2xx HTTP code.

```JSON
{
  "fields": [
    "url",
    "metadata.title.nb"
  ],
  "filters": {
    "and": [
      {
        "field": "http_code",
        "predicate": "between",
        "value": [200, 300]
      },
      {
        "not": {
          "field": "previous",
          "predicate": "exists"
        }
      }
    ]
  }
}
```

### Start the export

You first use **createUrlsExport** to start the CSV export. The response could be the following.
```JSON
{
  "job_id": 19381,
  "job_url": "https://api.botify.com/v1/analyses/username/project_slug/analysis_slug/urls/export/19381",
  "job_status": "CREATED",
  "date_created": "2016-06-01T10:07:03.309416Z",
  "query": ...,
  "area": "current",
  "nb_results": null,
  "results": null
}
```

### Poll status till finished

Then poll start polling **getUrlsExportStatus** till `job_status` equals `DONE` (or `FAILED`). Once the export is finished, the response could be the following:
- `nb_results` gives you the number of URLs exported.
- `results.download_url` gives you the URL of the **zip file** containing your CSV export.
```JSON
{
  "job_id": 19381,
  "job_url": "https://api.botify.com/v1/analyses/username/project_slug/analysis_slug/urls/export/19381",
  "job_status": "DONE",
  "date_created": "2016-06-01T10:07:03.309416Z",
  "nb_results": 275,
  "area": "current",
  "query": ...,
  "results": {
    "download_url": "https://d121xa69ioyktv.cloudfront.net/csv_exports/10ebf8c8de4a8d4e47ca1da766704d7d.zip"
  }
 }
```



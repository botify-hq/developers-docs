# Error Codes

When a client error occurs, a 4xx HTTP status code is returned with the following error payload. `error_code` provides an error code which is more specific than the HTTP status code. Error codes are listed below.
```JSON
{
  "error": {
    "error_code": string,
    "message": string
  }
}
```

## List
Error Code | Message
--- | ---
1 | Not Authorized
2 | Permission denied
3.1 | Analysis not found
3.2 | Insight not found
3.3 | URL export not found
3.4 | User not found
3.5 | Revision not found
3.6 | Query not found
3.7 | Project not found
3.8 | Crawl Statistics Data currently not available
3.9 | PDF Export not found
3.10 | Dry run segment not found
3.11 | Segment Rule not found
4 | Bad regular expression
5 | 'Fields' is mandatory
6 | No result for this URL
7 | 'Identifiers' is mandatory
8 | Invalid area
9 | Badly formatted request
9.1 | Query not found on request
9.2 | Badly formatted query
9.21 | Badly formatted aggregation query
9.3 | Query parameter should be an object
9.4 | Frequency not found on request
9.5 | Incorrect value for 'frequency' parameter
9.6 | Cannot launch export: more than 10 fields requested
9.7 | Cannot launch export: more than 1 multi-valued field requested
9.8 | Field does not exist
9.9 | Field not allowed to perform requested operation
9.10 | Field not allowed to perform top values operation
9.11 | Crawl Statistics Data currently not available
9.12 | Insight cannot be requested in current context
11 | The requested feature is disabled
11.1 | The comparison feature is disabled
11.2 | The Google Analytics feature is disabled
12 | The requested task failed
13 | Cannot delete a scheduled crawl which already started
14 | Method not allowed

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
1000 | Unknown error
1001 | Not Authorized
1002 | Permission denied
1004 | Analysis not found
1005 | Insight not found
1006 | URL export not found
1007 | User not found
1008 | Revision not found
1009 | Query not found
1010 | Project not found
1011 | Crawl Statistics Data currently not available
1012 | PDF Export not found
1013 | Dry run segment not found
1014 | Segment Rule not found
1015 | Bad regular expression
1016 | 'Fields' is mandatory
1017 | No result for this URL
1018 | 'Identifiers' is mandatory
1019 | Invalid area
1020 | Badly formatted request
1021 | Query not found on request
1022 | Badly formatted query
1023 | Badly formatted aggregation query
1024 | Query parameter should be an object
1025 | Frequency not found on request
1026 | Incorrect value for 'frequency' parameter
1027 | Cannot launch export: more than 10 fields requested
1028 | Cannot launch export: more than 1 multi-valued field requested
1029 | Field does not exist
1030 | Field not allowed to perform requested operation
1031 | Field not allowed to perform top values operation
1032 | Insight cannot be requested in current context
1033 | Crawl data file (S3) is missing
1034 | The requested feature is disabled
1035 | The comparison feature is disabled
1036 | The Visits feature is disabled
1037 | The requested task failed
1038 | Cannot delete a scheduled crawl which already started
1039 | Method not allowed

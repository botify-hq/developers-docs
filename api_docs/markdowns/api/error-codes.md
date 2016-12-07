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
1004 | Analysis was not found
1005 | Insight was not found
1006 | Url export was not found
1007 | User was not found
1008 | Revision was not found
1009 | Query was not found
1010 | Project was not found
1011 | Crawl Statistics Data is currently not available
1012 | Pdf Export was not found
1013 | Dry run segment not found
1014 | Segment Rule not found
1015 | Bad regular expression
1016 | Fields are mandatory
1017 | No result for this URL
1018 | Insight identifiers are mandatory
1019 | Invalid area
1020 | Badly formatted request
1021 | Query not found on request
1022 | Badly formatted queries
1023 | Badly formatted aggregation query
1024 | Query parameter should be an object
1025 | Frequency not found on request
1026 | Incorrect value for 'frequency' parameter
1027 | Cannot launch export: more than 10 fields requested
1028 | Cannot launch export: more than 1 multiple field requested
1029 | Field does not exist
1030 | Field is not allowed to perform suggest operation
1031 | Field is not allowed to perform top values operation
1032 | Can not request insight in current context
1033 | Crawl data file (S3) is missing
1034 | The requested feature is disabled
1035 | The comparison features is disabled
1036 | The Visits feature is disabled
1037 | The requested task failed
1038 | Cannot delete an already-launched planified crawl
1039 | Method not allowed
1040 | Logfile was not found
1041 | Logfile preview is not allowed
1042 | User setting was not found
1043 | The query is too big to execute it
1044 | Query can not be executed
1045 | The list of urls for dry run on segments contains invalid URLs
1046 | The Search Engines feature is disabled
1047 | Orphans not found
1048 | Search Engines Internal Error
1049 | Logfile analysis was not found
1050 | Logfile analysis id not allowed
1051 | Logfile samples was not found
1052 | A CSV export is already running
1053 | Too many requests
1054 | Log file analysis job settings not found
1055 | Out of range logfile analysis date
1056 | Too large logfile analysis date range
1057 | Badly formatted regex in query
1058 | An advanced export is already running
1059 | Advanced export was not found
1060 | The export failed

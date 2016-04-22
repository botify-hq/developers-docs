# Rate Limit

To prevent excessive usage of the Botify API and ensure its availability, we set up an API Rate Limit.

## Limits

- **100 calls by minute by operation** (endpoint) by user. For instance, getting the [[analysis summary;reference#/Analysis/getAnalysisSummary]] of 5 different analyses in the same second reaches the limit.

Once the limit is reached, the API responds with a **[429 HTTP Code](https://tools.ietf.org/html/rfc6585#section-4)** until the limit reason no longer applies.


## Need more?

If you need the limit to be raised, feel free to contact us at [support@botify.com](mailto:support@botify.com).

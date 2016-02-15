# Rate Limit

To prevent an excessive usage of the API and ensure Botify API availability, we set up an API Rate Limit.

## Limits

- **5 calls by second by operation** (endpoint) by user. For instance, getting the [[analysis summary;reference#Analysis_getAnalysisSummary]] of 5 differents analysis in the same second reaches the limit.

Once the limit is reached, the API responds with a **[429 HTTP Code](https://tools.ietf.org/html/rfc6585#section-4)** until limit reason is gone.


## Leverage

If you need the limit to be increased, feel free to contact us at [support@botify.com](mailto:support@botify.com).

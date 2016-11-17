# Rate Limit

To prevent excessive usage of the Botify API and ensure its availability, we set up an API Rate Limit.

## Limits

- **5 API calls by second**.
- **50 CSV exports by day**.

Once the limit is reached, the API responds with a **[429 HTTP Code](https://tools.ietf.org/html/rfc6585#section-4)** until the limit reason no longer applies.
**Note that** these limits are shared with the Botify Application. For instance, if you launch 50 CSV export within a day using the API, you will not be able to launch more exports either using the API or the URL Explorer in the application.


## Need more?

If you need the limit to be raised, feel free to contact us at [support@botify.com](mailto:support@botify.com).

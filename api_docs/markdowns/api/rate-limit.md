# Rate Limit

To prevent excessive usage of the Botify API and ensure its availability, we enforce the following limits.

## Limits

- **5 API calls by second**.
- **50 CSV exports by day**.
- **100k URLs max by CSV Export**

**Note that** these limits are shared with the Botify Application. For instance, if you launch 50 CSV exports within a day using the API, you will not be able to launch more exports either using the API or the URL Explorer in the application.

Once the limit is reached, the API responds with a **[429 HTTP Code](https://tools.ietf.org/html/rfc6585#section-4)** until the limit reason no longer applies.


## Need more?

If you need limits to be raised, please contact your account manager.

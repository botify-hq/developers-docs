# Authentication

To use the Botify Rest API, you need an active user account. This section describes how to authenticate via the API.

## Token Authentication
To authenticate to the Botify REST API, you need to provide a valid API Token.
The *Authorization* header must be set on every request to the API.

**Example:**
```SH
curl 'https://api.botify.com/v1/projects/${username}' \
     -H 'Authorization: Token ${API_KEY}' \
```

### Get your API Token
You can get your **API Auth Token** at [https://app.botify.com/account](https://app.botify.com/account).
If you don't see an API Auth Token section in you profile settings, you might not have access to the Botify API yet. Please contact your account manager.


### Regenerate your Token
You can regenerate your Token at [https://app.botify.com/account](https://app.botify.com/account).
Once the new token is generated, any request using the previous token is forbidden.

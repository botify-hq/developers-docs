# Authentication

To use the Botify Rest API, you need an active user account. The section below describes how to authenticate on the API.

## Token Authentication
To authenticate to the Botify REST API, you need to provide a valid API Token.
The *Authorization* header must be set on every request to the API.

Example:
```SH
curl 'https://api.botify.com/projects/${username}' \
     -H 'Authorization: Token ${API_KEY}' \
     -H 'Content-type: application/json'
```

### Get your API Token
You can get your **API Auth Token** at https://app.botify.com/account/.

### Regenerate your Token
You can regenerate your Token at https://app.botify.com/account/.
After generating a new token, the previous token is invalidated and any requests using this token are forbidden.

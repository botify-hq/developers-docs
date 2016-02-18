# Authentication

To use the Botify Rest API, you need an active user account. This section describes how to authenticate on the API.

## Token Authentication
To authenticate to the Botify REST API, you need to provide a valid API Token.
The *Authorization* header must be set on every request to the API.

**Example:**
```SH
curl 'https://api.botify.com/projects/${username}' \
     -H 'Authorization: Token ${API_KEY}' \
```

### Get your API Token
You can get your **API Auth Token** at [https://app.botify.com/account](https://app.botify.com/account).

### Regenerate your Token
You can regenerate your Token at [https://app.botify.com/account](https://app.botify.com/account).
Once the new token generated, any requests using the previous token are forbidden.


<a href="https://docs.google.com/forms/d/1T6D588024flDKHS6q_IMlVMS-q8rmRvgzBIc8EZdyDo/viewform" class="inscription-button">Request your Limited Preview of Botify Alpha API</a>

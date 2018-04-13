# Botify CMS Embed

**Botify CMS Embed** allows you to easily get Botify data for a URL inside your Content Management System.

## Pre-requisites

Initial installation must be performed by a developer with access to the CMS templates.
To setup the Botify CMS Embed, you will need the following information:

- A project on Botify, with at least one crawl (we recommend a scheduled crawl so the information displayed is as recent as possible)
- Your API Token (you can get your token in your [profile settings](https://app.botify.com/account))
- Access to your CMS's templating engine, to modify templates

## Setup

The Botify CMS embed can be displayed in one of two ways: as an inline block (inside the flow of the CMS page for the entry) or as an overlay (with Botify's data displayed on top of the CMS page for the entry).
This is configurable in the template when setting up the Botify CMS Embed for your CMS.

To setup, change the template in your CMS for a page, and add the Botify CMS Embed initializer: 

- Add a `script` tag to add the CMS Embed bundle to the context of your page:

``` <script src="https://public-js.botify.com/embed/latest/botify-embed.js"> </script>```

This will include everything that is necessary to embed Botify information into your CMS page.
It injects a global `window.BotifyEmbed` variable that allows you to control the embed on the page. 

- Add a `script` tag to start the CMS Embed bundle once the CMS Page is loaded:

```
<script>
// Wait for the DOM Content to be loaded before initializing the Botify Embed
window.addEventListener('DOMContentLoaded', function() {
    // Initialize the Botify CMS Embed for this project
    BotifyEmbed.start({
      username: 'your-username-slug',
      projectSlug: 'your-project-slug',
      token: "your-api-token",
      url: 'the-url-for-this-page', // <= Here, we give the Embed the resulting URL for this CMS page
      mode: 'OVERLAY',
    });
})
</script>
```

The `url` paramater will need to be injected according to the URL that will be produced by your CMS when editing the CMS entry page.

Parameters for the `BotifyEmbed.start` function:

- `username` - *(Required)* - Username slug of the project you would like to target
- `projectSlug` - *(Required)* - Project slug of the project you would like to target
- `token` - *(Required)* - API Token for your user
- `url` - *(Required)* - URL to target (must be crawled in your username/projectSlug project)
- `mode` - *(Optional)* - Default: 'OVERLAY' - Possible Values:
    - `'OVERLAY'` - displays the embed as an *overlay* appended to the document body
    - `'INLINE'` - displays the embed as an *inline-block* on the specified `target` DOM element
- `target` - *(Required if `mode='INLINE'`)* - Query selector to find the DOM node in which the CMS Embed should render

The exact same information is displayed, whether the CMS Embed is displayed as an overlay or as an inline block.

## Usage

Once the setup is complete, the Embed should be displayed in your CMS, either on as an overlay or as an inline block.

### Inline Embed

![image](/staticfiles/images/img_botify_cms_embed_inline.png)

### Overlay Embed

![image](/staticfiles/images/img_botify_cms_embed_overlay.png)

## Troubleshooting

Opening the console when displaying the Botify CMS Embed will give you human-readable errors to understand why the CMS Integration is not working.

For further help setting up your CMS embed, [contact our Support](mailto:support@botify.com).

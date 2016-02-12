# Botify Developers Docs
This repo contains sources to build the Botify Developers **static website** using Django Medusa.

- `botify_docs` app contains main templates, styles, statics and homepage.
- `api_docs` contains mostly markdown files that are used to generated documentation pages.


## Add / Update api documentation pages
`api_docs/markdown/index.py` describes pages path and their relative markdown file.

## Publish on dev / prod environment
@TODO


## Development

### Requirement
- python 2.7
- python-dev 2.7 (for ubuntu)
- pip (for ubuntu)

```SH
sudo apt-get install python2.7 python2.7-dev python-pip
sudo pip install virtualenvwrapper
```

### Installation
```SH
mkvirtualenv docs
pip install -r requirements.txt
```

### Run Server
```SH
./manage.py runserver
```
Open in your browser `http://127.0.0.1:8000/`.

### Build CSS
@TODO



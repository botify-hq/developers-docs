# Botify Developers Docs
[![Build Status](https://travis-ci.org/botify-hq/developers-docs.svg?branch=master)](https://travis-ci.org/botify-hq/developers-docs)

This repo contains sources to build the Botify Developers **static website** using Django Medusa.

- `botify_docs` app contains main templates, styles, statics and homepage.
- `api_docs` contains mostly markdown files that are used to generated documentation pages.


## Add / Update api documentation pages

`api_docs/markdown/index.py` describes pages path and their relative markdown file.

## Development

### Requirement
- python 2.7
- python-dev 2.7 (for ubuntu)
- pip (for ubuntu)

```SH
sudo apt-get install python2.7 python2.7-dev python-pip
sudo pip install virtualenvwrapper
```

For virtualenvwrapper on Linux, add the following to your `~/.bashrc` file

```SH
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export BOTIFY_ENVIRONMENT=local
export LC_ALL="en_US.UTF-8"
source /usr/local/bin/virtualenvwrapper.sh
```

and then `source ~/.bashrc`. For other OS read the installation guide on
http://virtualenvwrapper.readthedocs.org/en/latest/install.html#installation

### Installation
```SH
mkvirtualenv docs
workon docs
pip install -r requirements.txt
```

### Run Server
be sure to be on the virtual env `workon docs`

```SH
./script/run
```

You can define a different host and port if you need to

```SH
./script/run 0.0.0.0:8080
```

### Watch SASS
```
compass watch botify_docs/static/style
```


### Deploy locally

To generate the website:
```SH
./script/deploy_local
# => answer 'yes'
```

Then you may want to serve them through HTTP with:
```SH
python -m SimpleHTTPServer 8001
```

And then open your brower at http://localhost:8001/_site/


### Deploy Staging

You need to have AWS environment variables to be able to deploy. You can add the following two lignes in your `~/.bashrc`
```SH
export AWS_ACCESS_KEY_ID=xxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxxxx
```
Then run the deploy staging command **within a virtual env**.
```SH
./script/deploy_staging
# => answer 'yes'


### Deploy Production

You need to have AWS environment variables to be able to deploy. You can add the following two lignes in your `~/.bashrc`
```SH
export AWS_ACCESS_KEY_ID=xxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxxxx
```
Then run the deploy prod command **within a virtual env**.
```SH
./script/deploy_prod
# => answer 'yes'

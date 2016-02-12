# Botify Developers Docs
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

### Build CSS
@TODO

### Deploy locally
@TODO How to locally generate the files

### Deploy Production
@TODO How to deploy to a s3 bucket

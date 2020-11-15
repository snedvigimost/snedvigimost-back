# real-estate

[![Build Status](https://travis-ci.org/andriyor/real-estate.svg?branch=master)](https://travis-ci.org/andriyor/real-estate)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Its all about a Weissman score > 5.0. Check out the project's [documentation](http://andriyor.github.io/real-estate/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```


http://127.0.0.1:4222/swagger/

sudo service postgresql stop 

python manage.py startapp countries
python manage.py makemigrations 
python manage.py migrate
 
https://dephell.readthedocs.io/cmd-deps-convert.html

docker-compose run web bash
python manage.py loaddata db2.json

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
http://127.0.0.1:4222/admin/

sudo service postgresql stop 

python manage.py runserver 4222

python manage.py startapp countries
python manage.py makemigrations 
python manage.py migrate

https://django-modeltranslation.readthedocs.io/en/latest/commands.html#commands-update-translation-fields
python manage.py update_translation_fields 
 
https://dephell.readthedocs.io/cmd-deps-convert.html
dephell deps convert --from=pyproject.toml --to=requirements.txt

scp db.json  root@188.166.80.5:/root/snedvigimost-back
docker-compose run web bash
python manage.py loaddata db2.json

[Django : Transfer data from Sqlite to another database](https://www.shubhamdipt.com/blog/django-transfer-data-from-sqlite-to-another-database/)

```
python manage.py dumpdata > db.json
Change the database settings to new database such as of MySQL / PostgreSQL.
python manage.py migrate
python manage.py shell 
Enter the following in the shell
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
python manage.py loaddata db.json
```

from realestate.listings.models import Listing      
from django.contrib.gis.geos import Point   

kk = Listing.objects.get(pk=1)    
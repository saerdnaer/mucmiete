# Deine Miete

(c) Copyright 2015 by Thomas Tanner.

Licensed under GNU Affero General Public License 3.0. See the file LICENSE for details.

## Prerequisites

 * virtualenv
 * bower
 * A postgresql database is recommended
 * nginx as webserver is recommended

## Installation

Copy settings/preconfig.py.template to settings/preconfig.py and configure it according to your setup.

```
bower install
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
./manage.py migrate
```

with HAVE_ADMIN: 
```
./manage.py createsuperuser
```

Server for local testing:
```
./manage.py runserver
```

## Deployment

Copy the static file over to the location specified in preconfig.py:

```
./manage.py collectstatic --noinput
```

uwsgi and nginx are recommended. Be sure to turn off debug mode.

# Deine Miete

[TODO: Description of the project]

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
./manage.py create_plz_mapping
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

## Template Structure

The top-most template is `base.html`. It is extended by `standalone.html` and `embed.html`.
The templates for the non-interactive pages only extend `standalone.html`. The template for the pages used for the form do either extend `standalone.html` or `embed.html`, depending of the value of the template variable `is_embeded`.

## Embedding
To embed a page (e.g. the main form) in a different page via `<iframe>`, append `?embed` to the url. This will only affect pages related to the form.

## Copyright

(c) Copyright 2015 by Konstantin Schütze and Thomas Tanner.

Licensed under GNU Affero General Public License 3.0. See the file LICENSE for details.

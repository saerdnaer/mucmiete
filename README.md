# mucmiete
OpenData - Munich Miete 

(c) Copyright 2015 by Thomas Tanner.

Licensed under GNU Affero General Public License 3.0. See the file LICENSE for details.

## Installation

in settings/ configure preconfig.py, devel.py, production.py

```
mkvirtualenv miete
pip install -r requirements.txt
./manage.py migrate
```

with HAVE_ADMIN: 
```
./manage.py createsuperuser
```

for local testing:
```
./manage.py runserver
```

for deployment:
```
./manage collectstatic -l --noinput
```
uwsgi and nginx are recommended

# BasicApp Overview


## Architecture


**General Project Layout**
```
setup.py          --- python package install information
readme.md         --- project info and getting started docs
installer.py      --- command line script for getting the app installed
tests/            --- pytest, tests folder
docs/             --- a place to put your apps docs
basicapp/         --- this app's source code
```
<br>


**Source Code Layout**
```
basicapp/
    client/         --- the flask web app front end and routes
    controllers/    --- data model implementations
    models/         --- app data models
    scripts/        --- any cli tools for the python package
    utils/          --- common utilities and variables
```
<br>


**Flask App Layout**
```
basicapp/client/
    app.py           --- the flask app and routes
    config.py        --- flask configs
    templates/       --- html / jinja2 files
        layouts/         --- base html templates
        pages/           --- page implementations of base layouts
        includes/        --- html components used across pages and layouts
    static/          --- site static files (css, js, icons, ect...)
```
<br>
# Project Structure
While projects can be arranged in many ways, the following is a useful and versatile setup
for many different types of python projects.


## High level
This generic project structure is useful for many cases.

```
project/
    mypackage/          <-- always name this folder what you want
                            to see when you import it.

    tests/              <-- seperate tests from source-code for easier prod deploys

    docs/               <-- a useful place to put your package documentation

    readme.md           <-- PLEASE ALWAYS include this.... just please.

    install.py          <-- optional file to make complex installs easier for users

    setup.py            <-- package install info

    .gitignore          <-- dont forget this, or .pyc files will get added to git
```


# Package Structures

## MVC
the traditional model, view, controller setup is useful for app and some REST api projects.

```
mypackage/
    __init__.py
    models/
    controllers/
    views/
    scripts/
    utils/
```

## Importable API
these are projects like `numpy` that are not really meant to be called from the command line 
or run as an app. Rather these projects are intended to be imported into other packages and scripts.

```
mypackage/
    __init__.py
    core/
    models/
    utils/
    ???          <-- modules should be named by topics (i.e. database, algorithms, ect..)
```


## Flask App
used in the current `basicapp` demo application, this is a modification of the MVP model
with the exception that `client/` replaces the `views/` section. Because the data models
are intended to aid the flask web application.

```
mypackage/
    __init__.py
    core/
    models/
    utils/
    scripts/
    client/
        __init__.py
        app.py
        configs.py
        static/
        templates/
            layouts/
            pages/
            includes/
```

Inside the client folder the `static/` folder contains icons, js files, css files and other non-changing resources.
The `templates/` folder contains the html files used by flask and jinja2 to template pages and components.

    
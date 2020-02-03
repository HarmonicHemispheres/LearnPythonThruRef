# Setup Package

Python packages are the defacto way to deploy and share python projects that can be easily used in other project.


## Minimal Package Structure

```
project-folder/
    setup.py            <-- python package install details
    pkg_name/           <-- package
        __init__.py         <-- this file signals this folder as a python package
        module.py           <-- modules can exist inside a package
```

## The `setup.py` file: minimal

this script is used for installing a package into the local python package index.

```
from setuptools import setup, find_packages

setup(
    # --- metadata ---
    name='BasicApp',
    version='0.0.1',
    description='',
    url='',
    authors=['Robby Boney',],
    author_email='robbyb@gointerject.com',

    # --- the source code folders ---
    packages=['basicapp'],

    # --- project dependancies ---
    install_requires=[]
)
```

The setup file can be used with the following command while located in the project folder.

```
$ pip install -e .
```

## Console Scripts

including the `entry_points` keyword to the setup object will allow for command line scripts to
be added to the path and easily launchable.

```python
entry_points={
    'console_scripts': [
        'basicapp = basicapp.scripts.launcher:main'
    ]
}
```

The above console script will allow the `main()` function from the `basicapp.scripts.launcher` module
to be run with the command:

```
$ basicapp
```

if this is not added to the setup file scripts will need to be run the traditional way:

```
$ python basicapp/scripts/launcher.py
```

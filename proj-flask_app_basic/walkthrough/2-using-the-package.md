# Using The Package

We have already discussed calling `console_scripts` installed with the package,
but it is also possible to import resources from the package into other scripts
or within the package itself. this is an important concept.

## Prerequisites
this document assumes we have already installed a package called `pkg` by running:

```
$ pip install -e .
```

## Importing into seperate module

```python
### various ways to import our package ###

import pkg                    # EX-1: how to import
pkg.func_one()                # EX-1: how to use


import pkg as p               # EX-2: how to import
p.func_one()                  # EX-2: how to use


from pkg import func_one      # EX-3: how to import
func_one()                    # EX-3: how to use


from pkg import (             # EX-4: how to import multiple resources
    func_one, 
    func_two
    )
func_one() + func_two()       # EX-4: how to use
```


## Relative importing
packages, modules and resources can be imported relative to other files as well.

```python
from .pkg import func_one
```


## Importing from subpackages


**Subpackage and modules**
```
[DIR]   pkg/
[file]      __init__.py
[file]      module_1.py
[DIR]       subpkg/
[file]          __init__.py
[file]          module_2.py
```

the above `module_2.py` can be imported with:

```python
from pkg.subpkg.module_2 import func_two
```

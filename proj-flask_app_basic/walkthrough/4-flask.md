# Getting started with Flask

## `app.py`

the app file is ussually where flask is initialized.

```python
from .config import DevelopmentConfig
from flask import (
    Flask, 
    render_template
)


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

##### ROUTES #####
@app.route('/', methods=["GET"])
def home():
    return render_template("pages/index.html")


@app.route('/about', methods=["GET"])
def about():
    return render_template("pages/about.html")


@app.route('/login', methods=["POST"])
def login():
    return render_template("pages/login.html")

# launch application
if __name__ == '__main__':
    app.run()
```
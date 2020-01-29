from flask import (
    Flask, 
    render_template, 
    redirect, 
    url_for, 
    make_response,
    request
)
import requests
import os
import sys
import psutil
from pathlib import Path
import subprocess
import webbrowser
from .config import (
    Config, 
    ProductionConfig, 
    TestingConfig,
    DevelopmentConfig
)


def getconfig(settings):
    if settings == 'default':
        return Config
    elif settings == 'dev':
        return DevelopmentConfig
    elif settings == 'prod':
        return ProductionConfig
    elif settings == 'test':
        return TestingConfig


def create_app(settings='default'):

    app = Flask(__name__)
    settings_obj = getconfig(settings)
    app.config.from_object(settings_obj)


    ################################################
    ####              --ROUTES--                ####
    ################################################
    @app.route('/', methods=["GET"])
    def home():
        return render_template("pages/home.html")


    @app.route('/about', methods=["GET"])
    def about():
        return render_template("pages/about.html")


    @app.route('/shutdown')
    def shutdown():

        pid = os.fork()
        if pid == 0:
            return render_template('pages/shutdown.html')
        else:
            subprocess.run(['kill', f'{os.getpid()}'])


    ################################################
    ####            --LAUNCH APP--              ####
    ################################################
    app_pid = os.fork()
    if app_pid == 0:
        app.run()
    else:
        webbrowser.open(settings_obj.SERVER_NAME)

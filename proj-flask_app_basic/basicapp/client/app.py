from flask import (
    Flask, 
    render_template, 
    redirect, 
    url_for, 
    make_response,
    request,
    jsonify
)
import requests
import os
import sys
import psutil
from pathlib import Path
from multiprocessing import Process
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


def shutdown_server():
    """ utility for shutting down the builtin flask server """

    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


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


    @app.route('/shutdown', methods=["POST"])
    def shutdown():
        shutdown_server()
        return render_template("pages/shutdown.html")

    ################################################
    ####            --LAUNCH APP--              ####
    ################################################
    webbrowser.open(settings_obj.SERVER_NAME)
    app.run()

import os
from flask import Flask, render_template, Blueprint, render_template, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from jinja2 import TemplateNotFound
from blueprints.main.views import main

def create_app():
    app = Flask(__name__)
    # setup with the configuration provided by the user / environment
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    
    # setup all our dependencies
    #database.init_app(app)
    #commands.init_app(app)
    
    # register blueprint
    app.register_blueprint(main)

    return app

if __name__ == '__main__':
    create_app().run()
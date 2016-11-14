"""`main` is the top level module for your Flask application."""

# Standard imports
import os
import webapp2
import logging
import jinja2
import json
import urllib

# More imports 
from apiclient.discovery import build
import httplib2
import numpy #stat calculations 

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

#API key
API_KEY = 'AIzaSyCkyFHccAyc2c5t8Uk2AvEkWL7u6-E5J2E'

#Table ID
TABLE_ID = '1r6Pxx-CPnNXi_ggNYttpFSml6qQamkT1865Qewlk'

service = build('fusiontables', 'v1', developerKey=API_KEY)

@app.route('/')

def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

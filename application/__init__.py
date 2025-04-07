from flask import Flask
import os

app = Flask(__name__)

from application import routes

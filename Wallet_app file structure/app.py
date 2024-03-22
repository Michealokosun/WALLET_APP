
#!/usr/bin/env python

"""Contains the flask app"""


from models import *
from flask import request
#from .models import URLData, TextData, ContactData, QRCode

from flask import Flask

app = Flask(__name__)
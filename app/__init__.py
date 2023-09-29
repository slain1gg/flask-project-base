from flask import Flask

app = Flask(__name__)

USERS = [] # list for object of type User
EXPRS = [] # list for object of type Expression

from app import views
from app import models
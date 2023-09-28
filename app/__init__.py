from flask import Flask

app = Flask(__name__)

USERS = [] # lits for object of type User

from app import views
from app import models
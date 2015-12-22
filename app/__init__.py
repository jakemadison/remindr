__author__ = 'Madison'

from flask import Flask
import config
import os.path
import db_controller

# if not os.path.isfile(config.DATABASE_LOC):   # create DB if needed
#     print 'No DB present. Creating DB file '+config.DATABASE_LOC
#     open(config.DATABASE_LOC, 'a').close()
#     db_controller.create_table()

app = Flask(__name__, static_url_path='')
from app import views
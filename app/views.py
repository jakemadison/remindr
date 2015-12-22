__author__ = 'Madison'

from app import app
from flask import request, jsonify, send_file, render_template

@app.route('/')
@app.route('/index')
def index():

    print 'running view for index.'

    return render_template('index.html')


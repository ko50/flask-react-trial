from flask import render_template

from back.main import APP

@APP.route('/')
def index():
    return render_template('index.html')

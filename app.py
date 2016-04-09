# -*- coding: utf-8 -*-


import sys
import json
reload(sys)
sys.setdefaultencoding("utf-8")
from sqlite3 import dbapi2 as sqlite3
from flask import Flask,jsonify ,request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

import urllib

from datetime import datetime,timedelta
from datetime import date
from datetime import datetime



# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def main():
    pass

@app.route('/navigator', methods=[ 'GET','POST'])
def navigator():
    print request.args.get('search_term', '')

    return render_template('index.html',result="result")


if __name__ == '__main__':


    app.run(host='localhost', port=9876 , threaded=True)

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
    search_term= request.args.get('search_term', '')
    url = "https://api.github.com/search/repositories?q="+search_term+"&order=desc"        
    response = json.loads(urllib.urlopen(url).read())
    items=response["items"]
    print items[0].keys()
    print "yes"
    results=[None]*5
    for i in xrange(min(5, len(items))):
        
        results[i]={
        "search_term": search_term,
        "respository_name": items[i]["name"],
        "owner_login":items[i]["owner"]["login"],
        "created_at":items[i]["created_at"],
        "avatar_url": items[i]["owner"]["avatar_url"]
        }


    print results
    return render_template('index.html',results=results)


if __name__ == '__main__':


    app.run(host='localhost', port=9876 , threaded=True)

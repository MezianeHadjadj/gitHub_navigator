# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import sys
import json
reload(sys)
sys.setdefaultencoding("utf-8")
from sqlite3 import dbapi2 as sqlite3
from flask import Flask,jsonify ,request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

#import nltk 
#from nltk import word_tokenize
import urllib

from datetime import datetime,timedelta
from datetime import date



from datetime import datetime


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def main():
    #db.posts.remove()
    keyword="clicandcall"
    #twitter=get_old_tweets()
    #twitter.main(keyword=keyword)
    new_tweets_iogrow(keyword)
    #twitter_stats(keyword)

    
    # res= posts.find({"kind":"keyword"})
    # for keyword in res:
    #     try:
    #         twitter=get_old_tweets()
    #         twitter.main(keyword=keyword)
    #     except:
    #         print 'error searching for tweets'
    #     new_tweets_iogrow(keyword)


@app.route('/search', methods=[ 'GEt','POST'])
def search():
    #main()
    return render_template('index.html',)


if __name__ == '__main__':

    # res= posts.find({"kind":"keyword"})
    # for keyword in res:
    #     try:
    #         twitter=get_old_tweets()
    #         twitter.main(keyword=keyword)
    #     except:
    #         print 'error searching for tweets'
    #     new_tweets_iogrow()
    app.run(host='localhost', port=5000 , threaded=True)

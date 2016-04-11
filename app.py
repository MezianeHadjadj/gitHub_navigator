# -*- coding: utf-8 -*-


import sys
import json
reload(sys)
sys.setdefaultencoding("utf-8")
from flask import Flask,jsonify ,request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

import urllib




# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def get_last_commit(full_name):
    commits_url = "https://api.github.com/repos/"+full_name+"/commits"        
    commits = json.loads(urllib.urlopen(commits_url).read())
    return commits


@app.route('/navigator', methods=[ 'GET','POST'])
def navigator():
    search_term= request.args.get('search_term', '')
    #search repositories by name
    url = "https://api.github.com/search/repositories?q="+search_term+"&order=desc&per_page=5"        
    response = json.loads(urllib.urlopen(url).read())
    items=response["items"]
    results=[None]*5
    for i in xrange(len(items)):
        #get last commit
        commits= get_last_commit(items[i]["full_name"])
        #render results
        results[i]={
        "search_term": search_term,
        "respository_name": items[i]["name"],
        "owner_login":items[i]["owner"]["login"],
        "created_at":items[i]["created_at"],
        "avatar_url": items[i]["owner"]["avatar_url"],
        "sha":commits[0]["sha"],
        "commit_message": commits[0]["commit"]["message"],
        "commit_author_name": commits[0]["commit"]["author"]["name"],
        "html_url": items[i]["html_url"]
        }

    return render_template('index.html',results=results)


if __name__ == '__main__':


    app.run(host='localhost', port=9876 , threaded=True)

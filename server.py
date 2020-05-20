#!/usr/bin/env python3
from flask import Flask, request
app = Flask(__name__)
fromVar="nothing"
@app.route('/')
def index():
    return(fromVar)
#function to get something in url, and answer somesting(not json)
@app.route('/api')
def api():
    fromVar=request.args.get('from')
    return(fromVar)
if __name__ == '__main__':
    app.run(debug=True)

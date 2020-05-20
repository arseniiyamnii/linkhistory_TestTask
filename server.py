#!/usr/bin/env python3
from flask import Flask, request, jsonify
app = Flask(__name__)
fromVar="nothing"
@app.route('/')
def index():
    return("use /visited_domains")
#function to get something in url, and answer somesting(not json)
@app.route('/visited_domains')
def visited_domains():
    fromVar=request.args.get('from')
    return(jsonify(fromVar))
@app.route('/api',methods=['POST'])
def api():
    content=request.get_json()
    print(content)
    return('DONE')
if __name__ == '__main__':
    app.run(debug=True)

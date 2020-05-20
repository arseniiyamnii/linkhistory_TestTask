#!/usr/bin/env python3
from flask import Flask, request, jsonify
import Redis
import json
import time
class DBMS():
    def __init__(self):
        self.db=redis.Redis()
    #need test
    #function to sending something to REDIS
    def sendToDB(self, content):
        timeStamp=time.time() #get current time
        contentJson=json.dumps(content)
        db.set('item', contentJson)
    #need test
    #function to search and return something from REDIS
    def searchAndReturnFromDB(self, timeFrom, timeTo):
        pattern="["+str(timeFrom)+"-"+str(timeTo)+"]:*"
        return(self.db.keys(pattern))
db=redis.Redis() #initialise Redis
app = Flask(__name__) #initialise Flask
#need test
@app.route('/')
def index():
    return("use /visited_domains")
#need test
#function to get something in url, and answer somesting in json
@app.route('/visited_domains')
def visited_domains():
    fromVar=request.args.get('from')
    return(jsonify(fromVar))
#need test
#function to get something in json
@app.route('/visited_links',methods=['POST'])
def visited_links():
    content=request.get_json()
    print(content)
    return('DONE')
if __name__ == '__main__':
    app.run(debug=True)

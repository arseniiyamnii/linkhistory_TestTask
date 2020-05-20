#!/usr/bin/env python3
from flask import Flask, request, jsonify
import redis
import json
import time
import bisect
class DBMS():
    def __init__(self):
        self.db=redis.StrictRedis('localhost',6379,charset="utf-8", decode_responses=True)
        self.indexingKeys=[]
    #need test
    #function to sending something to REDIS
    def sendToDB(self, content):
        timeStamp=int(time.time()) #get current time
        contentJson=json.dumps(content)
        self.db.set(timeStamp, contentJson)
    #need test
    #function to search and return something from REDIS
    def searchAndReturnFromDB(self, timeFrom, timeTo):
        print(timeFrom," ",timeTo)
        indexingKeys=self.db.keys("*")
        indexingKeys=list(map(int,indexingKeys))
        indexingKeys.sort()
        #for i in indexingKeys:
        #    i=i.decode('utf-8')
        print(indexingKeys)
        from_bound=bisect.bisect_left(indexingKeys, int(timeFrom))
        to_bound=bisect.bisect_right(indexingKeys, int(timeTo))
        print("indexing ready")
        allNeededKeys=indexingKeys[from_bound:to_bound]
        print(allNeededKeys)
        allValues=[]
        for oneKey in allNeededKeys:
            allValues.append(self.db.get(str(oneKey)))
        print(allValues)

db=DBMS() #initialise Redis
app = Flask(__name__) #initialise Flask
#need test
@app.route('/')
def index():
    return("use /visited_domains and /visited_links")
#need test
#function to get something in url, and answer somesting in json
@app.route('/visited_domains')
def visited_domains():
    global db
    #fromVar=request.args.get()
    fromVar=request.args.get('from')
    toVar=request.args.get('to')
    #toVar=request.args.get('to', type=int)
    dbAnswer=db.searchAndReturnFromDB(fromVar,toVar)
    print(dbAnswer)
    return(jsonify(dbAnswer))
#need test
#function to get something in json
@app.route('/visited_links',methods=['POST'])
def visited_links():
    global db
    content=request.get_json()
    db.sendToDB(content)
    return('DONE')
if __name__ == '__main__':
    app.run(debug=True)

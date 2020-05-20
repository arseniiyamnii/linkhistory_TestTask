#!/usr/bin/env python3
from flask import Flask, request, jsonify
import redis
import json
import time
import bisect
from urllib.parse import urlparse
class DBMS():
    def __init__(self):
        self.db=redis.StrictRedis('localhost',6379,charset="utf-8", decode_responses=True)
        self.indexingKeys=[]
    #need test
    #function to sending something to REDIS
    def sendToDB(self, content):
        print(content[0])
        timeStamp=int(time.time()) #get current time
        for i in content:
            self.db.lpush(timeStamp,i)
        #contentJson=json.dumps(content)
        #self.db.set(timeStamp, contentJson)
    #need test
    #function to search and return something from REDIS
    def searchAndReturnFromDB(self, timeFrom, timeTo):
        try:
            status="OK"
            print(timeFrom," ",timeTo)
            indexingKeys=self.db.keys("*")
            indexingKeys=list(map(int,indexingKeys))
            indexingKeys.sort()
            print(indexingKeys)
            from_bound=bisect.bisect_left(indexingKeys, int(timeFrom))
            to_bound=bisect.bisect_right(indexingKeys, int(timeTo))
            print("indexing ready")
            allNeededKeys=indexingKeys[from_bound:to_bound]
            print("all needed keys is: ",allNeededKeys)
            allValues=[]
            for oneKey in allNeededKeys:
                for i in range(0,self.db.llen(str(oneKey))):
                    allValues.append(self.db.lindex(str(oneKey),i))
        except redis.exceptions.RedisError as e:
            status=e
        for i in range(len(allValues)):
            url = urlparse(allValues[i])
            if url.netloc != "":
                allValues[i]=url.netloc
            if allValues[i][:7]=="http://" or allValues[i][:8]=="https://":
                print("delete")
                allValues[i].replace(url.scheme,'')
        allValues=list(dict.fromkeys(allValues))
        answerDict={"domains":allValues,"status":status}
        return(answerDict)

            #allValues.append(self.db.get(str(oneKey)))
            #print(self.db.get(str(oneKey)))
        

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
    db.sendToDB(content['links'])
    #print(content['links'])
    return('DONE')
if __name__ == '__main__':
    app.run(debug=True)

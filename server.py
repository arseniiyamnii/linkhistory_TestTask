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

    def getAllKeys(self):
        indexingKeys=self.db.keys("*")
        indexingKeys=list(map(int,indexingKeys))
        indexingKeys.sort()
        return indexingKeys
    def findNeededKeys(self,indexingKeys,fromVar,toVar):
        from_bound=bisect.bisect_left(indexingKeys, int(fromVar))
        to_bound=bisect.bisect_right(indexingKeys, int(toVar))
        allNeededKeys=indexingKeys[from_bound:to_bound]
        return allNeededKeys
    def domainParser(self,urls):
        for i in range(len(urls)):
            url = urlparse(urls[i])
            if url.netloc != "":
                urls[i]=url.netloc
            if urls[i][:7]=="http://" or urls[i][:8]=="https://":
                urls[i].replace(url.scheme,'')
        return(urls)
    #need test
    #function to sending something to REDIS
    def sendToDB(self, content):
        timeStamp=int(time.time()) #get current time
        for i in content:
            self.db.lpush(timeStamp,i)

    #need test
    #function to search and return something from REDIS
    def searchAndReturnFromDB(self, timeFrom, timeTo):
        try:
            status="OK"
            indexingKeys=self.getAllKeys()
            allNeededKeys=self.findNeededKeys(indexingKeys,timeFrom,timeTo)
            allValues=[]
            for oneKey in allNeededKeys:
                for i in range(0,self.db.llen(str(oneKey))):
                    allValues.append(self.db.lindex(str(oneKey),i))
        except redis.exceptions.RedisError as e:
            status=e
        allValues=self.domainParser(allValues)
        allValues=list(dict.fromkeys(allValues))
        answerDict={"domains":allValues,"status":status}
        return(answerDict)

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
    fromVar=request.args.get('from')
    toVar=request.args.get('to')
    dbAnswer=db.searchAndReturnFromDB(fromVar,toVar)
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

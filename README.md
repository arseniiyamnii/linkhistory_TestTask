# linksserver  
## Requirements  

python3 `sudo apt install python3`  
redis
```
curl -s -0 redis-stable.tar.gz "http://download.redis.io/redis-stable.tar.gz"
sudo mkdir -p /usr/local/lib
sudo chmod a+w /usr/local/lib/
sudo tar -C /usr/local/lib/ -xzf redis-stable.tar.gz
rm redis-stable.tar.gz
cd /usr/local/lib/redis-stable/
sudo make
sudo make install
sudo mkdir -p /etc/redis/
sudo touch /etc/redis/6379.conf
```  
then insert this:
'''
'''
into `/etc/redis/6379.conf`
run redis `redis-server /etc/redis/6379.conf`

python packages:  
flask `pip3 install flask`
redis `pip3 install redis-py`

## Parameters:
Redis run at `localhost:6357`
Flask run at `localhost:5000`
## How to use:
walk to project dirrectory
run server with:
`./server.py` or `python3 server.py`
or tests with:
`./tests.py` or `python3 tests.py`
when your server alredy run, you can check it in your browser, with:
`http://localhost:5000/`
You see small tip about using this server
### Sending links to server:
use POST request to sending links
Exemple with CURL:
`curl --header "Content-Type: application/json" --request POST --data '{"links":["http://ya.ru","funbox.ru","http://google.com","https://sososo.ru/somasoma"]}' localhost:5000/visited_links`
we send few links in json with POST method
### Get links from date range:
Example with CURL:
`curl 'localhost:5000/visited_domains?from=1590010422&to=1599999999'`
date range using in UNIX format. Only first 10 digits

##Why i need that?
Example. You can create small extencion for Browser, to gram all visited url, and store them in yur server. For examle for child control.

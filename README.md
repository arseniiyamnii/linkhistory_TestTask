# linksserver  
## Зависимости и как их установить  

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
Далее вставьте это:  
'''
# /etc/redis/6379.conf
 
port              6379
daemonize         yes
save              60 1
bind              127.0.0.1
tcp-keepalive     300
dbfilename        dump.rdb
dir               ./
rdbcompression    yes
'''  
в `/etc/redis/6379.conf`  
Запускаем redis `redis-server /etc/redis/6379.conf`  

python3 модули:  
flask `pip3 install flask`  
redis `pip3 install redis-py`  

## Параметры сервера:
Redis запускается на `localhost:6357`  
Flask запускается на `localhost:5000`  
Redis использует базу данных по умолчанию `0`  
## Как это использовать:
Переходим в дирректорию проекта  
Запускаем сервер:  
`./server.py` или `python3 server.py`  
или тестируем его с поомощью:  
`./tests.py` или `python3 tests.py`  
!!!Внимание!!! Redis должен быть запущен !!!  
Когда ваш сервер запущен, вы можете проверить его в браузере:  
`http://localhost:5000/`
Вы увидите маленькую подсказку по работе сервера  
### Отправка ссылок на сервер:
Используйте POST запрос для отправки ссылок  
Пример запроса через CURL:  
`curl --header "Content-Type: application/json" --request POST --data '{"links":["http://ya.ru","funbox.ru","http://google.com","https://sososo.ru/somasoma"]}' localhost:5000/visited_links`  
Готово! Мы отправили ссылки на сервер!  
### Взять ссылки с сервера за определенный период:
Пример с помощью CURL:  
`curl 'localhost:5000/visited_domains?from=1590010422&to=1599999999'`  
Дата исползуется в UNIX формате. Используются только первые 10 знаков  

##Зачем мне все это?
Например вы можете создать маленкое расширение для браузера, для сохранения всех посещенных ссылок. С помощью него вы можете мониторить что посещает ваш ребенок

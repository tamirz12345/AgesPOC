# AgesPOC
Learning to use:
	rebbitmq and its python lib pika
	mongodb and its python libray pymongo
	flask for http server in python


Supported API requests in http (currently listen on localhost:5000/)

	1. Get http://adress:port/info?username={username}
	   returns a string the age of the user {age} with the age from the db if the user exist.
	2. Get http://adress:port/insert?username={username}&age={age}


AgesMongo -> Class to acess the ages collection in current mongo server runs on my pc
Sender -> sends usrename and age to rabbit mq i created on my local pc stroing dicts of {username: str username,age: int age}
reciver -> reads the quete and send insert to the App.py
# AgesPOC
Learning to use:
<ul>
	<li> rebbitmq and its python lib pika</li>
	<li> mongodb and its python libray pymongo</li>
	<li> flask for http server in python</li>
</ul><br><br>

Supported API requests in http (currently listen on <strong>localhost:5000 </strong>)

	1. Get http://adress:port/info?username={username}
	   returns a string the age of the user {age} with the age from the db if the user exist.
	2. Get http://adress:port/insert?username={username}&age={age}


AgesMongo -> Class to acess the ages collection in current mongo server runs on my pc<br>
Sender -> sends usrename and age to rabbit mq i created on my local pc stroing dicts of : <br><tr><strong> {username: str username,age: int age}</strong><br>
reciver -> reads the queue and send insert api request with dicts of username and age to the App.py

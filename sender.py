import pika
import sys
import json
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
age_dict = json.dumps({"username":sys.argv[1],"age":sys.argv[2]})
channel.basic_publish(exchange='', routing_key='hello', body=age_dict)
connection.close()
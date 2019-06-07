import pika
import json
import urllib
import urllib2


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    age_dict = json.loads(body)
    params = urllib.urlencode(age_dict)
    urllib2.urlopen('http://localhost:5000/insert?' + params)

channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
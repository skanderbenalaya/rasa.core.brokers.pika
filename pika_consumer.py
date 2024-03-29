import pika
import sys
import os
import json
import pymongo
from datetime import datetime


mongo = pymongo.MongoClient("mongodb://localhost:27017/logs")
userchat = mongo.logs.userinput
botchat = mongo.logs.botresponse


def main():
    # credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # channel.queue_declare(queue='rasa_events')

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(json.dumps(message, indent=8))
        if (message['event'] == 'user'):
            print(datetime.fromtimestamp(message['timestamp']).strftime("%m/%d/%Y, %H:%M:%S"))
            message["datetime"]=datetime.fromtimestamp(message['timestamp'])
            userchat.insert_one(message)
        if (message['event'] == 'bot'):
            message["datetime"]=datetime.fromtimestamp(message['timestamp'])
            botchat.insert_one(message)
        # print('Received event only {}'.format(message["event"]))

    channel.basic_consume(queue='rasa_queue',
                          on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

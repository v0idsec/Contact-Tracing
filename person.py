import pika
import json
import random
import time
import sys

#get person ID and speed from command line
person_id = sys.argv[1]
speed = float(sys.argv[2])

#init RabbitMQ Connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='position')

#initial position
x, y = random.randint(0, 9), random.randint(0, 9)

def move():
    global x, y
    x = max(0, min(9, x + random.choice([-1, 0, 1])))
    y = max(0, min(9, x + random.choice([-1, 0, 1])))
    data = json.dumps({'id': person_id, 'x': x, 'y': y})
    channel.basic_publish(exchange='', routing_key='position', body=data)

while True:
    move()
    time.sleep(speed)
    
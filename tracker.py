import pika
import json
from collections import defaultdict

#init RabbitMQ server connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Declare queues
channel.queue_declare(queue='position')
channel.queue_declare(queue='query')
channel.queue_declare(queue='query-response')

#track positions and contacts
positions = {}
contacts = defaultdict(list)

def update_position(ch, method, properties, body):
    data = json.loads(body)
    person_id, x, y = data['id'], data['x'], data['y']
    print(f"Received update: {person_id} at position ({x}, {y})")  # Debugging line

    if (x, y) in positions:
        for other in positions [(x, y)]:
            contacts[person_id].append(other)
            contacts[other].append(person_id)

    positions[(x, y)] = positions.get((x, y), []) + [person_id]

def handle_query(ch, method,properties, body):
    person_id = body.decode()
    response = json.dumps(contacts.get(person_id, []))
    channel.basic_publish(exchange='', routing_key='query response', body=response)

channel.basic_consume(queue='position', on_message_callback=update_position, auto_ack=True)
channel.basic_consume(queue='query', on_message_callback=update_position, auto_ack=True)

print("tracker is running...")
channel.start_consuming()
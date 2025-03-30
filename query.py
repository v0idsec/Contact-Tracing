import pika
import sys

def query_contact(person_id):
    connection =  pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='query')
    channel.queue_declare(queue='query-response')

    channel.basic_publish(exchange='', routing_key='query', body=person_id)

    def callback(ch, method, properties, body):
        print(f"Contacts for {person_id}: {body.decode()}")
        connection.close()

    channel.basic_consume(queue='query-response', on_message_callback=callback, auto_ack=True )
    channel.start_consuming()

query_contact(sys.argv[1])

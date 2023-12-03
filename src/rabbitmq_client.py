"""
    Create a RabbitMQ interface to send/receive messages.
    The messsages can be consumed by a Masstransit handler.
"""
import uuid
import pika
import json
import os

class RabbitMQSettings:
    """RabbitMQSettings contains the settings to connect to RabbitMQ."""


    def __init__(self) -> None:
        """RabbitMQSettings constructor."""

        self._connection_name = os.getenv("RABBITMQ_CONNECTION_NAME")
        self._host = os.getenv("RABBITMQ_HOST")
        self._username = os.getenv("RABBITMQ_USERNAME")
        self._password = os.getenv("RABBITMQ_PASSWORD")
        self._vhost = os.getenv("RABBITMQ_USERNAME")

    def get_host(self):
        return self._host
    
    def get_username(self):
        return self._username
    
    def get_password(self):
        return self._password
    
    def get_vhost(self):
        return self._vhost
    
    def get_connection_name(self):
        if (self._connection_name is None):
            return self.__class__.__name__
        else:
            return self._connection_name
    
    def get_connection_string(self):
        return f"amqps://{self._username}:{self._password}@{self._host}/{self._vhost}"
    

class RabbitMQSender:
    """RabbitMQSender allows to send messages to RabbitMQ."""

    def __init__(self, namespace: str, message_name: str):
        """ RabbitMQSender constructor.

            It will receive the RabbitMQ url from the environment variable AMQP_URL and create a connection to RabbitMQ.
        """

        self._settings = RabbitMQSettings()
        self._connection_name = os.getenv("RABBITMQ_CONNECTION_NAME")

        # get the class name
        class_name = self.__class__.__name__

        self._connection = None
        self._channel = None
        self._exchange = f"{namespace}:{message_name}"
        self.__connect()

    def __connect(self):
        """
            Create a connection to RabbitMQ.
        """


        params = pika.URLParameters(self._settings.get_connection_string())
        params.client_properties = {
            'connection_name': self._connection_name,
            'socket_timeout': 5
        }

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()


    def send_message(self, message):
        """Send a message to RabbitMQ that will be consumed by a Masstransit handlers."""

        # Serializing json
        json_data = self.build_message(message)

        self._channel.basic_publish(
            exchange=self._exchange, 
            routing_key='', 
            body=json_data)


    def build_message(self, message) -> str:
        """Format the message to be sent to RabbitMQ in json format."""

        message_type = f"urn:message:{self._exchange}"
        rabbitmq_address = f"amqps://{self._settings.get_host()}"

        json_message = {
            'messageId': str(uuid.uuid1()),
            'messageType': [
                message_type
            ],
            'message':  message,
            'sourceAddress': rabbitmq_address,
        }

        # Serializing json
        json_data = json.dumps(json_message)
        return json_data
    
    def close_connection(self):
        """Stop consuming messages from RabbitMQ."""

        if self._connection:
            self._connection.close()    


class RabbitMQConsumer:
    """RabbitMQConsumer allows to consume messages coming from RabbitMQ."""

    def __init__(self, queue: str):
        """RabbitMQSender constuctor.
        It will receive the RabbitMQ url from the environment variable AMQP_URL and create a connection to RabbitMQ."""

        self._settings = RabbitMQSettings()        
        self._queue = queue
        self._connection = None
        self._channel = None

        self._connect()


    def _connect(self):
        """Create a connection to RabbitMQ."""

        # get the class name
        class_name = self.__class__.__name__

        params = pika.URLParameters(self._settings.get_connection_string())
        params.client_properties = {
            'connection_name': class_name,
            'socket_timeout': 5
        }

        self._connection = pika.BlockingConnection(params)
        self._channel = self._connection.channel()
        
        self._channel.queue_declare(queue=self._queue)
        self._channel.queue_bind(
            queue=self._queue,
            exchange='llm.message.complete',
            routing_key='*')


    def start_consuming(self):
        """Start consuming messages from RabbitMQ"""

        if not self._connection or not self._channel:
            self._connect()

        self._channel.basic_consume(
            queue=self._queue, on_message_callback=self._callback, auto_ack=True)
        
        print(' [*] Waiting for messages.\n To exit press CTRL+C')
        self._channel.start_consuming()


    def stop_consuming(self):
        """Stop consuming messages from RabbitMQ"""

        if self._connection:
            self._connection.close()


    def _callback(self, ch, method, properties, body):
        """Callback function for the consumer"""

        print(f" [x] Received {body}")

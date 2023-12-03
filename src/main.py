"""The main file to run the program"""
import os
import threading
#from fiscanner_integration import FiscannerIntegration
from rabbitmq_client import RabbitMQConsumer, RabbitMQSender
import logging
from time import sleep
import sys


def setup_logger(name='rabbitmq_client', log_file='app.log', level=logging.INFO):
    """To setup as many loggers as you want."""

    # add logging to file
    logging.basicConfig(filename=log_file, filemode='a', format='%(asctime)s %(levelname)-8s %(message)s', level=level)

    # add logging to console
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(message)s'))
    console.setLevel(level)

    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    # logging.getLogger('').addHandler(logging.FileHandler(log_file))


def start_consuming():
    logging.info("Setup RabbitMQ telegram.bot.suggestion.requested received!")
    rabbitmq_consumer = RabbitMQConsumer(
        queue='telegram.bot.suggestion.requested')
        
    rabbitmq_consumer.start_consuming()
    rabbitmq_consumer.close_connection()


def main():
    setup_logger()

    logging.info('*************************************')
    logging.info('RabbitMQ Client Warm up!')
    logging.info('*************************************')

    # read configuration from environment file
    dotenv_path = os.path.join(os.path.dirname(__file__), '..\\cloud.env')
    if os.path.exists(dotenv_path):
        logging.info('Reading configuration from environment file')
        from dotenv import load_dotenv
        load_dotenv(dotenv_path)


    """ Setup RabbitMQ sender """
    rabbitmq_sender = RabbitMQSender(
                                    namespace='<<insert your message namespace here>>',
                                    message_name='<<insert your message type here>>')



    # Fiscanner integration
    # fiscanner_integration = FiscannerIntegration()
    # fiscanner_integration.run("Can you tell me the best campaign for whom love animals?")

#    print("Setup RabbitMQ receiver!")
#    rabbitmq_consumer = RabbitMQConsumer(queue='llm-completed-auto')
#    rabbitmq_consumer.start_consuming()
#    rabbitmq_consumer.close_connection()

    # create a thread to handle RabbitMQ consumer
#    rabbitmq_consumer_thread = threading.Thread(target=start_consuming, daemon=True)
#    rabbitmq_consumer_thread.start()

    # Wait until CRTL+C is pressed
    try:
        while True:

            json_message = {
                "user_id": "12313",
                "order_id": "AAAAAAAAAAAAAAA",
                "amount": 0.01,
                "currency": "EUR"
            }

            rabbitmq_sender.send_message(json_message)
            logging.info(f'Message sent!')
            sleep(2)
            pass
    except KeyboardInterrupt:
        # check that CTRL+C is pressed

        rabbitmq_sender.close_connection()
        print("Exit")
        exit(0)


if __name__ == "__main__":
    main()

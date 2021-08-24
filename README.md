# rasa.core.brokers.pika

## Requirements

   - [Python](https://www.python.org/) (v3.8+)
   - [MongoDB](https://mongodb.com/) (v4.4.4+)
   - [Rabbitmq](https://www.rabbitmq.com/download.html) (v3.8.17+)
   - [Rasa](https://rasa.com/docs/rasa/installation/) (v2.3.4)
    
       
   ### Python dependencies

   Pika : `pip install pika`
   Pymongo : `pip install pymongo`
   
    
   Enable Rabbitmq management interface : `rabbitmq-plugins enable rabbitmq_management`
   
   You can then access it through : `http://localhost:15672/`
   
   Edit the endpoints.yml with the one in this repository

   Launch Rabbitmq server
   
   Run `rasa shell -- debug`
   
   Run the python pika_consumer.py script
   
   Interact with rasa shell and check for the logging in mongodb collection "logs"
   
   Leave the rasa shell idle for 10mins and try again to check if the channel is still open for the broker.pika.
   

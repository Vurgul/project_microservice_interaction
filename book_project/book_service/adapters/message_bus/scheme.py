from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue, Connection

broker_scheme = BrokerScheme(
    Queue('ProjectQueue', Exchange('our_exchange'), routing_key='project_queue'),
)

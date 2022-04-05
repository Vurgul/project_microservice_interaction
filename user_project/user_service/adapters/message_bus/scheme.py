from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue, Connection

broker_scheme = BrokerScheme(
    Queue('UsersQueue', Exchange('users_exchange'), routing_key='users_queue'),
)

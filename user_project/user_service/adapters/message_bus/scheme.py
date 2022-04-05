from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue, Connection

broker_scheme = BrokerScheme(
    Queue('UsersOutputQueue', Exchange('users_exchange'), routing_key='users_output'),
    Queue('UsersInputQueue', Exchange('users_exchange'), routing_key='users_input'),
)

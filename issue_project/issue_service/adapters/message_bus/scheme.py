from classic.messaging_kombu import BrokerScheme
from kombu import Exchange, Queue, Connection

broker_scheme = BrokerScheme(
    Queue('IssueQueue', Exchange('issues_exchange'), routing_key='issues_queue'),
)

from classic.messaging_kombu import KombuConsumer
from issue_service.application import services
from kombu import Connection

from .scheme import broker_scheme


def create_consumer(
    connection: Connection, issues: services.IssueService
) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        issues.take_message,
        'ProjectQueue',
    )

    return consumer

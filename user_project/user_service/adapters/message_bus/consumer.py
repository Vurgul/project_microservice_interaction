"""from kombu import Connection

from classic.messaging_kombu import KombuConsumer

from user_service.application import services

from .scheme import broker_scheme


def create_consumer(
    connection: Connection, users: services.UserService
) -> KombuConsumer:

    consumer = KombuConsumer(connection=connection, scheme=broker_scheme)

    consumer.register_function(
        users.create_user,
        'ProjectQueue',
    )

    return consumer"""

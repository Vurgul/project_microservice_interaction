from classic.messaging_kombu import KombuPublisher
from classic.sql_storage import TransactionContext
from kombu import Connection
from sqlalchemy import create_engine
from user_service.adapters import database, message_bus, user_api
from user_service.application import services


class Settings:
    db = database.Settings()
    user_api = user_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL)  # , echo=True
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
        messages_params={
            'our_exchange': {
                'exchange': 'our_exchange',
                'routing_key': 'project_queue',
            }
        }
    )


class Application:
    users = services.UserService(
        user_repo=DB.users_repo,
        publisher=MessageBus.publisher,
    )


class Aspects:
    services.join_points.join(DB.context)
    user_api.join_points.join(MessageBus.publisher, DB.context)


app = user_api.create_app(
    users=Application.users
)


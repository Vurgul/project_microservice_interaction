from classic.sql_storage import TransactionContext
from user_service.adapters import user_api, database, message_bus
from user_service.application import services
from sqlalchemy import create_engine

from kombu import Connection
from classic.messaging_kombu import KombuPublisher


class Settings:
    db = database.Settings()
    user_api = user_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)  # , echo=True
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    users_repo = database.repositories.UsersRepo(context=context)


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    message_bus.broker_scheme.declare(connection)

    publisher = KombuPublisher(
        connection=connection,
        scheme=message_bus.broker_scheme,
    )


class Application:
    users = services.UserService(
        user_repo=DB.users_repo,
        publisher=MessageBus.publisher,
    )


class Aspects:
    services.join_points.join(DB.context)
    #user_api.join_points.join(DB.context)
    user_api.join_points.join(MessageBus.publisher, DB.context)


app = user_api.create_app(
    users=Application.users
)

#if __name__ == '__main__':
#    from wsgiref import simple_server
#    with simple_server.make_server('localhost', 8000, app=app) as server:
#        print(f'Server running on http://localhost:{server.server_port} ...')
#        server.serve_forever()

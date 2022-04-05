from classic.sql_storage import TransactionContext
from book_service.adapters import book_api, database, message_bus
from book_service.application import services
from sqlalchemy import create_engine

from kombu import Connection
from classic.messaging_kombu import KombuPublisher


class Settings:
    db = database.Settings()
    chat_api = book_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)  # , echo=True
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    books_repo = database.repositories.BooksRepo(context=context)


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
    books = services.BookService(
        book_repo=DB.books_repo,
        publisher=MessageBus.publisher,
    )


class Aspects:
    services.join_points.join(DB.context)
    #book_api.join_points.join(DB.context)
    book_api.join_points.join(MessageBus.publisher, DB.context)


app = book_api.create_app(
    books=Application.books
)

#if __name__ == '__main__':
#    from wsgiref import simple_server
#    with simple_server.make_server('localhost', 8000, app=app) as server:
#        print(f'Server running on http://localhost:{server.server_port} ...')
#        server.serve_forever()

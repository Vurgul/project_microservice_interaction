from classic.sql_storage import TransactionContext
from issue_service.adapters import issue_api, database, message_bus
from issue_service.application import services
from sqlalchemy import create_engine

from kombu import Connection
from classic.messaging_kombu import KombuPublisher


class Settings:
    db = database.Settings()
    issue_api = issue_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)  # , echo=True
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.IssuesRepo(context=context)


class Application:
    issues = services.IssueService(
        issue_repo=DB.issues_repo,
        #publisher=MessageBus.publisher,
    )


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)

    consumer = message_bus.create_consumer(connection, Application.issues)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)

#    message_bus.broker_scheme.declare(connection)
#    publisher = KombuPublisher(
#        connection=connection,
#        scheme=message_bus.broker_scheme,
#    )


class Aspects:
    services.join_points.join(DB.context)
    issue_api.join_points.join(DB.context)
    #issue_api.join_points.join(MessageBus.publisher, DB.context)


#if __name__ == '__main__':
#    MessageBus.declare_scheme()
#    MessageBus.consumer.run()


#MessageBus.declare_scheme()
#MessageBus.consumer.run()

app = issue_api.create_app(
    issues=Application.issues
)

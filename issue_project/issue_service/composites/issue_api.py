from threading import Thread

from classic.sql_storage import TransactionContext
from issue_service.adapters import database, issue_api, message_bus
from issue_service.application import services
from kombu import Connection
from sqlalchemy import create_engine


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
    )


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)

    consumer = message_bus.create_consumer(connection, Application.issues)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    issue_api.join_points.join(DB.context)


MessageBus.declare_scheme()
consumer = Thread(target=MessageBus.consumer.run, daemon=True)
consumer.start()


app = issue_api.create_app(
    issues=Application.issues
)

from classic.sql_storage import TransactionContext
from issue_service.adapters import issue_api, database
from issue_service.application import services
from sqlalchemy import create_engine


class Settings:
    db = database.Settings()
    chat_api = issue_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)  # , echo=True
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)

    issues_repo = database.repositories.issuesRepo(context=context)


class Application:
    issues = services.IssueService(
        issue_repo=DB.issues_repo,
    )


class Aspects:
    services.join_points.join(DB.context)
    issue_api.join_points.join(DB.context)


app = issue_api.create_app(
    issues=Application.issues
)

#if __name__ == '__main__':
#    from wsgiref import simple_server
#    with simple_server.make_server('localhost', 8000, app=app) as server:
#        print(f'Server running on http://localhost:{server.server_port} ...')
#        server.serve_forever()

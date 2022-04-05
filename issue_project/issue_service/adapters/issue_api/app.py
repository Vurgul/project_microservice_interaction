from classic.http_api import App
from classic.http_auth import Authenticator
from issue_service.application import services

from . import controllers


def create_app(issues: services.IssueService) -> App:
    app = App()
    app.register(controllers.Issues(issues=issues))

    return app

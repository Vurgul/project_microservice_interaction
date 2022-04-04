from classic.http_api import App
from classic.http_auth import Authenticator
from user_service.application import services

from . import controllers


def create_app(users: services.UserService) -> App:
    app = App()
    app.register(controllers.Users(users=users))

    return app

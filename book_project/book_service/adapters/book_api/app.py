from classic.http_api import App
from classic.http_auth import Authenticator
from book_service.application import services

from . import controllers


def create_app(books: services.BookService) -> App:
    app = App()
    app.register(controllers.Books(books=books))

    return app

from book_service.application import services
from classic.http_api import App

from . import controllers


def create_app(books: services.BookService) -> App:
    app = App()
    app.register(controllers.Books(books=books))

    return app

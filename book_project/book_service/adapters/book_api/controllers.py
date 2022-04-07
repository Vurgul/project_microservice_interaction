from attr import asdict
from book_service.application import services
from classic.components import component

from .join_points import join_point


@component
class Books:
    books: services.BookService

    @join_point
    def on_get_book_info(self, request, response):
        """Получить информацию о книге"""
        book = self.books.get_book_info(
            **request.params
        )
        response.media = asdict(book)

    @join_point
    def on_get_books(self, request, response):
        """Получить информацию о всех книгах"""
        books = self.books.get_books_info()
        response.media = [asdict(book) for book in books]


    @join_point
    def on_post_add_book(self, request, response):
        """Добавить книгу"""
        book = self.books.create_book(
            **request.media
        )

        response.media = {
            'book_id': book.id
        }

    @join_point
    def on_post_edit_book(self, request, response):
        """Изменение данных книги"""
        book = self.books.update_book_info(
            **request.media
        )
        response.media = asdict(book)

    @join_point
    def on_post_delete_book(self, request, response):
        """ Удалить книгу"""
        self.books.delete_book(
            **request.media
        )

    @join_point
    def on_post_take(self, request, response):
        """ Взять книгу"""
        self.books.take_book(
            **request.media
        )

    @join_point
    def on_post_return(self, request, response):
        """ Вернуть книгу"""
        self.books.return_book(
            **request.media
        )

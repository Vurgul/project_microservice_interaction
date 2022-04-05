from classic.app.errors import AppError


class NoBook(AppError):
    msg_template = 'No book with id {id}'
    code = 'book.no_book'


class BookBusy(AppError):
    msg_template = 'Book with id {id} busy'
    code = 'book.book_busy'


class BookNotBusy(AppError):
    msg_template = 'Book with id {id} not busy, cant return'
    code = 'book.book_not_busy'

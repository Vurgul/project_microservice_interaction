import pytest
from book_service.application import errors
from book_service.application.services import BookService
from unittest.mock import Mock

data_book = {
    'id': 3,
    'title': 'test_title_3',
    'author': 'test_author_1',
    'status': True
}

data_book_update = {
    'book_id': 1,
    'title': 'NewTitle',
}


@pytest.fixture(scope='function')
def service(book_repo):
    return BookService(book_repo=book_repo, publisher=None)


def test_get_book_info(service, book_repo, book_1):
    book = service.get_book_info(book_id=book_1.id)
    assert book == book_1


def test_get_books_info(service, book_1, book_2):
    books = service.get_books_info()
    assert book_1 in books
    assert book_2 in books
    assert len(books) == 2


def test_create_book(service):
    service.create_book(**data_book)
    service.book_repo.add.assert_called_once()


def test_update_book_info(service, book_1):
    service.update_book_info(**data_book_update)
    assert book_1.title == 'NewTitle'
    assert book_1.author == 'test_author_1'


def test_delete_book(service, book_1):
    service.delete_book(book_id=book_1.id)
    service.book_repo.remove.assert_called_once()


def test_take_book(service, book_1):
    service.take_book(book_id=book_1.id, taker_id=1)
    assert book_1.status is False


def test_return_book(service, book_2):
    service.book_repo.get_by_id = Mock(return_value=book_2)
    service.return_book(book_id=book_2.id, returner_id=1)
    assert book_2.status is True


def test_no_book_in_database(service, book_1):
    service.book_repo.get_by_id = Mock(return_value=None)
    with pytest.raises(errors.NoBook):
        service.get_book_info(book_id=10)
        service.update_book_info(**data_book_update)
        service.delete_book(book_id=book_1.id)


def test_book_busy(service, book_1, book_2):
    service.book_repo.get_by_id = Mock(return_value=book_2)
    with pytest.raises(errors.BookBusy):
        service.take_book(book_id=book_1.id, taker_id=1)


def test_book_not_busy(service, book_1):
    with pytest.raises(errors.BookNotBusy):
        service.return_book(book_id=book_1.id, returner_id=1)

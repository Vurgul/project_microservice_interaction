from unittest.mock import Mock

import pytest
from book_service.application import interfaces


@pytest.fixture(scope='function')
def book_repo(book_1, book_2):
    book_repo = Mock(interfaces.BooksRepo)
    book_repo.get_by_id = Mock(return_value=book_1)
    book_repo.get_all = Mock(return_value=[book_1, book_2])
    return book_repo

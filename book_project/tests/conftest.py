import pytest
from book_service.application import dataclasses


@pytest.fixture(scope='function')
def book_1():
    return dataclasses.Book(
        id=1,
        title='test_title_1',
        author='test_author_1',
        status=True
    )


@pytest.fixture(scope='function')
def book_2():
    return dataclasses.Book(
        id=2,
        title='test_title_2',
        author='test_author_2',
        status=False
    )

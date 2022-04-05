from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Book

from classic.messaging import Message, Publisher

join_points = PointCut()
join_point = join_points.join_point


class BookInfo(DTO):
    author: str
    title: int
    id: Optional[int]
    status: Optional[bool]


class BookUpDateInfo(DTO):
    author: Optional[str]
    title: Optional[int]
    status: Optional[bool]
    id: int


@component
class BookService:
    book_repo: interfaces.BooksRepo
    publisher: Publisher

    @join_point
    @validate_arguments
    def get_book_info(self, book_id: int) -> Book:
        book = self.book_repo.get_by_id(book_id)
        if book is None:
            raise errors.NoBook(id=book_id)
        print(book)
        return book

    @join_point
    def get_books_info(self) -> List[Book]:
        books = self.book_repo.get_all()
        return books

    @join_point
    @validate_with_dto
    def create_book(self, book_info: BookInfo) -> Book:
        book = book_info.create_obj(Book)
        self.book_repo.add(book)
        return book

    @join_point
    @validate_arguments
    def update_book_info(self, book_id: int, **kwargs) -> Book:
        book = self.get_book_info(book_id)
        modern_book = BookUpDateInfo(id=book_id, **kwargs)
        modern_book.populate_obj(book)
        return book

    @join_point
    @validate_arguments
    def delete_book(self, book_id: int):
        book = self.get_book_info(book_id)
        self.book_repo.remove(book)

    @join_point
    @validate_arguments
    def take_book(self, book_id: int, taker_id: int):
        book = self.get_book_info(book_id)
        if book.status is True:
            modern_book = BookUpDateInfo(id=book_id, status=False)
            modern_book.populate_obj(book)

            # TODO: докрутить паблишера
        else:
            raise errors.BookBusy(id=book_id)

    @join_point
    @validate_arguments
    def return_book(self, book_id: int, taker_id: int):
        book = self.get_book_info(book_id)
        if book.status is False:
            modern_book = BookUpDateInfo(id=book_id, status=True)
            modern_book.populate_obj(book)

            # TODO: докрутить паблишера
        else:
            raise errors.BookNotBusy(id=book_id)

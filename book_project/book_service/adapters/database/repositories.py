from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from book_service.application import interfaces
from book_service.application.dataclasses import Book
from sqlalchemy import select


@component
class BooksRepo(BaseRepository, interfaces.BooksRepo):

    def get_by_id(self, id: int) -> Optional[Book]:
        query = select(Book).where(Book.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, book: Book):
        self.session.add(book)
        self.session.flush()

    def get_all(self):
        query = select(Book)
        return self.session.execute(query).scalars().all()

    def remove(self, book: Book):
        self.session.delete(book)

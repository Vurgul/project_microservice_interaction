from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import Book


class BooksRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Book]: ...

    @abstractmethod
    def add(self, book: Book): ...

    @abstractmethod
    def remove(self, book: Book): ...

    @abstractmethod
    def get_all(self): ...

from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]: ...

    @abstractmethod
    def add(self, user: User): ...

    @abstractmethod
    def remove(self, user: User): ...

    @abstractmethod
    def get_all(self): ...

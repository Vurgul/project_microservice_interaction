from abc import ABC, abstractmethod
from typing import Optional

from .dataclasses import Issue


class IssuesRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Issue]: ...

    @abstractmethod
    def add(self, issue: Issue): ...

    @abstractmethod
    def remove(self, issue: Issue): ...

    @abstractmethod
    def get_all(self): ...

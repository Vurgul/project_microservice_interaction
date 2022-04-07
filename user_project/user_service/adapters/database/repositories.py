from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select
from user_service.application import interfaces
from user_service.application.dataclasses import User


@component
class UsersRepo(BaseRepository, interfaces.UsersRepo):

    def get_by_id(self, id: int) -> Optional[User]:
        query = select(User).where(User.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, user: User):
        self.session.add(user)
        self.session.flush()

    def get_all(self):
        query = select(User)
        return self.session.execute(query).scalars().all()

    def remove(self, user: User):
        self.session.delete(user)

from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import User

join_points = PointCut()
join_point = join_points.join_point


class UserInfo(DTO):
    name: str
    age: int
    id: Optional[int]


class UserUpDateInfo(DTO):
    name: Optional[str]
    age: Optional[int]
    id: int


@component
class UserService:
    user_repo: interfaces.UsersRepo

    @join_point
    @validate_arguments
    def get_user_info(self, user_id: int) -> User:
        user = self.user_repo.get_by_id(user_id)
        if user is None:
            raise errors.NoUser(id=user_id)
        print(user)
        return user

    @join_point
    def get_users_info(self) -> List[User]:
        users = self.user_repo.get_all()
        return users

    @join_point
    @validate_with_dto
    def create_user(self, user_info: UserInfo) -> User:
        user = user_info.create_obj(User)
        self.user_repo.add(user)
        return user

    @join_point
    @validate_arguments
    def update_user_info(self, user_id: int, **kwargs) -> User:
        user = self.get_user_info(user_id)
        modern_user = UserUpDateInfo(id=user_id, **kwargs)
        modern_user.populate_obj(user)
        print(user)
        return user

    @join_point
    @validate_arguments
    def delete_user(self, user_id: int):
        user = self.get_user_info(user_id)
        self.user_repo.remove(user)

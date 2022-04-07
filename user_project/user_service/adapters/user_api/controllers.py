from attr import asdict
from classic.components import component
from user_service.application import services

from .join_points import join_point


@component
class Users:
    users: services.UserService

    @join_point
    def on_get_user_info(self, request, response):
        """Получить информацию о пользователе"""
        user = self.users.get_user_info(
            **request.params
        )
        response.media = asdict(user)

    @join_point
    def on_get_users(self, request, response):
        """Получить информацию о всех пользователях"""
        users = self.users.get_users_info()
        response.media = [asdict(user) for user in users]


    @join_point
    def on_post_add_user(self, request, response):
        """Добавить пользователя"""
        user = self.users.create_user(
            **request.media
        )

        response.media = {
            'user_id': user.id
        }

    @join_point
    def on_post_edit_user(self, request, response):
        """Изменение данных пользователя"""
        user = self.users.update_user_info(
            **request.media
        )
        response.media = asdict(user)

    @join_point
    def on_post_delete_user(self, request, response):
        """ Удалить пользователя"""
        self.users.delete_user(
            **request.media
        )

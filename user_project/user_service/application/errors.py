from classic.app.errors import AppError


class NoUser(AppError):
    msg_template = 'No user with id {id}'
    code = 'chat.no_user'
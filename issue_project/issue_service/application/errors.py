from classic.app.errors import AppError


class NoIssue(AppError):
    msg_template = 'No issue with id {id}'
    code = 'issue.no_issue'


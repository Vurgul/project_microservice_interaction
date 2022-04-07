from attr import asdict
from classic.components import component
from issue_service.application import services

from .join_points import join_point


@component
class Issues:
    issues: services.IssueService

    @join_point
    def on_get_issue_info(self, request, response):
        """Получить информацию о заметки"""
        issue = self.issues.get_issue_info(
            **request.params
        )
        response.media = asdict(issue)

    @join_point
    def on_get_issues(self, request, response):
        """Получить информацию о всех заметках"""
        issues = self.issues.get_issues_info()
        for issue in issues:
            issue.date = issue.date.strftime('%Y-%m-%d %H:%M:%S')
        response.media = [asdict(issue) for issue in issues]


    @join_point
    def on_post_add_issue(self, request, response):
        """Добавить заметку"""
        issue = self.issues.create_issue(
            **request.media
        )

        response.media = {
            'issue_id': issue.id
        }

    @join_point
    def on_post_edit_issue(self, request, response):
        """Изменение данных заметки"""
        issue = self.issues.update_issue_info(**request.media)
        response.media = asdict(issue)

    @join_point
    def on_post_delete_issue(self, request, response):
        """ Удалить заметку"""
        self.issues.delete_issue(**request.media)

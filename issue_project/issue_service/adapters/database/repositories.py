from typing import Optional

from classic.components import component
from classic.sql_storage import BaseRepository
from issue_service.application import interfaces
from issue_service.application.dataclasses import Issue
from sqlalchemy import select


@component
class IssuesRepo(BaseRepository, interfaces.IssuesRepo):

    def get_by_id(self, id: int) -> Optional[Issue]:
        query = select(Issue).where(Issue.id == id)
        return self.session.execute(query).scalars().one_or_none()

    def add(self, issue: Issue):
        self.session.add(issue)
        self.session.flush()

    def get_all(self):
        query = select(Issue)
        return self.session.execute(query).scalars().all()

    def remove(self, issue: Issue):
        self.session.delete(issue)

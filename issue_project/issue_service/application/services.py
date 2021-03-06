from datetime import datetime
from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from classic.messaging import Publisher
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Issue

join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    action: str
    id: Optional[int]
    object_type: Optional[str]
    object_id: Optional[int]


class IssueUpDateInfo(DTO):
    action: Optional[str]
    object_type: Optional[str]
    object_id: Optional[int]
    id: int


class IssueConsumer(DTO):
    action: str
    object_type: str
    object_id: int
    id: Optional[int]

@component
class IssueService:
    issue_repo: interfaces.IssuesRepo
    publisher: Optional[Publisher] = None

    @join_point
    @validate_arguments
    def get_issue_info(self, issue_id: int) -> Issue:
        issue = self.issue_repo.get_by_id(issue_id)
        if issue is None:
            raise errors.NoIssue(id=issue_id)
        print(issue)
        return issue

    @join_point
    def get_issues_info(self) -> List[Issue]:
        issues = self.issue_repo.get_all()
        #for issue in issues:
        #    issue.date = issue.date.strftime('%Y-%m-%d %H:%M:%S')
        return issues

    @join_point
    @validate_with_dto
    def create_issue(self, issue_info: IssueInfo) -> Issue:
        issue = issue_info.create_obj(Issue)
        self.issue_repo.add(issue)
        return issue

    @join_point
    @validate_arguments
    def update_issue_info(self, issue_id: int, **kwargs) -> Issue:
        issue = self.get_issue_info(issue_id)
        modern_issue = IssueUpDateInfo(id=issue_id, **kwargs)
        modern_issue.populate_obj(issue)
        return issue

    @join_point
    @validate_arguments
    def delete_issue(self, issue_id: int):
        issue = self.get_issue_info(issue_id)
        self.issue_repo.remove(issue)

    @join_point
    def take_message(self, action: str, object_type: str, object_id: int):
        new_issue = Issue(action=action, object_type=object_type, object_id=object_id)
        self.issue_repo.add(new_issue)

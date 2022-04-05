from typing import List, Optional

from classic.app import DTO, validate_with_dto
from classic.aspects import PointCut
from classic.components import component
from pydantic import validate_arguments

from . import errors, interfaces
from .dataclasses import Issue

join_points = PointCut()
join_point = join_points.join_point


class IssueInfo(DTO):
    author: str
    title: int
    id: Optional[int]
    status: Optional[bool]


class IssueUpDateInfo(DTO):
    author: Optional[str]
    title: Optional[int]
    status: Optional[bool]
    id: int


@component
class IssueService:
    issue_repo: interfaces.IssuesRepo

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


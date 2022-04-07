from unittest.mock import Mock

import pytest
from issue_service.application import errors
from issue_service.application.services import IssueService

data_issue = {
    'id': 3,
    'action': 'test_action_3',
    'object_type': 'test_object_type_3',
    'object_id': 3
}

data_issue_update = {
    'issue_id': 1,
    'action': 'NewAction',
}


@pytest.fixture(scope='function')
def service(issue_repo):
    return IssueService(issue_repo=issue_repo, publisher=None)


def test_get_issue_info(service, issue_repo, issue_1):
    issue = service.get_issue_info(issue_id=issue_1.id)
    assert issue == issue_1


def test_get_issues_info(service, issue_1, issue_2):
    issues = service.get_issues_info()
    assert issue_1 in issues
    assert issue_2 in issues
    assert len(issues) == 2


def test_create_issue(service):
    service.create_issue(**data_issue)
    service.issue_repo.add.assert_called_once()


def test_update_issue_info(service, issue_1):
    service.update_issue_info(**data_issue_update)
    assert issue_1.action == 'NewAction'
    assert issue_1.object_type == 'test_object_type_1'


def test_delete_issue(service, issue_1):
    service.delete_issue(issue_id=issue_1.id)
    service.issue_repo.remove.assert_called_once()


def test_no_issue_in_database(service, issue_1):
    service.issue_repo.get_by_id = Mock(return_value=None)
    with pytest.raises(errors.NoIssue):
        service.get_issue_info(issue_id=10)
        service.update_issue_info(**data_issue_update)
        service.delete_issue(issue_id=issue_1.id)

from unittest.mock import Mock

import pytest
from issue_service.application import interfaces


@pytest.fixture(scope='function')
def issue_repo(issue_1, issue_2):
    issue_repo = Mock(interfaces.IssuesRepo)
    issue_repo.get_by_id = Mock(return_value=issue_1)
    issue_repo.get_all = Mock(return_value=[issue_1, issue_2])
    return issue_repo

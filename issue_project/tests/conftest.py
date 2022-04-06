import pytest
from issue_service.application import dataclasses


@pytest.fixture(scope='function')
def issue_1():
    return dataclasses.Issue(
        id=1,
        action='test_action_1',
        object_type='test_object_type_1',
        object_id=1
    )


@pytest.fixture(scope='function')
def issue_2():
    return dataclasses.Issue(
        id=2,
        action='test_action_2',
        object_type='test_object_type_2',
        object_id=2
    )

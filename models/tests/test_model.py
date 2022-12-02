import models.models as models
import pytest

@pytest.fixture
def my_user():
    return models.User()

def test_user():
    test_cases = [
        {
            "name": "pass",
            "id": 1,
            "username": "jimmy",
            "email": "okidijimmie@gmail.com",
            "password": "test234",
            "output":  "jimmy"
        }
    ]
    for test_case in test_cases:
        my_user = models.User(test_case['id'], test_case['username'], test_case['email'], test_case['password'])
        assert my_user.username == test_case['output']
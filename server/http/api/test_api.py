from unittest import mock
from server.http.server import get_app
from server.http.middleware.middleware import TokenRequired
from models.sportbet_models import (
    CreateBetRequest,
    CreateBetResponse,
)
from models.user_models import (
    ValidateTokenRequest,
    ValidateTokenResponse,
)

class MockAuthProvider:
    def validate_token(self, request: ValidateTokenRequest) -> ValidateTokenResponse:
        return ValidateTokenResponse(200, "OK", "test_user")

def test_create_bet(mocker):
    # prepare
    class MockSportProvider:
        def create_bet(self, req: CreateBetRequest) -> CreateBetResponse:
            pass

    mock_sport_service = MockSportProvider()
    sport_spy = mocker.spy(mock_sport_service, 'create_bet')

    mock_auth_service = MockAuthProvider()
    auth_spy = mocker.spy(mock_auth_service, 'validate_token')

    flask_app = get_app(
        mock_auth_service,
        None,
        mock_sport_service,
    )
    test_client = flask_app.test_client()

    test_cases = [
        {
            "name": "success",
            "path": "/createbet",
            "input": {
                "league": "test",
                "home_team": "",
                "away_team": ""
            },
            "output": 200
        },
    ]
    for test_case in test_cases:
        res = test_client.post(test_case['path'], json=test_case['input'], headers={
                               "Authorization": "Authorization valid"})

        assert res.status_code == test_case['output']
        sport_spy.assert_called_once()
        auth_spy.assert_called_once()


def test_read_bet(client):
    test_cases = [
        {
            "name": "pass",
            "input": "/readbet",
            "output": 200
        },
        {
            "name": "fail",
            "input": "/read",
            "output": 401
        }
    ]
    for test_case in test_cases:
        response = TokenRequired(mock.MagicMock())
        res = response.validate_token(client.get(
            test_case['input'])).return_value = test_case["output"]
        assert res == test_case['output']


def test_update_bet(client):
    test_cases = [
        {
            "name": "pass",
            "input": "updatebet/<id>",
            "output": 200
        },
        {
            "name": "fail",
            "input": "updatebet/<i",
            "output": 401
        }
    ]
    for test_case in test_cases:
        response = TokenRequired(mock.MagicMock())
        res = response.validate_token(client.put(
            test_case['input'])).return_value = test_case["output"]
        assert res == test_case['output']


def test_delete(client):
    test_cases = [
        {
            "name": "pass",
            "input": "/deletebet",
            "output": 200
        },
        {
            "name": "fail",
            "input": "/delete",
            "output": 401
        }
    ]
    for test_case in test_cases:
        response = TokenRequired(mock.MagicMock())
        res = response.validate_token(client.delete(
            test_case['input'])).return_value = test_case["output"]
        assert res == test_case['output']

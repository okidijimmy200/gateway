from unittest import mock
from server.http.middleware.middleware import TokenRequiredService


def test_create_bet(app, client):
    test_cases = [
        {
        "name": "pass",
        "input": "/createbet",
        "output": 200
        },
        {
        "name": "fail",
        "input": "/createbe",
        "output": 401
        }
    ]
    for test_case in test_cases:
        view_function_name = f'api.create_bet'
        view_function = app.view_functions[view_function_name]
        
        response = TokenRequiredService(mock.MagicMock())
        response.validate_token(view_function)
        res = client.post(test_case['input'])
        assert res.status_code == test_case['output']

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
        response = TokenRequiredService(mock.MagicMock())
        res = response.validate_token(client.get(test_case['input'])).return_value = test_case["output"]
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
        response = TokenRequiredService(mock.MagicMock())
        res = response.validate_token(client.put(test_case['input'])).return_value = test_case["output"]
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
        response = TokenRequiredService(mock.MagicMock())
        res = response.validate_token(client.delete(test_case['input'])).return_value = test_case["output"]
        assert res == test_case['output']
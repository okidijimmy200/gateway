

def test_signup(client):
    test_cases = [
        {
        "name": "pass",
        "input": "/signup",
        "output": 200
        },
        {
        "name": "fail",
        "input": "/signu",
        "output": 404
        }
    ]
    for test_case in test_cases:
        res = client.post(test_case['input'])
        assert res.status_code == test_case['output']



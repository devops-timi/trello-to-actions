import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.get_json() == {"status": "UP"}


def test_sum(client):
    res = client.post('/sum', json={"a": 5, "b": 10})
    assert res.get_json()["result"] == 15


def test_reverse(client):
    res = client.post('/reverse-string', json={"text": "hello"})
    assert res.get_json()["result"] == "olleh"


def test_sum_invalid_input(client):
    res = client.post('/sum', json={"a": "hello", "b": 10})
    assert res.status_code == 400
    assert res.get_json()["error"] == "Invalid input"


def test_sum_with_negative(client):
    res = client.post('/sum', json={"a": -5, "b": 10})
    assert res.get_json()["result"] == 5


def test_sum_with_zero(client):
    res = client.post('/sum', json={"a": 0, "b": 0})
    assert res.get_json()["result"] == 0


def test_reverse_empty_string(client):
    res = client.post('/reverse-string', json={"text": ""})
    assert res.get_json()["result"] == ""


def test_reverse_single_char(client):
    res = client.post('/reverse-string', json={"text": "a"})
    assert res.get_json()["result"] == "a"


# Additional 8th test: Testing sum with missing keys (defaults to 0)
def test_sum_missing_keys(client):
    res = client.post('/sum', json={})
    assert res.get_json()["result"] == 0


# Additional Unit tests
def test_reverse_long_string(client):
    res = client.post('/reverse-string', json={"text": "abcdef"})
    assert res.get_json()["result"] == "fedcba"


def test_sum_large_numbers(client):
    res = client.post('/sum', json={"a": 1000000, "b": 2000000})
    assert res.get_json()["result"] == 3000000


def test_health_status_key(client):
    res = client.get('/health')
    assert "status" in res.get_json()


def test_sum_invalid_string(client):
    res = client.post('/sum', json={"a": "abc", "b": 10})
    assert res.status_code == 400

    
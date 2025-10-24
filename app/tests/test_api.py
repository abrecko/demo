from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_plus_happy():
    r = client.post("/calc/plus", json={"a": 1, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 3


def test_minus_happy():
    r = client.post("/calc/minus", json={"a": 5, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 2


def test_multiply_happy():
    r = client.post("/calc/multiply", json={"a": 2, "b": 4})
    assert r.status_code == 200
    assert r.json()["result"] == 8


def test_divide_happy():
    r = client.post("/calc/divide", json={"a": 10, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 5


def test_safe_div_happy():
    r = client.post("/calc/safe-div", json={"a": 10, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 5


def test_divide_by_zero():
    r = client.post("/calc/divide", json={"a": 1, "b": 0})
    assert r.status_code == 400
    assert r.json()["detail"] == "Cannot divide by zero"


def test_safe_div_by_zero():
    r = client.post("/calc/safe-div", json={"a": 1, "b": 0})
    assert r.status_code == 400
    assert r.json()["detail"] == "Cannot divide by zero"


def test_validation_error():
    r = client.post("/calc/plus", json={"a": "not-a-number", "b": 2})
    assert r.status_code == 422

from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


def test_question_answer_json():
    questions = {"questions": ["What is the capital of France?"]}
    files = {
        "document": ("doc.json", '{"content": "Paris is the capital of France."}', "application/json")
    }
    
    response = client.post("/question-answer/", json=questions, files=files)
    assert response.status_code == 200
    assert response.json() == [{"question": "What is the capital of France?", "answer": "Paris"}]


def test_question_answer_pdf():
    questions = {"questions": ["Who wrote Hamlet?"]}
    files = {
        "document": ("hamlet.pdf", open("tests/hamlet.pdf", "rb"), "application/pdf")
    }
    
    response = client.post("/question-answer/", json=questions, files=files)
    assert response.status_code == 200
    assert response.json() == [{"question": "Who wrote Hamlet?", "answer": "William Shakespeare"}]


def test_unsupported_file_type():
    questions = {"questions": ["What is the capital of France?"]}
    files = {
        "document": ("doc.txt", "Some random text", "text/plain")
    }
    
    response = client.post("/question-answer/", json=questions, files=files)
    assert response.status_code == 400
    assert response.json() == {"detail": "Unsupported file type. Only JSON and PDF are allowed."}


def test_rate_limiter():
    from app.utils.rate_limiter import rate_limiter
    from starlette.requests import Request
    import time

    request_mock = Request({"type": "http", "client": ("127.0.0.1", 8080)})
    rate_limiter(request_mock)  # First request allowed
    for _ in range(59):
        rate_limiter(request_mock)  # 59 more requests allowed
    with pytest.raises(HTTPException):
        rate_limiter(request_mock)  # 61st request blocked
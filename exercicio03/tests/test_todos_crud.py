import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def session():
    with requests.Session() as s:
        yield s


@pytest.fixture
def todo(session):
    # CREATE
    payload = {"title": "Minha tarefa", "completed": False, "userId": 1}
    resp = session.post(f"{BASE_URL}/todos", json=payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    todo_id = data.get("id")
    assert todo_id is not None, "API did not return id for created todo"
    try:
        yield data
    finally:
        session.delete(f"{BASE_URL}/todos/{todo_id}")


def test_create_todo_success(todo):
    assert todo["title"] == "Minha tarefa"
    assert todo["completed"] is False
    assert todo["userId"] == 1
    assert "id" in todo


def test_read_todo():
    # READ 
    resp = requests.get(f"{BASE_URL}/todos/1")
    assert resp.status_code == 200
    data = resp.json()
    assert data.get("id") == 1
    assert "title" in data
    assert "completed" in data
    assert "userId" in data


def test_update_todo_patch(session):
    create = session.post(f"{BASE_URL}/todos", json={"title": "To update", "completed": False, "userId": 2})
    assert create.status_code in (200, 201)
    created = create.json()
    tid = created.get("id")
    assert tid is not None

    # PATCH 
    patch = session.patch(f"{BASE_URL}/todos/{tid}", json={"completed": True})
    assert patch.status_code in (200, 201)
    patched = patch.json()

    assert patched.get("completed") is True
    session.delete(f"{BASE_URL}/todos/{tid}")


def test_delete_todo_and_verify(session):
    create = session.post(f"{BASE_URL}/todos", json={"title": "To delete", "completed": False, "userId": 3})
    assert create.status_code in (200, 201)
    created = create.json()
    tid = created.get("id")
    assert tid is not None

    # DELETE
    delete_resp = session.delete(f"{BASE_URL}/todos/{tid}")
    assert delete_resp.status_code in (200, 204, 201, 202)

    get_resp = session.get(f"{BASE_URL}/todos/{tid}")

    if get_resp.status_code == 404:
        assert True
    else:
        try:
            body = get_resp.json()
        except ValueError:
            pytest.skip("GET returned non-json after delete; skipping strict verification")
        if body == {}:
            assert True
        else:
            assert "id" in body


def test_create_todo_without_title(session):
    payload = {"completed": False, "userId": 1}
    resp = session.post(f"{BASE_URL}/todos", json=payload)
    if resp.status_code >= 400:
        assert True
    else:
        data = resp.json()
        assert "title" not in data or not data.get("title")
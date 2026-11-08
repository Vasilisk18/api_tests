import pytest

def test_get_post_has_required_fields(api, base_url):
    posts = api.get(url = f"{base_url}/posts/1", timeout=5)
    assert posts.status_code == 200
    data = posts.json()
    for key in ["userId", "id", "title", "body"]:
        assert key in data

def test_get_nonexistent_post_returns_404(api, base_url):
    posts = api.get(url = f"{base_url}/posts/9999", timeout=5)
    assert posts.status_code == 404

def test_create_post_returns_201(api, base_url):
    payload = {"title": "test", "body": "test"}
    posts = api.post(url = f"{base_url}/posts", json = payload, timeout=5)
    assert posts.status_code == 201
    data = posts.json()
    assert data["title"] == "test"
    assert "id" in data

def test_delete_post_returns_200(api, base_url):
    posts = api.delete(url = f"{base_url}/posts/1", timeout=5)
    assert posts.status_code == 200

def test_update_post_returns_200(api, base_url):
    payload = {"id": 1, "userId": 1, "title": "new title", "body": "new body"}
    posts = api.put(url = f"{base_url}/posts/1", json = payload, timeout=5)
    assert posts.status_code == 200
    data = posts.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]

def test_patch_post_returns_new_title(api, base_url):
    payload = {"title": "test2"}
    posts = api.patch(url = f"{base_url}/posts/1", json = payload, timeout=5)
    assert posts.status_code == 200
    data = posts.json()
    assert data["title"] == payload["title"]
    assert "body" in data
    assert data["id"] == 1

@pytest.mark.parametrize("user_id", [1,2,3])
def test_get_user_post_returns_200(api, base_url, user_id):
    response = api.get(f"{base_url}/posts", params = {"userId": user_id}, timeout=5)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    for post in data:
        assert post["userId"] == user_id
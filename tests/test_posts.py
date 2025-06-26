import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_post_and_operations():
    # Register user
    email = "postuser@example.com"
    password = "strongpassword"
    client.post("/auth/register", json={"email": email, "password": password})
    
    # Login user
    login_res = client.post("/auth/login", data={"username": email, "password": password})
    tokens = login_res.json()
    access_token = tokens["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    
    # Create post
    post_data = {"title": "Test Post", "content": "This is a test post content."}
    create_res = client.post("/posts/", json=post_data, headers=headers)
    assert create_res.status_code == 201
    post = create_res.json()
    post_id = post["id"]
    assert post["title"] == post_data["title"]
    assert post["content"] == post_data["content"]
    
    # Get post
    get_res = client.get(f"/posts/{post_id}")
    assert get_res.status_code == 200
    assert get_res.json()["id"] == post_id
    
    # Update post
    updated_data = {"title": "Updated Title", "content": "Updated content."}
    update_res = client.put(f"/posts/{post_id}", json=updated_data, headers=headers)
    assert update_res.status_code == 200
    updated_post = update_res.json()
    assert updated_post["title"] == updated_data["title"]
    
    # Delete post
    delete_res = client.delete(f"/posts/{post_id}", headers=headers)
    assert delete_res.status_code == 204
    
    # Confirm deletion
    confirm_res = client.get(f"/posts/{post_id}")
    assert confirm_res.status_code == 404

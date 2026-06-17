def test_register_succes(client):
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@test.com"
    assert "id" in data

def test_register_existing_email(client):
    client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    assert response.status_code == 400

def test_login_succes(client):
    client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "test123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"
    })
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
                           

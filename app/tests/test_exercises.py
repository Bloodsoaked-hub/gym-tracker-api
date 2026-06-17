def get_auth_header(client):
    client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test123"  
    })
    response = client.post("/auth/login", json={
        "email": "test@test.com",
        "password": "test123"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_exercise(client):
    headers = get_auth_header(client)
    response = client.post("/exercises", json={
        "name": "Bench Press",
        "description": "Chest exercise",
        "muscle_group": "Chest"
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Bench Press"

def test_list_exercises(client):
    headers = get_auth_header(client)
    client.post("/exercises/", json={
        "name": "Squat",
        "muscle_group": "Legs"
    }, headers=headers)
    response = client.get("/exercises/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1

def test_create_exercise_without_auth(client):
    response = client.post("/exercises/", json={
        "name": "Deadlift",
        "muscle_group": "Back"
    })
    assert response.status_code == 401
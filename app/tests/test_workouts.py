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


def test_create_workout(client):
    headers = get_auth_header(client)
    response = client.post("/workouts/", json={
        "date": "2026-06-15T10:00:00",
        "duration_minutes": 60,
        "notes": "Leg day"
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["notes"] == "Leg day"


def test_list_workouts(client):
    headers = get_auth_header(client)
    client.post("/workouts/", json={
        "date": "2026-06-15T10:00:00",
        "duration_minutes": 60
    }, headers=headers)
    response = client.get("/workouts/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_get_workout_not_found(client):
    headers = get_auth_header(client)
    response = client.get("/workouts/999", headers=headers)
    assert response.status_code == 404


def test_add_exercise_to_workout(client):
    headers = get_auth_header(client)
    
    workout_response = client.post("/workouts/", json={
        "date": "2026-06-15T10:00:00",
        "duration_minutes": 60
    }, headers=headers)
    workout_id = workout_response.json()["id"]

    exercise_response = client.post("/exercises/", json={
        "name": "Squat",
        "muscle_group": "Legs"
    }, headers=headers)
    exercise_id = exercise_response.json()["id"]

    response = client.post(f"/workouts/{workout_id}/exercises/", json={
        "exercise_id": exercise_id,
        "sets": 3,
        "reps": 10,
        "weight": 100.0
    }, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["exercise_name"] == "Squat"
    assert data["sets"] == 3
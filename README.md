# Gym Tracker API

A RESTful API for tracking gym workouts and exercises, built with FastAPI and PostgreSQL.

## Tech Stack

- **Python 3.11** + **FastAPI**
- **PostgreSQL 16**
- **SQLAlchemy** + **Alembic** (migrations)
- **JWT** authentication (python-jose)
- **Docker** + **Docker Compose**
- **pytest** (11 tests)

## Features

- User registration and login with JWT authentication
- CRUD operations for exercises
- CRUD operations for workouts
- Adding exercises to workouts with sets, reps, and weight tracking
- Automatic API documentation (Swagger UI)

## Getting Started

### Prerequisites

- Docker

### Installation 

1. Clone the repository:
``` bash
git clone https://github.com/Username/gym-tracker-api
cd gym_tracker_api
```

2. Create `.env` file:
```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/gym_tracker
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. Run the application
```bash
docker compose up --build
```

4. Run database migrations:
```bash
docker compose exec api alembic upgrade head
```

5. API is available at: `http://localhost:8000`
6. Swagger docs: `http://localhost:8000/docs`

## Running Tests

```bash
docker compose exec api pytest
```

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/register | Register new user |
| POST | /auth/login | Login and get JWT token |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /users/me | Get current user |

### Exercises
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /exercises/ | List all exercises |
| POST | /exercises/ | Create exercise |
| PUT | /exercises/{id} | Update exercise |
| DELETE | /exercises/{id} | Delete exercise |

### Workouts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /workouts/ | List user workouts |
| POST | /workouts/ | Create workout |
| GET | /workouts/{id} | Get workout details |
| DELETE | /workouts/{id} | Delete workout |
| POST | /workouts/{id}/exercises/ | Add exercise to workout |
| GET | /workouts/{id}/exercises/ | List workout exercises |

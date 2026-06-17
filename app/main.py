from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api.router import api_router

app = FastAPI()

app.include_router(api_router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title="Gym Tracker API",
        version="1.0.0",
        description="API for tracking gym workouts and exercises",
        routes=app.routes,
    )
    schema["components"]["securitySchemes"]["bearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
    }
    for path in schema["paths"].values():
        for method in path.values():
            method["security"] = [{"bearerAuth": []}]
    
    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = custom_openapi
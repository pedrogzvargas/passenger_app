from fastapi import FastAPI

from app.api.v1.passenger.routes import passenger_router

app = FastAPI(root_path="/api/v1", title="Traxion-Passenger-App")

app.include_router(passenger_router)

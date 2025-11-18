# powerplant-challenge/app/main.py

from fastapi import FastAPI
from app.routers import production_plan

# FastAPI Application Setup
app = FastAPI()

# --- Routers ---
# Include the production_plan router, which handles the /productionplan endpoint.
app.include_router(production_plan.router)

# powerplant-challenge/app/models/data_models.py

from pydantic import BaseModel, Field, conlist
from typing import Literal

# --- Input Schemas ---

class Fuels(BaseModel):
    gas_euro_per_mwh: float = Field(alias="gas(euro/MWh)", gt=0)
    kerosine_euro_per_mwh: float = Field(alias="kerosine(euro/MWh)", gt=0)
    co2_euro_per_ton: float = Field(alias="co2(euro/ton)", ge=0)
    wind_percentage: float = Field(alias="wind(%)", ge=0, le=100) # Percentage (0 to 100)

class Powerplant(BaseModel):
    name: str
    type: Literal["gasfired", "turbojet", "windturbine"]
    efficiency: float = Field(gt=0, le=1)  # 0 to 1 (e.g., 0.53)
    pmin: float = Field(ge=0)
    pmax: float = Field(ge=0)

class InputPayload(BaseModel):
    """The main input structure for the /productionplan endpoint."""
    load: float = Field(gt=0)
    fuels: Fuels
    powerplants: conlist(Powerplant, min_length=1)

# --- Output Schemas ---

class ProductionPlanItem(BaseModel):
    """Defines the production output for a single power plant."""
    name: str
    p: float = Field(ge=0) # Power produced (MWh), multiple of 0.1 MWh

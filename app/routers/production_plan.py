# powerplant-challenge/app/api/v1/endpoints/production_plan.py

from fastapi import APIRouter, HTTPException
from app.models.data_models import InputPayload, OutputResponse
from app.core.merit_order_solver import calculate_production_plan
import logging

# Set up a basic logger
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/productionplan")
async def post_production_plan(payload: InputPayload):
    try:
        # Call the core business logic solver
        production_list = calculate_production_plan(payload)
            
        return OutputResponse(productionplan=production_list)

    except Exception as e:
        logger.error(f"Runtime error during production plan calculation: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal calculation error.")
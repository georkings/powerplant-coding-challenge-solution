# tests/test_solver.py

import json
import pytest
from pathlib import Path
from app.core.merit_order_solver import calculate_production_plan
from app.models.data_models import InputPayload

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent

def load_json(filename: str):
    """Helper to load json from the example_payloads folder."""
    file_path = BASE_DIR / "example_payloads" / filename
    
    with open(file_path, "r") as f:
        return json.load(f)

@pytest.mark.parametrize("payload_file, expected_response_file", [
    ("payload3.json", "response3.json"),
])
def test_production_plan_calculation(payload_file, expected_response_file):
    # Load Input and expected response
    payload_data = load_json(payload_file)
    payload = InputPayload(**payload_data)
    expected_response = load_json(expected_response_file)
    
    # Run Solver
    actual_result_models = calculate_production_plan(payload)
    
    # Convert Pydantic objects to dicts for comparison
    actual_result_dicts = [item.model_dump() for item in actual_result_models]

    # Assert Results
    assert actual_result_dicts == expected_response

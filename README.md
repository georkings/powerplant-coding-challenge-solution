# **Powerplant Coding Challenge \- Solution**

This repository contains my REST API solution for the [Powerplant Coding Challenge](https://github.com/gems-st-ib/powerplant-coding-challenge). The application calculates the optimal production plan for a set of powerplants to meet a specific load, taking into account merit order, cost efficiency, and operational constraints (Pmin/Pmax).

## **🚀 Tech Stack**

* **Language:** Python 3.11
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Server:** Uvicorn
* **Containerization:** Docker

## **🛠️ How to Run**

### **Option 1: Running with Docker**

This is the easiest way to ensure the environment matches the specifications.

1. **Build the image:**
    ```
    docker build -t powerplant-api .
    ```

2. **Run the container:** The API will be exposed on port 8888.
    ```
    docker run -p 8888:8888 powerplant-api
    ```

3. **Access the API:**
    * **Swagger UI:** http://localhost:8888/docs  
    * **Endpoint:** `POST http://localhost:8888/productionplan`

### **Option 2: Running Locally**

1. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

2. **Launch the application:** Please ensure you run this command from the root directory of the project.
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 8888
    ```

## **🧪 Testing**

The project includes unit tests focusing on the core solver logic.

To run the tests:
```
pytest
```

## **🧠 The Algorithm**

The solution implements a greedy approach as follows:

1. **Cost Calculation:** Calculates the cost (€/MWh) for each plant (including CO2 costs for gas plants).  
2. **Sorting:** Plants are sorted by cost.  
3. **Greedy Dispatch:** Plants are committed in order of increasing cost until the load is met.  
4. **Constraint Handling (Pmin):** If the remaining load is smaller than the `Pmin` of the next available plant, the algorithm performs a backward adjustment:
    * It activates the cheapest available plant at its minimum capacity (`Pmin`).
    * It creates an oversupply.
    * It compensates by reducing the output of the most expensive already committed units.

### **Algorithmic Complexity Discussion**

The current solution operates with a complexity of approximately **O(N log N)** due to the sorting step. This is highly efficient and scalable for grids with hundreds of powerplants.

**The "Optimal" Mathematical Solution:** It is worth noting that to guarantee the absolute mathematical minimum in all edge cases involving constraints (like `Pmin`), one would need to evaluate all possible combinations of On/Off states.

* This approach would have a complexity of **O(2^n)**.
* While it guarantees perfection, it is computationally infeasible for large inputs.

## **🔮 Future Improvements**

Given more time, the following improvements would be prioritized:

1. **Floating Point Precision:**
    The current implementation uses standard Python `float` types. This can introduce minor precision errors (e.g., `0.1 + 0.2 != 0.3`). A more robust solution would utilize the `decimal.Decimal` class to ensure exact precision for currency and MWh values.
2. **Enhanced Test Coverage:**
    I would expand the current unit tests to include specific edge cases that rigorously test the Pmin backward adjustment mechanism and boundary conditions (e.g., load exactly equals available capacity, no available capacity).
3. **Integration Tests:**
    The current test suite focuses on unit testing the `merit_order_solver.py`. I would add Integration Tests using `FastAPI.testclient` to verify the full HTTP request/response cycle, including API routing, schema validation, and correct error handling (e.g., 422 for bad input).

from fastapi import FastAPI
from pydantic import BaseModel

from src.spending_calculator import get_total

app = FastAPI()


class SpendingRequest(BaseModel):
    costs: dict[str, float]
    items: list[str]
    tax: float


@app.post("/total")
def calculate_total(request: SpendingRequest) -> dict[str, float]:
    result = get_total(request.costs, request.items, request.tax)
    return {"result": result}
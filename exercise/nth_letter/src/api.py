from fastapi import FastAPI
from pydantic import BaseModel

from src.nth_letter import nth_letter

app = FastAPI()


class NthLetterRequest(BaseModel):
    words: list[str]


@app.post("/nth")
def get_nth_letter(request: NthLetterRequest) -> dict[str, str]:
    result = nth_letter(request.words)
    return {"result": result}
from fastapi import FastAPI

from src.dictionary import Dictionary

app = FastAPI()
dictionary = Dictionary()

@app.post("/entries")
def add_entry(word: str, definition: str) -> dict[str, str]:
    dictionary.newentry(word, definition)
    return {"message": f"Entry '{word}' added successfully"}

@app.get("/entries/{word}")
def look_entry(word: str) -> dict[str, str]:
    return {"result": dictionary.look(word)}
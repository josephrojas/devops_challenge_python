# 📖 Dictionary — Microservice

A REST microservice that exposes a simple in-memory dictionary with word lookup functionality. Built with FastAPI and deployed as a Docker container.

---

## 📋 Exercise Description

Implement a `Dictionary` class that supports adding word-definition pairs and looking them up. If a word doesn't exist, return a descriptive message instead of raising an exception.

```python
d = Dictionary()
d.newentry('Apple', 'A fruit that grows on trees')

print(d.look('Apple'))   # → A fruit that grows on trees
print(d.look('Banana'))  # → Can't find entry for Banana
```

---

## 🏗️ Structure

```
dictionary/
├── src/
│   ├── __init__.py
│   ├── dictionary.py    → Business logic
│   └── api.py           → FastAPI layer
├── tests/
│   ├── unit/
│   │   └── test_dictionary.py
│   └── integration/
│       └── test_api.py
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 🧠 Implementation

### Business Logic — `src/dictionary.py`

The `Dictionary` class stores entries in a private `dict[str, str]` and validates input types using `isinstance()`. Both `word` and `definition` must be strings — passing any other type raises a `TypeError`.

Key design decisions:
- **In-memory storage** — entries are lost on restart; no persistence layer for this exercise
- **Type validation** with `isinstance()` over type hints alone — runtime safety matters for an API
- **`dict.get()` with default** — avoids `KeyError` and returns a user-friendly message
- **Two-layer architecture** — business logic (`dictionary.py`) is fully decoupled from the HTTP layer (`api.py`)

### API Layer — `src/api.py`

Endpoints use a **Pydantic model** for request body validation, keeping the FastAPI layer thin — it only handles HTTP concerns and delegates all logic to the `Dictionary` class.

---

## 🌐 API Reference

### `POST /entries` — Add a word

**Request body:**
```json
{
  "word": "Apple",
  "definition": "A fruit that grows on trees"
}
```

**Response `200`:**
```json
{
  "message": "Entry 'Apple' added successfully"
}
```

---

### `GET /entries/{word}` — Look up a word

**Response `200` — word found:**
```json
{
  "result": "A fruit that grows on trees"
}
```

**Response `200` — word not found:**
```json
{
  "result": "Can't find entry for Banana"
}
```

---

## 🧪 Tests

### Unit Tests — `tests/unit/test_dictionary.py`

Tests cover the `Dictionary` class in isolation, with no HTTP layer involved.

| Test | Description |
|---|---|
| `test_add_value` | Adds a valid entry without raising exceptions |
| `test_newentry_invalid_key_type` | Raises `TypeError` when `word` is not a string |
| `test_newentry_invalid_value_type` | Raises `TypeError` when `definition` is not a string |
| `test_look_existing_entry` | Returns the correct definition for a known word |
| `test_look_missing_entry` | Returns `"Can't find entry for {word}"` when absent |
| `test_look_empty_dictionary` | Returns error message on empty dictionary |

### Integration Tests — `tests/integration/test_api.py`

Tests cover the full HTTP layer using FastAPI's `TestClient` — no server is started, tests run in-process.

| Test | Description |
|---|---|
| `test_add_entry` | `POST /entries` returns 200 with valid payload |
| `test_look_existing_entry` | `GET /entries/{word}` returns correct definition |
| `test_look_missing_entry` | `GET /entries/{word}` returns descriptive message |

### Coverage

```
Name                Stmts   Miss  Cover
---------------------------------------
src/dictionary.py      15      0   100%
---------------------------------------
TOTAL                  15      0   100%
```

---

## 🚀 Running Locally

### Install dependencies

```bash
uv sync --group dev
```

### Run lint + type check + tests

```bash
make check
```

### Run the API

```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000 --reload
```

### Example requests

```bash
# Add an entry
curl -X POST "localhost:8000/entries" \
     -H "Content-Type: application/json" \
     -d '{"word": "Apple", "definition": "A fruit that grows on trees"}'

# Look up a word
curl "localhost:8000/entries/Apple"

# Look up a missing word
curl "localhost:8000/entries/Banana"
```

Interactive docs available at `http://localhost:8000/docs`.

---

## 🐳 Docker

### Build

```bash
docker build -t dictionary:local .
```

### Run

```bash
docker run -p 8000:8000 dictionary:local
```

### Image

The Dockerfile uses a **multi-stage build**:
- **Builder stage** — installs all dependencies with `uv` into a virtualenv
- **Runtime stage** — copies only the `.venv` and `src/`, no build tools included

This keeps the final image minimal and free of development dependencies.

Published image:
```
ghcr.io/<owner>/devops_challenge_python/dictionary:main
```
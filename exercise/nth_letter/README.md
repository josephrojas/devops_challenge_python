# 🔤 Nth Letter — Microservice

A REST microservice that constructs a new word by concatenating the nth letter from each word in a list, where n is the position of the word in the list. Built with FastAPI and deployed as a Docker container.

---

## 📋 Exercise Description

Implement a `nth_letter(words)` function that takes a list of words and returns a string formed by concatenating the nth letter of each word, where n is the index of the word in the list. Words that are too short for their position are silently ignored.

```python
nth_letter(["yoda", "best", "has"])
#           n=0      n=1     n=2
#           y        e       s
# → "yes"
```

---

## 🏗️ Structure

```
nth_letter/
├── src/
│   ├── __init__.py
│   ├── nth_letter.py    → Business logic
│   └── api.py           → FastAPI layer
├── tests/
│   ├── unit/
│   │   └── test_nth_letter.py
│   └── integration/
│       └── test_api.py
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 🧠 Implementation

### Business Logic — `src/nth_letter.py`

`nth_letter` is implemented as a standalone function — stateless logic with a single clear responsibility.

Key design decisions:
- **Function over class** — no shared state between calls
- **Silent ignore for short words** — words shorter than their position index are skipped, consistent with the exercise note that test cases contain valid input
- **Silent ignore for empty strings** — an empty string at position n has no letter to contribute
- **`isinstance()` validation** — raises `TypeError` for non-list input or non-string elements
- **`enumerate()`** — cleanly pairs each word with its position index

### API Layer — `src/api.py`

A single `POST /nth` endpoint receives a JSON body with a `words` array. Pydantic handles type validation automatically — invalid payloads return `422 Unprocessable Entity` before reaching the business logic.

---

## 🌐 API Reference

### `POST /nth` — Get nth letter word

**Request body:**
```json
{
  "words": ["yoda", "best", "has"]
}
```

**Response `200`:**
```json
{
  "result": "yes"
}
```

---

## 🧪 Tests

### Unit Tests — `tests/unit/test_nth_letter.py`

| Test | Description |
|---|---|
| `test_nth_letter_basic` | Returns correct word from exercise example |
| `test_nth_letter_empty_list` | Empty list returns empty string |
| `test_nth_letter_single_word` | Single word returns its first letter |
| `test_nth_letter_word_too_short` | Words shorter than their position are ignored |
| `test_nth_letter_empty_string_ignored` | Empty strings in the list are ignored |
| `test_nth_letter_invalid_element_type` | Raises `TypeError` when an element is not a string |
| `test_nth_letter_invalid_input_type` | Raises `TypeError` when input is not a list |

### Integration Tests — `tests/integration/test_api.py`

| Test | Description |
|---|---|
| `test_nth_letter_basic` | `POST /nth` returns correct result with valid payload |
| `test_nth_letter_empty_list` | Empty list returns empty string at API level |
| `test_nth_letter_word_too_short` | Short words ignored at API level |
| `test_nth_letter_invalid_payload` | Invalid payload returns `422 Unprocessable Entity` |

### Coverage

```
Name                  Stmts   Miss  Cover
-----------------------------------------
src/nth_letter.py        14      0   100%
-----------------------------------------
TOTAL                    14      0   100%
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

### Example request

```bash
curl -X POST "localhost:8000/nth" \
     -H "Content-Type: application/json" \
     -d '{"words": ["yoda", "best", "has"]}'
# → {"result": "yes"}
```


---

## 🐳 Docker

### Build

```bash
docker build -t nth-letter:local .
```

### Run

```bash
docker run -p 8000:8000 nth-letter:local
```

### Image

Published image:
```
ghcr.io/<owner>/devops_challenge_python/nth_letter:main
```
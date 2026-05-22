# 🛒 Spending Calculator — Microservice

A REST microservice that calculates the total cost of a list of items with tax applied. Built with FastAPI and deployed as a Docker container.

---

## 📋 Exercise Description

Implement a `get_total(costs, items, tax)` function that calculates the total cost of purchased items plus a given tax rate. Items not found in the costs dictionary are silently ignored. The result is rounded to two decimal places.

```python
costs = {'socks': 5, 'shoes': 60, 'sweater': 30}

get_total(costs, ['socks', 'shoes'], 0.09)
# → 5 + 60 = 65
# → 65 + 0.09 of 65 = 70.85
# → Output: 70.85
```

---

## 🏗️ Structure

```
spending_calculator/
├── src/
│   ├── __init__.py
│   ├── spending_calculator.py    → Business logic
│   └── api.py                    → FastAPI layer
├── tests/
│   ├── unit/
│   │   └── test_spending_calculator.py
│   └── integration/
│       └── test_api.py
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```

---

## 🧠 Implementation

### Business Logic — `src/spending_calculator.py`

`get_total` is implemented as a standalone function — no class wrapper needed since there is no shared state between calls.

Key design decisions:
- **Function over class** — stateless logic doesn't benefit from encapsulation in a class
- **Silent ignore for missing items** — matches the exercise spec; no exception raised for unknown items
- **`isinstance()` validation** — runtime type safety for all three parameters
- **`round(..., 2)`** — applied after tax to avoid floating point accumulation errors

### API Layer — `src/api.py`

A single `POST /total` endpoint receives the full payload as a JSON body via a Pydantic model. Type validation at the HTTP layer is handled automatically by Pydantic — invalid payloads return `422 Unprocessable Entity` before reaching the business logic.

---

## 🌐 API Reference

### `POST /total` — Calculate total

**Request body:**
```json
{
  "costs": {"socks": 5, "shoes": 60, "sweater": 30},
  "items": ["socks", "shoes"],
  "tax": 0.09
}
```

**Response `200`:**
```json
{
  "result": 70.85
}
```

---

## 🧪 Tests

### Unit Tests — `tests/unit/test_spending_calculator.py`

| Test | Description |
|---|---|
| `test_get_total_basic` | Calculates correct total with existing items and tax |
| `test_get_total_missing_item_ignored` | Items not in costs are silently ignored |
| `test_get_total_empty_items` | Empty items list returns 0.00 |
| `test_get_total_all_items_missing` | All missing items returns 0.00 |
| `test_get_total_zero_tax` | Calculation with zero tax returns base sum |
| `test_get_total_rounding` | Result is always rounded to 2 decimal places |
| `test_get_total_invalid_costs_type` | Raises `TypeError` when costs is not a dict |
| `test_get_total_invalid_items_type` | Raises `TypeError` when items is not a list |
| `test_get_total_invalid_tax_type` | Raises `TypeError` when tax is not a number |

### Integration Tests — `tests/integration/test_api.py`

| Test | Description |
|---|---|
| `test_calculate_total_basic` | `POST /total` returns correct result with valid payload |
| `test_calculate_total_missing_item_ignored` | Missing items are ignored at API level |
| `test_calculate_total_empty_items` | Empty items list returns 0.0 |
| `test_calculate_total_invalid_payload` | Invalid payload returns `422 Unprocessable Entity` |

### Coverage

```
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/spending_calculator.py        12      0   100%
--------------------------------------------------
TOTAL                             12      0   100%
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
curl -X POST "localhost:8000/total" \
     -H "Content-Type: application/json" \
     -d '{
       "costs": {"socks": 5, "shoes": 60, "sweater": 30},
       "items": ["socks", "shoes"],
       "tax": 0.09
     }'
# → {"result": 70.85}
```


---

## 🐳 Docker

### Build

```bash
docker build -t spending-calculator:local .
```

### Run

```bash
docker run -p 8000:8000 spending-calculator:local
```

### Image

Published image:
```
ghcr.io/<owner>/devops_challenge_python/spending_calculator:main
```
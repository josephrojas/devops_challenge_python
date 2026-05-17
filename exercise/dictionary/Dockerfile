FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY src/ /app/src/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM python:3.12-slim AS runtime

RUN useradd -m appuser

# Solo copia el virtualenv y el código, sin uv
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src

WORKDIR /app
USER appuser

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
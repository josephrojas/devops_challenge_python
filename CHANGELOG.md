# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> From `v0.2.0` onwards, this file is updated automatically on every merge to `main` by a GitHub Action powered by the Claude API.

---

## [0.1.0] — 2026-05-17

### Added

#### Infrastructure & Pipeline
- Monorepo structure with `exercise/`, `infra/`, `.github/workflows/`, and `docs/` directories
- Root `Makefile` that orchestrates lint, type check, and test across all exercises
- GitHub Actions workflow (`build.yml`) with two jobs:
  - `sonarqube` — runs on every PR and push: installs dependencies with `uv`, executes `make check`, and uploads results to SonarCloud
  - `deploy_registry` — runs on push to `main` only: builds and pushes Docker images to `ghcr.io` using a matrix strategy across all exercises
- SonarCloud integration with Quality Gate: Security Rating A, Coverage ≥ 80%, Duplications ≤ 3%
- Multi-stage Dockerfile per exercise: builder stage installs dependencies with `uv`, runtime stage copies only `.venv` and `src/` for a minimal final image
- `sonar-project.properties` with multi-module configuration for the monorepo

#### Exercise — Dictionary
- `Dictionary` class with `newentry(word, definition)` and `look(word)` methods
- Runtime type validation using `isinstance()` — raises `TypeError` for non-string inputs
- `look()` returns `"Can't find entry for {word}"` instead of raising `KeyError`
- FastAPI microservice exposing `POST /entries` and `GET /entries/{word}`
- Pydantic request model for input validation at the HTTP layer
- Two-layer architecture: business logic fully decoupled from API layer
- 6 unit tests and integration tests via FastAPI `TestClient`
- 100% test coverage on `src/dictionary.py`
- `pyproject.toml` with `uv` managing dependencies and tool configuration (pytest, ruff, mypy)
- Per-exercise `Makefile` with `lint`, `test`, and `check` targets

#### Documentation
- Root `README.md` with project overview, stack, pipeline diagram, and roadmap
- `exercise/dictionary/README.md` with implementation details, API reference, test cases, and Docker instructions
- This `CHANGELOG.md`

### Architectural Decisions

- **One Docker image per exercise** — each microservice is independently deployable and versioned
- **`src/` layout** — prevents accidental imports of source files instead of installed packages
- **`uv` over pip/poetry** — faster installs, built-in lockfile, native `pyproject.toml` support
- **SonarCloud over self-hosted SonarQube** — zero infrastructure overhead for a personal project, same Quality Gate capabilities
- **Matrix strategy in GitHub Actions** — adding a new exercise only requires updating the matrix list, no new jobs needed
- **In-memory storage for Dictionary** — intentional for this exercise scope; no persistence layer needed

---

## [0.2.0] — 2026-05-17

### Added

- GitHub Actions workflow enhancement: container registry job (`deploy_registry`) that builds and pushes Docker images to `ghcr.io` for all exercises using matrix strategy
- Docker image metadata extraction and artifact attestation in CI/CD pipeline

### Changed

- GitHub Actions `build.yml` workflow restructured to include `REGISTRY` environment variable and conditional deployment to main branch only


*This changelog was written manually for v0.1.0. Subsequent versions are updated automatically.*
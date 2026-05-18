# 🐍 DevOps Challenge — Python Exercises

A complete DevOps pipeline built around three Python kata exercises, designed to demonstrate a full software development lifecycle: from TDD and static analysis to containerization, CI/CD, and AI-powered documentation.

> This project is primarily a learning exercise in DevOps practices. The Python exercises are intentionally simple — the complexity lives in the infrastructure and tooling around them.

---

## 📌 Exercises

| Exercise | Description | Status |
|---|---|---|
| `dictionary` | A `Dictionary` class with `newentry()` and `look()` methods | ✅ Done |
| `spending_calculator` | Calculates total cost of items with tax, ignoring unknown items | 🔜 Pending |
| `nth_letter` | Concatenates the nth letter of each word in a list | 🔜 Pending |

Each exercise is an independent microservice exposed via **FastAPI**, containerized with **Docker**, and published to **GitHub Container Registry**. See each exercise's README for implementation details, test cases, and API usage.

---

## 🏗️ Repository Structure

```
monorepo/
├── exercise/
│   ├── dictionary/           → Microservice 1
│   ├── spending_calculator/  → Microservice 2
│   └── nth_letter/           → Microservice 3
├── infra/
│   ├── ansible/              → Local environment provisioning
│   ├── terraform/            → AWS serverless stack
│   └── k8s/                  → Kubernetes manifests for k3d
├── .github/workflows/        → CI/CD pipeline
├── docs/                     → Architecture diagrams
├── Makefile                  → Runs all exercises
└── README.md
```

---

## 🛠️ Tech Stack

### Application
| Tool | Purpose |
|---|---|
| Python 3.12 | Runtime |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| uv | Dependency management |

### Quality
| Tool | Purpose |
|---|---|
| pytest + pytest-cov | Testing and coverage |
| ruff | Linting and formatting |
| mypy | Static type checking |
| SonarCloud | SAST and coverage gate (≥ 80% required) |

### CI/CD
| Tool | Purpose |
|---|---|
| GitHub Actions | Pipeline orchestration |
| ghcr.io | Container registry |
| docker/build-push-action | Multi-stage Docker builds |

### Infrastructure
| Tool | Purpose |
|---|---|
| k3d | Local Kubernetes cluster |
| Ansible | Local environment provisioning |
| Terraform | AWS infrastructure as code |
| AWS Lambda + API Gateway | Serverless deployment |
| AWS S3 + CloudFront | Static frontend hosting |

---

## 🔄 CI/CD Pipeline

```
Pull Request
    └── sonarqube job
            ├── Install uv
            ├── make check (all exercises)
            │       ├── ruff check
            │       ├── mypy
            │       └── pytest --cov → coverage.xml
            └── SonarCloud scan

Push to main
    ├── sonarqube job
    └── deploy_registry job (matrix: all exercises)
            ├── docker build (multi-stage)
            └── docker push → ghcr.io
```

### SonarCloud Quality Gate
- Security Rating: **A** required
- Coverage: **≥ 80%** required on new code
- Duplications: **≤ 3%** required

---

## 🚀 Running Locally

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Docker
- make

### Run all exercises

```bash
make check
```

### Run a single exercise

```bash
cd exercise/dictionary
make check
```

See each exercise's README for individual API usage and Docker instructions.

---

## 🤖 AI-Powered Documentation

On every merge to `main`, a GitHub Action sends the PR diff to the Claude API, which automatically updates `CHANGELOG.md` with a structured entry describing what changed and any architectural decisions made.

---

## 🗺️ Roadmap

- [x] Session 1 — TDD, CI/CD, SonarCloud, Docker, AI docs
- [ ] Session 2 — k3d local cluster + Ansible provisioning
- [ ] Session 3 — AWS serverless stack + frontend

---

## 📋 Changelog

See [CHANGELOG.md](./CHANGELOG.md) for the full history of changes.

---
## 🤝 Contributing

This repository uses **Squash Merge** for all pull requests.

PR titles must follow [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | When to use | Version bump |
|---|---|---|
| `feat:` | New feature or endpoint | minor |
| `fix:` | Bug fix | patch |
| `chore:` | Maintenance, deps, config | patch |
| `docs:` | Documentation only | patch |
| `ci:` | Pipeline changes | patch |
| `feat!:` | Breaking change | major |

**Example:** `feat(spending-calculator): add tax calculation endpoint`
---
## 👤 Author

**Joseph Rojas**
IEEE Colombia — Student Activities Committee & Young Professionals
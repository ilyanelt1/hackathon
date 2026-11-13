# MTS Intern Dashboard

[![CI](https://github.com/ilyanelt1/hackathon/actions/workflows/ci.yml/badge.svg)](https://github.com/ilyanelt1/hackathon/actions/workflows/ci.yml)

Интеллектуальный аналитический дашборд программы стажировок МГТС. Проект помогает HR и руководителям отслеживать динамику оценок, анализировать обратную связь, выявлять риски и получать AI-инсайты.

## Текущий статус

Создана основа MVP: FastAPI backend, health endpoint, PostgreSQL 17 в Docker Compose, автоматические тесты и CI. Доменная функциональность, frontend, ETL и AI-модули реализуются последовательно отдельными задачами.

## Структура

```text
.
├── backend/
│   ├── app/main.py
│   └── Dockerfile
├── docs/architecture.md
├── tests/test_health.py
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Стек

- Python 3.13, FastAPI, Uvicorn
- PostgreSQL 17
- Docker Compose
- Ruff, Pre-commit, Pytest, GitHub Actions

## Быстрый запуск

Требуются Docker Engine/Desktop и Docker Compose v2.

```bash
cp .env.example .env
docker compose up --build -d
```

Проверка backend: `curl http://localhost:8000/health`

Ожидаемый ответ: `{"status":"ok"}`

Остановка: `docker compose down`

## Локальная разработка

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest -q
pre-commit install
pre-commit run --all-files
```

## CI

GitHub Actions запускает четыре независимые job при Pull Request в main и push:

| Job | Проверка |
|---|---|
| Ruff | Линтинг и проверка форматирования Python |
| Pre-commit | Все настроенные Git hooks |
| Pytest | Автоматические тесты |
| Docker test | Проверка Compose, сборка backend и smoke test /health |

## Документация

- [Архитектура](docs/architecture.md)

## Безопасность

Не коммитьте .env, токены, пароли и реальные персональные данные. Для локальной разработки используйте собственные значения из .env.example. AI-результаты должны быть вспомогательной аналитикой, а не единственным основанием кадровых решений.

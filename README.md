# MTS Intern Dashboard

[![CI](https://github.com/ilyanelt1/mts-intern-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/ilyanelt1/mts-intern-dashboard/actions/workflows/ci.yml)

Интеллектуальный аналитический дашборд программы стажировок МГТС. Проект предназначен для HR и руководителей: помогает отслеживать динамику оценок стажёров, анализировать обратную связь, выявлять риски и получать AI-инсайты.

## Возможности MVP

- **Overview:** ключевые показатели, динамика оценок, NPS, участие в опросах и количество рисков.
- **Стажёры:** список, поиск, фильтрация и пагинация.
- **Карточка стажёра:** история оценок, комментарии, сравнение с группой и наставником.
- **AI-анализ:** тональность, тематическая классификация и суммаризация комментариев.
- **Риск-скоринг:** объяснимые оценки риска с причинами и весами.
- **Экспорт:** подготовка отчётов для HR (планируемое расширение).

AI-результаты являются вспомогательной аналитикой и требуют проверки человеком. Они не должны использоваться как единственное основание для кадровых решений.

## Архитектура

Проект организован как монорепозиторий:

```text
mts-intern-dashboard/
├── backend/          # Backend API и бизнес-логика
├── frontend/         # Web-интерфейс
├── etl/              # Загрузка и обработка данных
├── docs/             # Архитектура и документация
├── scripts/          # Seed, backfill и служебные скрипты
├── .github/
│   └── workflows/    # CI GitHub Actions
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

### Технологический стек

| Компонент | Технологии |
|---|---|
| Backend | Python, FastAPI, Pydantic |
| ORM и миграции | SQLAlchemy, Alembic |
| Database | PostgreSQL |
| Frontend | React, TypeScript, Vite |
| Работа с API | TanStack Query, OpenAPI |
| ETL | Python, SQL |
| AI | Анализ тональности, классификация тем, суммаризация |
| Контейнеризация | Docker, Docker Compose |
| CI | GitHub Actions, Ruff, Pre-commit, Pytest |

## Основные сущности данных

- `Intern` — стажёр.
- `Mentor` — наставник.
- `Group` — группа стажёров.
- `Survey`, `Question` — опросы и вопросы.
- `Response`, `Answer` — ответы на опросы.
- `CommentAnalysis` — результаты AI-анализа комментариев.
- `RiskFlag` — объяснимые флаги риска.
- `MartInternMonth`, `MartGroupMonth` — аналитические витрины по месяцам.

## Локальный запуск

### Требования

- Git
- Docker Desktop или Docker Engine
- Docker Compose v2
- Python — версия будет зафиксирована в конфигурации backend
- Node.js — версия будет зафиксирована в конфигурации frontend

### Настройка

```bash
git clone https://github.com/ilyanelt1/mts-intern-dashboard.git
cd mts-intern-dashboard

cp .env.example .env
```

Заполни переменные окружения в `.env`. Не добавляй реальные секреты в Git.

### Запуск

```bash
docker compose up --build
```

Проверка состояния backend:

```bash
curl http://localhost:8000/health
```

Ожидаемый ответ:

```json
{
  "status": "ok"
}
```

Конкретные адреса frontend, backend и PostgreSQL, а также команды миграций будут уточнены в документации по мере реализации соответствующих задач.

## CI / Quality gates

GitHub Actions должен запускать независимые проверки:

| Job | Назначение |
|---|---|
| Ruff | Проверка Python-кода и форматирования |
| Pre-commit | Запуск настроенных Git hooks |
| Pytest | Unit- и интеграционные тесты |
| Docker test | Проверка Docker Compose и сборки образов |

Проверки выполняются при Pull Request и push в основную ветку. Изменения должны проходить CI до принятия в `main`.

## План разработки

Все задачи MVP объединяются в один GitHub milestone:

**MVP: Интеллектуальный дашборд стажировок МГТС**

Работа организуется через GitHub Issues и Kanban Project board:

`Backlog → Ready → In Progress → Review → Done`

Приоритеты и направления разработки задаются GitHub Labels.

## Документация

По мере реализации будут добавлены:

- `docs/architecture.md` — архитектура системы.
- `docs/data-model.md` — модель данных и ER-диаграмма.
- `docs/integration.md` — интеграция с сервисом анкетирования.
- `docs/ai-eval.md` — оценка качества AI-моделей.
- `docs/risk-scoring.md` — правила и пороги риск-скоринга.
- `docs/demo.md` — сценарий демонстрации MVP.

## Безопасность

- Секреты хранятся в переменных окружения.
- Доступ к API защищается авторизацией и ролями.
- Webhook-запросы должны проходить проверку подписи.
- Персональные данные стажёров не должны попадать в публичные логи.
- AI-результаты сопровождаются объяснениями и ограничениями.

## Статус проекта

Проект находится на этапе планирования и реализации MVP. Актуальный прогресс отслеживается через GitHub Issues, milestone и Project board.

---

**MTS Intern Dashboard** — аналитика, которая помогает замечать тенденции и вовремя поддерживать стажёров.

# AGENTS.md

## Hexlet project (ai-for-developers-project-386)

- **Не редактировать** `.github/workflows/hexlet-check.yml` — автоматически генерируется Hexlet и возвращается при каждой проверке.
- Пока нет Python, JS или других исходных файлов; репозиторий представляет собой заглушку, содержащую только README.md и CI.
- Тесты запускаются автоматически через CI Hexlet при каждом нажатии (не настраивается локально).
- Локальные инструменты сборки/тестирования/проверки не настроены. Добавьте инструменты, необходимые для выполнения задачи.
— Значок GitHub в README.md указывает на статус Hexlet CI.
- Ответы только на русском языке.

## Подход к разработке

Проект выполняется в подходе **Design First**:

- Сначала фиксируем поведение системы и API-контракт, и только потом переходим к реализации.
- Фронтенд и бэкенд реализуются раздельно и взаимодействуют через API-контракт.
- Контракт в этом шаге задает границу между частями приложения и остается единым источником правды для реализации.
- **Спецификация API**: `/home/pavel/My_folder/my_works/Hexlet/ai-for-developers-project-386` — единый источник правды для обеих частей приложения.
- **Исследование cal.com**: `/home/pavel/My_folder/my_works/Hexlet/ai-for-developers-project-386/docs/research-calcom.md` — используем для ориентира при разработке.

## Стек разработки

- **Контракт**: TypeSpec (`spec/main.tsp`) → компиляция в OpenAPI 3.1 (`spec/tsp-output/openapi.yaml`).
- **Бэкенд**: Python 3.12+, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic.
- **БД**: SQLite (единственная, время — UTC).
- **Auth**: JWT (хост); страница бронирования публична.
- **Тесты**: pytest + httpx + factory_boy. Качество: ruff + mypy. Менеджер: uv.
- **Фронтенд**: Next.js + TypeScript (реализуется позже).
- **Инфраструктура**: `Makefile` с задачами: `install`, `compile-spec`, `lint`, `test`, `dev`, `migrate`.

## Работа с Git

- запрещены любые операции с Git

## Формат коммитов (Conventional Commits)

Все коммиты (включая те, которые делает агент) должны соответствовать спецификации [Conventional Commits](https://www.conventionalcommits.org/):

```
<тип>(<область>): <описание>

[опциональное тело]

[опциональные footer]
```

**Типы:** `feat`, `fix`, `chore`, `docs`, `test`, `refactor`, `ci`, `build`, `style`, `perf`

**Примеры:**
- `feat: add Playwright e2e tests for booking flow`
- `fix(api): correct slot time filtering`
- `chore: update Docker Compose configuration`
- `docs: update README with CI instructions`
- `test(e2e): add booking scenario test`
- `ci: add GitHub Actions workflow for e2e`

**Области (scope):** `api`, `frontend`, `backend`, `docker`, `e2e`, `spec` — по усмотрению.

Этот формат используется release-please для автоматического определения версии (semver) и формирования CHANGELOG.
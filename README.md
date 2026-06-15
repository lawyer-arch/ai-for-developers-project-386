### Hexlet tests and linter status:
[![Actions Status](https://github.com/lawyer-arch/ai-for-developers-project-386/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lawyer-arch/ai-for-developers-project-386/actions)

## Запуск

### Docker (рекомендуется)

```bash
docker compose up --build
```

- Фронтенд: http://localhost:3000
- Бэкенд (Swagger): http://localhost:8000/docs
- Демо-пользователь: `demo`, расписание: пн–пт 09:00–17:00, тип встречи: `consult`

Остановка:

```bash
docker compose down
```

### Локально (2 терминала)

```bash
# Терминал 1 — бэкенд
make dev

# Терминал 2 — фронтенд
make frontend-dev
```

Seed-данные (для сквозного сценария бронирования):

```bash
make seed
```

### Полезные команды

| Команда | Описание |
|---------|----------|
| `make install` | Установка зависимостей |
| `make test` | Тесты бэкенда |
| `make frontend-test` | Тесты фронтенда |
| `make lint` | Линтер бэкенда |
| `make e2e-install` | Установка Playwright и браузера |
| `make e2e` | E2E-тесты (Playwright) |
| `make docker-build` | Сборка Docker-образов |
| `make docker-up` | Запуск в фоне |
| `make docker-down` | Остановка |
| `make docker-logs` | Логи |

## E2E-тесты (Playwright)

Интеграционные тесты проверяют основной сценарий бронирования в реальном браузере:

1. Открытие главной страницы со списком типов встреч
2. Переход на страницу бронирования
3. Выбор даты и слота
4. Заполнение формы и подтверждение бронирования

### Запуск

```bash
# Установка (один раз)
make e2e-install

# Запуск (приложение должно быть поднято)
make e2e
```

Или вручную:

```bash
npm ci
npx playwright install --with-deps chromium
npx playwright test
```

### Отчёт

После запуска откройте HTML-отчёт:

```bash
npx playwright show-report
```

## CI/CD

### GitHub Actions (e2e)

При каждом пуше в любую ветку автоматически запускаются интеграционные тесты:

1. Сборка и запуск Docker Compose (backend + frontend)
2. Ожидание готовности сервисов
3. Запуск Playwright-тестов
4. Загрузка отчёта при ошибках

### Release-please

При пуше в `main` автоматически создаётся/обновляется release-PR с changelog и предложением новой версии (semver). После мёржа release-PR создаётся GitHub Release.

Формат коммитов: [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `chore:`, `docs:`, `test:`, `ci:` и др.).

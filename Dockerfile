FROM python:3.12-slim as builder

# Установка Poetry и настройка переменных окружения
RUN pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Копируем только файлы конфигурации
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости без разработки
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Создаем финальный образ
FROM python:3.12-slim

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

# Копируем виртуальное окружение из сборочного образа
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Копируем приложение
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.9 as requirements-stage

WORKDIR /tmp

# Install Poetry with specific version and configure it
RUN pip install poetry==1.4.2 && \
    poetry config virtualenvs.create false

COPY ./backend/app/pyproject.toml ./backend/app/poetry.lock* /tmp/

# Make sure we're in the directory with pyproject.toml
WORKDIR /tmp
# Export dependencies with additional flags to ensure success
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --no-interaction

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/app /app

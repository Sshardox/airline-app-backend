FROM python:3.11 as requirements-stage

WORKDIR /tmp

# Copy requirements file directly instead of using poetry
COPY ./backend/requirements.txt /tmp/requirements.txt

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt && \
    # Install bcrypt for passlib with specific version
    pip install bcrypt==4.0.1

COPY ./backend/app /app

# Configure environment variables for database connection
ENV DATABASE_USERNAME=postgres \
    DATABASE_PASSWORD=123123 \
    DATABASE_HOST=db \
    DATABASE_PORT=5432 \
    DATABASE_NAME=mydb

# Airline Booking Application

## Authors
- Juan David Orozco 2019214012
- Yeiker Ruiz 2019214069

## Project Structure
The project is organized as follows:
- `backend/`: Contains the backend application code
  - `app/`: Contains the FastAPI application
    - `auth/`: Authentication module
    - `booking/`: Booking module
    - `catalog/`: Catalog module
    - `core/`: Core functionality
    - `database/`: Database models and connection
    - `user/`: User management module
    - `main.py`: Main application entry point
- `Dockerfile`: Docker configuration for the application
- `docker-compose.yml`: Docker Compose configuration for the application and database

## Running the Application

### Using Docker (Recommended)
The easiest way to run the application is using Docker:

```bash
docker-compose up -d
```

This will start the application and the PostgreSQL database. The application will be available at http://localhost:80.

### Local Development Setup

#### Prerequisites
- Python 3.9 or higher
- PostgreSQL database
- Poetry (for dependency management)

#### Installation Steps

1. Install Poetry (if not already installed):
   ```bash
   pip install poetry
   ```

2. Navigate to the backend/app directory:
   ```bash
   cd backend/app
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Configure environment variables (optional):
   By default, the application uses these database settings:
   - Username: postgres
   - Password: 123123
   - Host: localhost
   - Port: 6548
   - Database name: mydb

   You can override these by setting environment variables:
   - DATABASE_USERNAME
   - DATABASE_PASSWORD
   - DATABASE_HOST
   - DATABASE_PORT
   - DATABASE_NAME
   - DATABASE_URI (if you want to set the full URI directly)

5. Run database migrations:
   ```bash
   cd backend/app
   poetry run alembic upgrade head
   ```

6. Start the application:
   ```bash
   cd backend/app
   poetry run uvicorn main:app --reload
   ```

   The application will be available at http://localhost:8000.

## API Documentation
Once the application is running, you can access the API documentation at:
- Swagger UI: http://localhost:80/docs (Docker) or http://localhost:8000/docs (local)
- ReDoc: http://localhost:80/redoc (Docker) or http://localhost:8000/redoc (local)

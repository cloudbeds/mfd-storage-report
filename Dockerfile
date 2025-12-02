FROM python:3.11-slim

# Build time args
ARG APP_DIR=/python-restapi-template

WORKDIR ${APP_DIR}

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH="${PYTHONPATH}:/python-restapi-template"

# Needed for Fast API
ENV WATCHFILES_FORCE_POLLING=true

# Copy project
COPY pyproject.toml ${APP_DIR}/pyproject.toml
COPY app ${APP_DIR}/app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev --no-interaction --no-ansi

# Copy project
COPY app ${APP_DIR}

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-slim

# Install dependencies
RUN apt-get update && apt-get install --no-install-recommends -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    export PATH="$HOME/.local/bin:$PATH"

# Set environment variable for Poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# Create a working directory
WORKDIR /opt/pysetup

# Copy dependency files
COPY poetry.lock pyproject.toml ./

# Install dependencies
RUN /root/.local/bin/poetry install --no-dev

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

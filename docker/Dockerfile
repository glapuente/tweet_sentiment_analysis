FROM python:3.12-slim

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# set working directory
WORKDIR /app

# copy dependencies
COPY pyproject.toml uv.lock ./

# install dependencies
RUN uv sync --frozen --no-install-project

# copy application code and static files
COPY src/ ./src/
COPY data/ ./data/

# install the project
RUN uv sync --frozen --no-dev

# make the virtualenv available
ENV PATH="/app/.venv/bin:$PATH"

FROM python:3.12-slim

# install Java (required by PySpark)
RUN apt-get update && \
    apt-get install -y --no-install-recommends openjdk-17-jre-headless && \
    rm -rf /var/lib/apt/lists/*

# set Java environmental variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

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

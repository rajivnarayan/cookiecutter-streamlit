FROM python:3.12-slim-bookworm AS builder
# Copy uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# Change working directory
WORKDIR /app

ENV PATH="/root/.local/bin:${PATH}"

# Copy the project into the image
ADD . /app

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes git && \    
    uv sync --frozen --no-install-project && \
    uv sync --frozen

ENTRYPOINT ["uv", "run", "streamlit", "run", "/app/app.py"]

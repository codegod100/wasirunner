FROM python:3.10-slim
RUN apt update && apt install -y curl
RUN curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
ENV PATH=/root/.local/bin:$PATH
WORKDIR /workspace/wasirunner
COPY pyproject.toml pyproject.toml
COPY pdm.lock pdm.lock
COPY README.md README.md
COPY . .
RUN pdm install
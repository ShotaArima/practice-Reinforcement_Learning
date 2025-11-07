FROM ghcr.io/astral-sh/uv:debian

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends git build-essential pkg-config && \
    rm -rf /var/lib/apt/lists/*



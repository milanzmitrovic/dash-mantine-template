
# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Keeps Python from generating .pyc files in the container.
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Ensure installed tools can be executed out of the box
ENV UV_TOOL_BIN_DIR=/usr/local/bin


# Creates a non-root user with an explicit UID and
# adds permission to access the /app folder.
RUN adduser -u 5678 --disabled-password --gecos "" appuser \
     && chown -R appuser /app


# Copy only dependency files
# necessary to install dependencies.
COPY pyproject.toml uv.lock /app/

# Install dependencies (no project)
# It is important to install dependencies
# here, before copying all project files,
# bc otherwise dependencies would be
# fetched from internet on every build.
RUN uv sync --locked --no-install-project --no-dev


# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

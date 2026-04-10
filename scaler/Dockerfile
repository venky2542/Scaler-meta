FROM python:3.10

WORKDIR /app

COPY . .

# Install uv (required for OpenEnv)
RUN pip install uv

# Install project using uv (uses uv.lock properly)
RUN uv pip install --system .

EXPOSE 7860

# Correct OpenEnv server entrypoint
CMD ["python", "-m", "server.app"]
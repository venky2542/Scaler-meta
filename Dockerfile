FROM python:3.10

WORKDIR /app

# 1. Install uv
RUN pip install uv

# 2. Copy the configuration files first (best practice for caching)
COPY pyproject.toml uv.lock ./

# 3. Install dependencies exactly as defined in uv.lock
# We use --system because we are inside a Docker container
RUN uv pip install --system -r pyproject.toml

# 4. Copy the rest of your code (including the my_env folder)
COPY . .

# Add this line before your CMD
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Ensure your CMD points to the correct location
CMD ["uvicorn", "my_env.app:app", "--host", "0.0.0.0", "--port", "7860"]

EXPOSE 7860

# 6. Correct entrypoint for the "Multi-mode" requirement
# IMPORTANT: Point to the 'app' object inside 'my_env/app.py'
CMD ["uvicorn", "my_env.app:app", "--host", "0.0.0.0", "--port", "7860"]

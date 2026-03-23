FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY recipe_normalizer/ recipe_normalizer/

ENTRYPOINT ["python", "-m", "recipe_normalizer"]

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY recipe_normalizer/ recipe_normalizer/

ENTRYPOINT ["python", "-m", "recipe_normalizer"]

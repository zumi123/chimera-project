FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install poetry || true
RUN pip install pytest jsonschema
COPY . /app
CMD ["pytest", "-q"]

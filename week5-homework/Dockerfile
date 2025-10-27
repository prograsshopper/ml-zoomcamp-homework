FROM agrigorev/zoomcamp-model:2025
WORKDIR /code

COPY pyproject.toml .
RUN pip install uv && uv sync

COPY main.py .
ENTRYPOINT ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9696"]

FROM python:3.11-slim

WORKDIR /app

# Instala poetry
RUN pip install --no-cache-dir poetry

# Copia archivos de dependencias
COPY pyproject.toml poetry.lock* ./

# Configura poetry
RUN poetry config virtualenvs.create false

# Instala solo dependencias
RUN poetry install --no-interaction --no-ansi --no-root

# Copia el código
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
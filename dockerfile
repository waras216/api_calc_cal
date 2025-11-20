FROM python:3.12-slim

# Dependencias del sistema para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Crea directorio
WORKDIR /app

# Copia requirements
COPY requirements.txt .

# Instala pip y dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Puerto para Django
EXPOSE 8000

# Comando de arranque
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

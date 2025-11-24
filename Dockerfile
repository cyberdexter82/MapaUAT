# Usa una imagen de Python de Linux ya lista
FROM python:3.10-slim

# Instala librerías de sistema necesarias (ejemplo: para compilación de Pandas/Numpy)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    # Si tu numpy/pandas falla, puedes necesitar más paquetes aquí
    && rm -rf /var/lib/apt/lists/*

# Configura la carpeta de trabajo
WORKDIR /home/site/wwwroot

# Copia los archivos de dependencia e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código
COPY . .

# Comando de inicio del servidor Gunicorn
# (Debe coincidir con lo que usaste: gunicorn config.wsgi)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]
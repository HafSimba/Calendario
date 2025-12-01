FROM python:3.11-slim

# Metadata
LABEL maintainer="calendario-presenze"
LABEL description="Calendario Presenze/Assenze - Docker Container"

# Imposta directory di lavoro
WORKDIR /app

# Copia file requirements e installa dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia applicazione
COPY app.py .
COPY templates/ templates/
COPY static/ static/

# Crea directory per database
RUN mkdir -p data

# Esponi porta Flask
EXPOSE 5000

# Variabili ambiente
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/stats')" || exit 1

# Comando di avvio
CMD ["python", "app.py"]

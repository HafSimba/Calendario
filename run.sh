#!/bin/bash
# Script di avvio per Linux/macOS

cd "$(dirname "$0")"

# Controlla se esiste virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creazione ambiente virtuale..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

echo ""
echo "🚀 Avvio Calendario Presenze..."
echo "📅 Apri il browser su: http://127.0.0.1:5000"
echo ""

python app.py

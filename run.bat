@echo off
REM Script di avvio per Windows

cd /d "%~dp0"

REM Controlla se esiste virtual environment
if not exist "venv" (
    echo Creazione ambiente virtuale...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo.
echo Avvio Calendario Presenze...
echo Apri il browser su: http://127.0.0.1:5000
echo.

python app.py
pause

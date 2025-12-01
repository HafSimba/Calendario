@echo off
chcp 65001 >nul
REM Script di avvio automatico per Windows - Calendario Presenze

cd /d "%~dp0"

echo ================================================================
echo   CALENDARIO PRESENZE/ASSENZE - Avvio Automatico
echo ================================================================
echo.

REM Verifica se Python è installato
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRORE] Python non è installato su questo PC!
    echo.
    echo Vuoi installare Python automaticamente? ^(S/N^)
    set /p INSTALL_PYTHON="Risposta: "
    
    if /i "%INSTALL_PYTHON%"=="S" (
        echo.
        echo Apertura pagina download Python...
        start https://www.python.org/downloads/
        echo.
        echo ISTRUZIONI:
        echo 1. Scarica Python dalla pagina aperta
        echo 2. Durante l'installazione, SELEZIONA "Add Python to PATH"
        echo 3. Completa l'installazione
        echo 4. Riavvia questo script
        echo.
        pause
        exit /b 1
    ) else (
        echo.
        echo Installazione annullata. L'applicazione richiede Python per funzionare.
        pause
        exit /b 1
    )
)

echo [OK] Python trovato: 
python --version
echo.

REM Verifica pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [AVVISO] pip non trovato. Installo pip...
    python -m ensurepip --default-pip
    if %errorlevel% neq 0 (
        echo [ERRORE] Impossibile installare pip.
        pause
        exit /b 1
    )
    echo [OK] pip installato con successo
    echo.
)

REM Controlla se esiste virtual environment
if not exist "venv" (
    echo ----------------------------------------------------------------
    echo   PRIMA ESECUZIONE - Configurazione Ambiente
    echo ----------------------------------------------------------------
    echo.
    echo Questa applicazione necessita di installare alcune dipendenze.
    echo Verranno scaricati circa 5-10 MB di file.
    echo.
    set /p INSTALL_DEPS="Procedere con l'installazione? (S/N): "
    
    if /i not "%INSTALL_DEPS%"=="S" (
        echo.
        echo Installazione annullata.
        pause
        exit /b 1
    )
    
    echo.
    echo [1/3] Creazione ambiente virtuale...
    python -m venv venv
    if %errorlevel% neq 0 (
        echo [ERRORE] Impossibile creare l'ambiente virtuale.
        echo Assicurati di avere i permessi necessari.
        pause
        exit /b 1
    )
    echo [OK] Ambiente virtuale creato
    
    echo.
    echo [2/3] Attivazione ambiente...
    call venv\Scripts\activate.bat
    
    echo.
    echo [3/3] Installazione dipendenze (Flask)...
    python -m pip install --upgrade pip >nul 2>&1
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERRORE] Impossibile installare le dipendenze.
        echo Verifica la connessione internet.
        pause
        exit /b 1
    )
    echo [OK] Dipendenze installate con successo
    echo.
    echo ================================================================
    echo   CONFIGURAZIONE COMPLETATA!
    echo ================================================================
    echo.
) else (
    call venv\Scripts\activate.bat
)

REM Verifica database
if not exist "data" (
    echo Creazione cartella database...
    mkdir data
)

echo.
echo ================================================================
echo   AVVIO CALENDARIO PRESENZE
echo ================================================================
echo.
echo  ^> Server in avvio su: http://127.0.0.1:5000
echo  ^> Premi CTRL+C per fermare il server
echo  ^> Chiudi questa finestra per terminare
echo.
echo ================================================================
echo.

REM Attendi un attimo e apri il browser
timeout /t 2 /nobreak >nul
start http://127.0.0.1:5000

REM Avvia l'applicazione
python app.py

REM Se l'app si chiude, mostra un messaggio
echo.
echo.
echo ================================================================
echo   Server arrestato
echo ================================================================
pause

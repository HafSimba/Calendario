@echo off
chcp 65001 >nul
REM Menu principale per tutte le opzioni di build e distribuzione

:MENU
cls
echo ================================================================
echo   📦 CALENDARIO PRESENZE - Menu Distribuzione
echo ================================================================
echo.
echo   Scegli un'opzione:
echo.
echo   1. 🚀 Avvia applicazione (normale)
echo   2. 📦 Crea eseguibile Windows (.exe)
echo   3. 📦 Crea pacchetto ZIP distribuzione
echo   4. 🐳 Build Docker image
echo   5. 📄 Apri guida distribuzione
echo   6. ❌ Esci
echo.
echo ================================================================

set /p choice="Inserisci numero opzione: "

if "%choice%"=="1" goto RUN_APP
if "%choice%"=="2" goto BUILD_EXE
if "%choice%"=="3" goto CREATE_ZIP
if "%choice%"=="4" goto BUILD_DOCKER
if "%choice%"=="5" goto OPEN_GUIDE
if "%choice%"=="6" goto EXIT

echo.
echo ❌ Opzione non valida!
timeout /t 2 >nul
goto MENU

:RUN_APP
echo.
echo ================================================================
echo   🚀 Avvio Applicazione
echo ================================================================
call run.bat
goto MENU

:BUILD_EXE
echo.
echo ================================================================
echo   📦 Creazione Eseguibile Windows
echo ================================================================
echo.
echo Questo processo richiede 2-3 minuti...
echo.
pause

REM Verifica Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python non installato!
    echo Installa Python da: https://www.python.org/downloads/
    pause
    goto MENU
)

REM Attiva venv se esiste
if exist "venv\Scripts\activate.bat" call venv\Scripts\activate.bat
if exist ".venv\Scripts\activate.bat" call .venv\Scripts\activate.bat

REM Installa PyInstaller
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo Installazione PyInstaller...
    pip install pyinstaller
)

REM Build
echo.
echo Compilazione in corso...
python build_exe.py

if exist "dist\CalendarioPresenze.exe" (
    echo.
    echo ✅ Eseguibile creato: dist\CalendarioPresenze.exe
    echo.
    set /p open_folder="Aprire cartella dist? (S/N): "
    if /i "%open_folder%"=="S" explorer dist
) else (
    echo ❌ Errore durante la compilazione!
)

pause
goto MENU

:CREATE_ZIP
echo.
echo ================================================================
echo   📦 Creazione Pacchetto ZIP
echo ================================================================
echo.
python create_package.py
pause
goto MENU

:BUILD_DOCKER
echo.
echo ================================================================
echo   🐳 Build Docker Image
echo ================================================================
echo.

REM Verifica Docker
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker non installato!
    echo Installa Docker Desktop da: https://www.docker.com/products/docker-desktop
    pause
    goto MENU
)

echo Build immagine Docker...
docker build -t calendario-presenze .

if %errorlevel% equ 0 (
    echo.
    echo ✅ Immagine Docker creata: calendario-presenze
    echo.
    echo Per avviare:
    echo   docker run -p 5000:5000 calendario-presenze
    echo.
    echo Oppure con docker-compose:
    echo   docker-compose up -d
) else (
    echo ❌ Errore durante il build!
)

pause
goto MENU

:OPEN_GUIDE
echo.
echo Apertura GUIDA_DISTRIBUZIONE.md...
if exist "GUIDA_DISTRIBUZIONE.md" (
    start notepad GUIDA_DISTRIBUZIONE.md
) else (
    echo ❌ File GUIDA_DISTRIBUZIONE.md non trovato!
)
timeout /t 2 >nul
goto MENU

:EXIT
echo.
echo Arrivederci!
timeout /t 1 >nul
exit /b 0

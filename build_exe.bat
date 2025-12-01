@echo off
REM Script per creare eseguibile Windows standalone
REM Richiede: Python con pip installato

echo ================================================================
echo   BUILD ESEGUIBILE WINDOWS - Calendario Presenze
echo ================================================================
echo.

REM Attiva ambiente virtuale se esiste
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Installa PyInstaller se necessario
pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo [1/2] Installazione PyInstaller...
    pip install pyinstaller
) else (
    echo [1/2] PyInstaller trovato
)

echo.
echo [2/2] Compilazione eseguibile...
echo Questo richiederà 2-3 minuti. Attendi...
echo.

REM Pulizia
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist CalendarioPresenze.spec del CalendarioPresenze.spec

REM Build
pyinstaller --onefile --name=CalendarioPresenze --add-data "templates;templates" --add-data "static;static" --hidden-import=flask --hidden-import=sqlite3 --clean app.py

if %errorlevel% neq 0 (
    echo.
    echo [ERRORE] Compilazione fallita!
    pause
    exit /b 1
)

REM Copia file necessari
echo.
echo Copia file di supporto...
xcopy /E /I /Y templates dist\templates >nul
xcopy /E /I /Y static dist\static >nul
if exist esempio_import.csv copy esempio_import.csv dist\ >nul
if exist ISTRUZIONI.txt copy ISTRUZIONI.txt dist\ >nul
if exist README.md copy README.md dist\ >nul
if not exist dist\data mkdir dist\data

echo.
echo ================================================================
echo   BUILD COMPLETATO!
echo ================================================================
echo.
echo Eseguibile: dist\CalendarioPresenze.exe
echo.
echo Per testare: cd dist ^&^& CalendarioPresenze.exe
echo Per distribuire: comprimi la cartella "dist" in un ZIP
echo.
pause

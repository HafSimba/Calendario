# 📦 Guida Completa alla Distribuzione
## Calendario Presenze/Assenze - Tutti i Metodi di Installazione

---

## 🎯 **METODO 1: Eseguibile Windows Standalone (CONSIGLIATO)**

### ✅ **Vantaggi:**
- ✅ Nessuna installazione richiesta
- ✅ Non serve Python
- ✅ Un singolo file .exe
- ✅ Funziona da chiavetta USB
- ✅ Dimensione: ~30-40 MB

### 📝 **Come Creare l'Eseguibile:**

#### Opzione A - Script Automatico (Semplice)
```batch
1. Apri terminale nella cartella Calendario
2. Esegui: python build_exe.py
   oppure: build_exe.bat (Windows)
3. Attendi 2-3 minuti
4. Trovi l'eseguibile in: dist/CalendarioPresenze.exe
```

#### Opzione B - Comando Manuale
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name=CalendarioPresenze \
    --add-data "templates;templates" \
    --add-data "static;static" \
    --hidden-import=flask \
    --hidden-import=sqlite3 \
    app.py
```

### 📦 **Distribuzione:**
1. Comprimi la cartella `dist/` in un file ZIP
2. Rinomina: `CalendarioPresenze_v1.0_Portable.zip`
3. Invia agli utenti
4. Loro devono solo:
   - Estrarre il ZIP
   - Doppio click su `CalendarioPresenze.exe`
   - Fatto! 🎉

### ⚠️ **Problemi Comuni:**

**Windows Defender lo blocca?**
```
→ Normale per app non firmate digitalmente
→ Click su "Maggiori informazioni" → "Esegui comunque"
→ È un falso positivo comune con PyInstaller
```

**Antivirus lo elimina?**
```
→ Aggiungi eccezione/esclusione per CalendarioPresenze.exe
→ Oppure disabilita temporaneamente per testare
```

**Errore "templates not found"?**
```
→ Assicurati che le cartelle templates/ e static/ 
  siano nella stessa directory dell'eseguibile
```

---

## 🎯 **METODO 2: Script Python con Auto-Install (Attuale)**

### ✅ **Vantaggi:**
- ✅ Installazione automatica di Python e dipendenze
- ✅ Dimensione minima (~2 MB)
- ✅ Più facile da aggiornare
- ✅ Cross-platform (Windows/Linux/macOS)

### 📝 **Come Usare:**
```batch
Windows: Doppio click su run.bat
Linux/macOS: ./run.sh
```

### 📦 **Distribuzione:**
1. Comprimi l'intera cartella `Calendario/`
2. Invia agli utenti
3. Loro eseguono `run.bat` (Windows) o `run.sh` (Linux/macOS)
4. Al primo avvio installerà tutto automaticamente

### ⚠️ **Problemi Comuni:**

**"Python non trovato"?**
```
→ Lo script chiederà di installare Python
→ Aprirà automaticamente python.org/downloads
→ Durante installazione: seleziona "Add Python to PATH"
```

**"pip install fallito"?**
```
→ Verifica connessione internet
→ Oppure usa proxy: set HTTP_PROXY=http://proxy:8080
→ Oppure scarica manualmente: pip download Flask
```

---

## 🎯 **METODO 3: Docker Container (Server/Multi-utente)**

### ✅ **Vantaggi:**
- ✅ Isolamento completo
- ✅ Multi-piattaforma
- ✅ Deploy su server
- ✅ Facile aggiornamento

### 📝 **Setup:**

#### 1. Crea Dockerfile:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### 2. Crea docker-compose.yml:
```yaml
version: '3.8'
services:
  calendario:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

#### 3. Avvia:
```bash
docker-compose up -d
```

### 📦 **Distribuzione:**
```bash
# Crea immagine
docker build -t calendario-presenze .

# Salva immagine
docker save calendario-presenze > calendario.tar

# Su altro PC
docker load < calendario.tar
docker run -p 5000:5000 -v $(pwd)/data:/app/data calendario-presenze
```

---

## 🎯 **METODO 4: Installer Windows con Inno Setup**

### ✅ **Vantaggi:**
- ✅ Installer professionale .exe
- ✅ Icona nel menu Start
- ✅ Disinstaller automatico
- ✅ Firma digitale (opzionale)

### 📝 **Setup:**

#### 1. Scarica Inno Setup:
```
https://jrsoftware.org/isdl.php
```

#### 2. Crea script installer.iss:
```iss
[Setup]
AppName=Calendario Presenze
AppVersion=1.0
DefaultDirName={autopf}\CalendarioPresenze
DefaultGroupName=Calendario Presenze
OutputDir=installer_output
OutputBaseFilename=CalendarioPresenze_Setup

[Files]
Source: "dist\CalendarioPresenze.exe"; DestDir: "{app}"
Source: "dist\templates\*"; DestDir: "{app}\templates"; Flags: recursesubdirs
Source: "dist\static\*"; DestDir: "{app}\static"; Flags: recursesubdirs
Source: "dist\*.txt"; DestDir: "{app}"

[Icons]
Name: "{group}\Calendario Presenze"; Filename: "{app}\CalendarioPresenze.exe"
Name: "{autodesktop}\Calendario Presenze"; Filename: "{app}\CalendarioPresenze.exe"

[Run]
Filename: "{app}\CalendarioPresenze.exe"; Description: "Avvia applicazione"; Flags: postinstall nowait
```

#### 3. Compila installer:
```
1. Apri installer.iss con Inno Setup
2. Build → Compile
3. Ottieni CalendarioPresenze_Setup.exe
```

---

## 🎯 **METODO 5: Portable con Embedded Python**

### ✅ **Vantaggi:**
- ✅ Python embedded incluso
- ✅ Nessuna installazione
- ✅ Più piccolo di PyInstaller (~20 MB)
- ✅ Avvio più veloce

### 📝 **Setup:**

#### 1. Scarica Python Embeddable:
```
https://www.python.org/downloads/windows/
→ Scarica "Windows embeddable package (64-bit)"
```

#### 2. Crea struttura:
```
CalendarioPortable/
├── python/              (Python embedded estratto)
├── app.py
├── templates/
├── static/
├── requirements.txt
└── start.bat
```

#### 3. Installa dipendenze embedded:
```batch
cd python
python.exe -m pip install --target ../lib -r ../requirements.txt
```

#### 4. Crea start.bat:
```batch
@echo off
set PYTHONPATH=%~dp0lib;%~dp0
start http://127.0.0.1:5000
python\python.exe app.py
```

---

## 📊 **Comparazione Metodi**

| Metodo | Dimensione | Velocità | Facilità | Compatibilità |
|--------|-----------|----------|----------|---------------|
| PyInstaller EXE | 30-40 MB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Windows |
| Script Python | 2 MB | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Multi-OS |
| Docker | 100 MB | ⭐⭐ | ⭐⭐⭐ | Multi-OS |
| Inno Setup | 35 MB | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Windows |
| Embedded Python | 20 MB | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Windows |

---

## 🎯 **Raccomandazioni per Caso d'Uso**

### 🏢 **Utenti Non Tecnici (PC Aziendali):**
→ **METODO 1** (Eseguibile PyInstaller)
- Funziona subito
- Nessuna configurazione
- Bypass restrizioni IT

### 🎓 **Studenti/Privati:**
→ **METODO 2** (Script Python)
- Più leggero
- Facile aggiornare
- Impara Python

### 🖥️ **Server/Cloud:**
→ **METODO 3** (Docker)
- Isolamento
- Multi-utente
- Deploy automatico

### 📦 **Distribuzione di Massa:**
→ **METODO 4** (Installer)
- Professionale
- Facile disinstallare
- Aggiornamenti automatici

### 💻 **Chiavetta USB/Offline:**
→ **METODO 5** (Embedded Python)
- Più compatto
- Avvio veloce
- Zero installazione

---

## 🔧 **Troubleshooting Generale**

### Problema: "Porta 5000 già in uso"
```python
# Modifica in app.py:
if __name__ == '__main__':
    app.run(port=5001)  # Cambia porta
```

### Problema: "Database locked"
```python
# Aggiungi timeout in app.py:
conn = sqlite3.connect(DB_PATH, timeout=10)
```

### Problema: "Template not found"
```python
# Verifica percorsi in app.py:
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(BASE_DIR, 'templates')
app = Flask(__name__, template_folder=template_folder)
```

---

## 📞 **Supporto e Risorse**

- **PyInstaller Docs:** https://pyinstaller.org/
- **Docker Docs:** https://docs.docker.com/
- **Inno Setup Docs:** https://jrsoftware.org/ishelp/
- **Python Embedded:** https://docs.python.org/3/using/windows.html#embedded-distribution

---

**Buona distribuzione! 🚀**

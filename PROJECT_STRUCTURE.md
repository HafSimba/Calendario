# 📁 Struttura Progetto - Calendario Presenze

## ✅ Riorganizzazione Completata!

Il progetto è stato riorganizzato seguendo le best practice:

### 🎯 Struttura Finale

```
Calendario/
├── 📄 README.md                 # Documentazione principale
├── 📄 LICENSE                   # MIT License
├── 📄 .gitignore               # Configurazione Git
├── 📄 requirements.txt          # Dipendenze Python
├── 📄 app.py                    # Applicazione Flask
├── 🚀 run.bat                   # Launcher Windows
├── 🚀 run.sh                    # Launcher Linux/macOS
├── 🐳 Dockerfile                # Configurazione Docker
├── 🐳 docker-compose.yml        # Docker Compose
│
├── 📁 templates/                # Template HTML
│   └── index.html
│
├── 📁 static/                   # File statici (CSS/JS)
│   └── app.js
│
├── 📁 data/                     # Database
│   └── .gitkeep                # (DB creato automaticamente)
│
├── 📁 docs/                     # 📚 Documentazione completa
│   ├── GUIDA_UTENTE.md         # Manuale utente
│   ├── GUIDA_DISTRIBUZIONE.md  # Guida distribuzione
│   └── CONTRIBUTING.md         # Guida contributori
│
├── 📁 scripts/                  # 🔧 Script build e utility
│   ├── build_exe.py            # Build eseguibile Windows
│   ├── build_exe.bat           # Build batch
│   ├── create_package.py       # Crea pacchetto ZIP
│   └── menu.bat                # Menu interattivo
│
└── 📁 examples/                 # 📋 File di esempio
    └── esempio_import.csv      # Template CSV
```

### ✅ File Mantenuti (19 totali)

**Root (9):**
- README.md
- LICENSE
- .gitignore
- requirements.txt
- app.py
- run.bat
- run.sh
- Dockerfile
- docker-compose.yml

**Documentazione (3):**
- docs/GUIDA_UTENTE.md
- docs/GUIDA_DISTRIBUZIONE.md
- docs/CONTRIBUTING.md

**Script (4):**
- scripts/build_exe.py
- scripts/build_exe.bat
- scripts/create_package.py
- scripts/menu.bat

**Templates & Static (2):**
- templates/index.html
- static/app.js

**Esempi (1):**
- examples/esempio_import.csv

### ❌ File Eliminati (11)

Rimossi file ridondanti e personali:
- ❌ DISTRIBUZIONE_FACILE.txt (ridondante)
- ❌ PUSH_GITHUB.txt (ridondante)
- ❌ push_github.sh (non necessario)
- ❌ ISTRUZIONI.txt (unificato in GUIDA_UTENTE.md)
- ❌ GITHUB.md (rinominato in CONTRIBUTING.md)
- ❌ app_desktop.py (feature non completa)
- ❌ calendariotocsv.md (file personale)
- ❌ lezioni_corso.csv (dati personali)
- ❌ migrate_db.py (script temporaneo)
- ❌ requirements-build.txt (unificato in requirements.txt)
- ❌ data/calendario.db (database con dati reali)

### 📦 Vantaggi della Nuova Struttura

✅ **Organizzazione Chiara:**
- Documentazione in `docs/`
- Script in `scripts/`
- Esempi in `examples/`

✅ **Best Practice:**
- Struttura standard Python/Flask
- Separazione contenuti
- README conciso con link

✅ **Manutenibilità:**
- Facile trovare file
- Documentazione modulare
- Script isolati

✅ **Git-Friendly:**
- .gitignore ottimizzato
- Nessun file ridondante
- Struttura pulita

### 🚀 Come Usare

**Eseguire l'app:**
```bash
./run.sh  # Linux/macOS
run.bat   # Windows
```

**Build eseguibile:**
```bash
cd scripts
python build_exe.py
```

**Creare pacchetto ZIP:**
```bash
cd scripts
python create_package.py
```

**Leggere documentazione:**
- [GUIDA UTENTE](docs/GUIDA_UTENTE.md) - Manuale completo
- [GUIDA DISTRIBUZIONE](docs/GUIDA_DISTRIBUZIONE.md) - Build e deploy
- [CONTRIBUTING](docs/CONTRIBUTING.md) - Come contribuire

### 📊 Statistiche

- **Cartelle:** 6 (root + 5 sottocartelle)
- **File totali:** 19
- **Linee codice:** ~3000 (app.py + templates + static)
- **Documentazione:** ~2500 righe (3 file MD)
- **Dimensione:** <1 MB (senza venv/database)

### ✅ Prossimi Passi

1. **Commit e push su GitHub:**
   ```bash
   git add .
   git commit -m "Riorganizza progetto secondo best practice"
   git push origin main
   ```

2. **Creare release:**
   - Build eseguibile con `scripts/build_exe.py`
   - Crea ZIP con `scripts/create_package.py`
   - Carica su GitHub Releases

3. **Distribuire:**
   - Link GitHub: Codice sorgente
   - Release: Eseguibile Windows + ZIP completo
   - Docker Hub: Immagine Docker (opzionale)

---

**Progetto pronto per GitHub! 🚀**

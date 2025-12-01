# 🚀 Come Contribuire / Usare da GitHub

## 📥 Clone del Repository

```bash
git clone https://github.com/HafSimba/Calendario.git
cd Calendario
```

## 🎯 Avvio Rapido

### Windows
```bash
run.bat
```

### Linux/macOS
```bash
chmod +x run.sh
./run.sh
```

L'applicazione si installerà automaticamente al primo avvio!

## 📦 File Inclusi nel Repository

### ✅ DA INCLUDERE (già tracciati):
- `app.py` - Applicazione Flask principale
- `templates/` - Template HTML
- `static/` - File CSS/JS
- `requirements.txt` - Dipendenze Python base
- `requirements-build.txt` - Dipendenze per build
- `run.bat` / `run.sh` - Script di avvio
- `README.md` - Documentazione
- `ISTRUZIONI.txt` - Guida rapida
- `GUIDA_DISTRIBUZIONE.md` - Guida completa distribuzione
- `esempio_import.csv` - Template CSV di esempio
- `build_exe.py` / `build_exe.bat` - Script per creare eseguibile
- `create_package.py` - Script per pacchetto ZIP
- `menu.bat` - Menu interattivo
- `Dockerfile` / `docker-compose.yml` - Per deploy Docker
- `data/.gitkeep` - Mantiene cartella data/ vuota

### ❌ DA IGNORARE (già in .gitignore):
- `venv/` / `.venv/` - Ambiente virtuale (creato automaticamente)
- `data/*.db` - Database con dati utente
- `__pycache__/` - Cache Python
- `build/` / `dist/` - Output di build
- `*.zip` - Pacchetti di distribuzione
- `lezioni_corso.csv` - CSV con dati personali
- `calendariotocsv.md` - Note personali
- `migrate_db.py` - Script di migrazione temporaneo

## 🔧 Workflow Consigliato

### Per Sviluppatori
```bash
# 1. Clone
git clone https://github.com/HafSimba/Calendario.git
cd Calendario

# 2. Setup ambiente
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# oppure: .venv\Scripts\activate  # Windows

# 3. Installa dipendenze
pip install -r requirements.txt
pip install -r requirements-build.txt  # Per creare eseguibili

# 4. Avvia app
python app.py

# 5. Fai modifiche...

# 6. Commit
git add .
git commit -m "Descrizione modifiche"
git push origin main
```

### Per Utenti Finali (solo uso)
```bash
# 1. Download ZIP da GitHub
#    Code → Download ZIP

# 2. Estrai cartella

# 3. Doppio click su run.bat (Windows)
#    oppure: ./run.sh (Linux/macOS)
```

## 📋 Checklist Prima del Push

- [ ] Rimuovi dati personali (CSV con lezioni reali)
- [ ] Verifica che `data/` sia vuota (solo .gitkeep)
- [ ] Testa `run.bat` / `run.sh` su clone fresco
- [ ] Aggiorna `README.md` se hai aggiunto features
- [ ] Verifica che `.gitignore` funzioni:
  ```bash
  git status  # Non deve mostrare venv/, data/*.db, ecc.
  ```

## 🏷️ Release su GitHub

### Creare una Release
1. Build eseguibile:
   ```bash
   python build_exe.py
   ```

2. Crea pacchetto ZIP:
   ```bash
   python create_package.py
   ```

3. Su GitHub:
   - Vai a "Releases"
   - "Create new release"
   - Tag: `v1.0`
   - Titolo: `Calendario Presenze v1.0`
   - Allega: `CalendarioPresenze_v1.0_YYYYMMDD.zip`
   - Allega: `dist/CalendarioPresenze.exe` (se disponibile)

## 🤝 Contributi

Pull requests benvenute! Per modifiche importanti:
1. Apri prima una issue per discutere
2. Fork del repository
3. Crea branch: `git checkout -b feature/nuova-funzione`
4. Commit: `git commit -m "Aggiunge nuova funzione"`
5. Push: `git push origin feature/nuova-funzione`
6. Apri Pull Request

## 📝 Licenza

MIT License - Vedi file LICENSE (da creare)

## 🐛 Bug Report

Apri una issue su GitHub con:
- Descrizione del problema
- Passi per riprodurlo
- Screenshot (se applicabile)
- Sistema operativo e versione Python

# 📅 Calendario Presenze/Assenze

Applicazione web locale e portabile per tracciare le presenze e assenze alle lezioni di un corso.

## ✨ Funzionalità

- ✅ Visualizzazione calendario con tutte le lezioni
- ✅ Aggiunta, modifica ed eliminazione lezioni
- ✅ Toggle rapido presenza/assenza con un click
- ✅ Import massivo da file CSV
- ✅ Export dati in CSV
- ✅ Statistiche in tempo reale (presenze, assenze, ore totali, percentuale)
- ✅ Filtri per ricerca, mese, stato presenza
- ✅ Calcolo automatico ore dalla durata
- ✅ Database SQLite locale (portabile)
- ✅ Interfaccia moderna e responsive

## 🚀 Avvio Rapido - Scegli il Tuo Metodo!

### 🎯 **METODO 1: Eseguibile Windows (CONSIGLIATO - Zero Installazione)**

**Per utenti che NON hanno Python installato:**

1. **Scarica** il pacchetto `CalendarioPresenze_Portable.zip`
2. **Estrai** il contenuto in una cartella
3. **Doppio click** su `CalendarioPresenze.exe`
4. **Fatto!** Il browser si apre automaticamente

✅ Vantaggi:
- Nessuna installazione richiesta
- Funziona anche su PC con restrizioni
- Portabile (funziona da chiavetta USB)
- Dimensione: ~30-40 MB

📦 **Come creare l'eseguibile** (per sviluppatori):
```bash
# Metodo automatico
python build_exe.py

# Oppure con batch
build_exe.bat

# L'eseguibile sarà in: dist/CalendarioPresenze.exe
```

---

### 🎯 **METODO 2: Script Python (100% Automatico)**

**Per utenti con Python installato o che vogliono installarlo:**

#### Windows - Plug & Play 🎯
1. **Scarica o copia** l'intera cartella `Calendario` sul tuo PC
2. **Doppio click** su `run.bat`
3. **Al primo avvio**: Lo script controllerà automaticamente:
   - ✅ Se Python è installato (altrimenti ti guiderà all'installazione)
   - ✅ Se pip è disponibile (altrimenti lo installerà)
   - ✅ Creerà l'ambiente virtuale
   - ✅ Installerà le dipendenze (Flask)
   - ✅ Aprirà il browser sulla pagina dell'app
4. **Successivi avvii**: Lancio istantaneo, tutto già configurato!

> **Nota**: Se Python non è installato, lo script ti chiederà il permesso e aprirà la pagina di download. Ricordati di selezionare **"Add Python to PATH"** durante l'installazione!

#### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```
Lo script installerà automaticamente tutto il necessario al primo avvio.

---

### 🎯 **METODO 3: Docker (Multi-utente/Server)**

**Per deploy su server o uso multi-utente:**

```bash
# Avvio rapido
docker-compose up -d

# Oppure build manuale
docker build -t calendario-presenze .
docker run -p 5000:5000 -v $(pwd)/data:/app/data calendario-presenze
```

✅ Vantaggi:
- Isolamento completo
- Deploy su server remoto
- Backup facile del volume data/

---

### 🎯 **METODO 4: Avvio Manuale (Opzionale)**

```bash
# Crea ambiente virtuale
python3 -m venv venv

# Attiva ambiente
source venv/bin/activate  # Linux/macOS
# oppure: venv\Scripts\activate  # Windows

# Installa dipendenze
pip install -r requirements.txt

# Avvia l'app
python app.py
```

Poi apri il browser su: **http://127.0.0.1:5000**

---

## 📋 **Quale Metodo Scegliere?**

| Situazione | Metodo Consigliato |
|------------|-------------------|
| PC aziendale con restrizioni | **Eseguibile** (Metodo 1) |
| Uso su chiavetta USB | **Eseguibile** (Metodo 1) |
| PC personale | **Script Python** (Metodo 2) |
| Server / Multi-utente | **Docker** (Metodo 3) |
| Sviluppo / Personalizzazione | **Manuale** (Metodo 4) |

📖 **Guida completa:** Vedi `GUIDA_DISTRIBUZIONE.md` per tutti i dettagli e troubleshooting

## 📁 Struttura Progetto

```
Calendario/
├── app.py                      # Applicazione Flask principale
├── requirements.txt            # Dipendenze Python
├── run.bat / run.sh           # Launcher multi-piattaforma
├── Dockerfile                  # Configurazione Docker
├── docker-compose.yml          # Orchestrazione Docker
│
├── templates/                  # Template HTML/Jinja2
│   └── index.html
│
├── static/                     # File statici (CSS/JS)
│   └── app.js
│
├── data/                       # Database SQLite
│   └── .gitkeep               # (calendario.db creato automaticamente)
│
├── docs/                       # Documentazione
│   ├── GUIDA_UTENTE.md        # Manuale utente completo
│   ├── GUIDA_DISTRIBUZIONE.md # Guida distribuzione e build
│   └── CONTRIBUTING.md        # Guida per contributori
│
├── scripts/                    # Script di build e utility
│   ├── build_exe.py           # Crea eseguibile Windows
│   ├── build_exe.bat          # Build Windows (batch)
│   ├── create_package.py      # Crea pacchetto ZIP
│   └── menu.bat               # Menu interattivo
│
└── examples/                   # File di esempio
    └── esempio_import.csv     # Template CSV per import
```

## 📥 Import CSV

L'app supporta l'importazione da file CSV con le seguenti colonne:

| Colonna | Descrizione | Esempio |
|---------|-------------|---------|
| giorno | Giorno della settimana | Lunedì |
| data | Data in formato YYYY-MM-DD | 2025-12-01 |
| aula | Nome/numero aula | Aula 101 |
| orario_inizio | Ora inizio (HH:MM) | 09:00 |
| orario_fine | Ora fine (HH:MM) | 11:00 |
| totale_ore | Durata in ore (opzionale, calcolato auto) | 2 |
| nome_lezione | Nome della materia | Matematica |
| professore | Nome docente | Prof. Rossi |
| presente | Stato presenza (Sì/No, 1/0, true/false) | Sì |
| note | Note opzionali | Prima lezione |

**Separatore**: punto e virgola (`;`)

Vedi `examples/esempio_import.csv` per un esempio completo.

## 🔄 Portabilità - Copia e Usa Ovunque!

Per trasferire l'app su un altro PC (anche senza Python installato):

1. **Copia l'intera cartella** `Calendario/` su una chiavetta USB, cloud, o condivisione di rete
2. **Sul nuovo PC Windows**:
   - Incolla la cartella ovunque (Desktop, Documenti, ecc.)
   - Doppio click su `run.bat`
   - Se Python non è presente, lo script ti guiderà nell'installazione
   - Conferma l'installazione delle dipendenze quando richiesto
3. **Sul nuovo PC Linux/macOS**:
   - Incolla la cartella e apri il terminale
   - Esegui: `chmod +x run.sh && ./run.sh`

Il database `data/calendario.db` contiene tutti i dati e viene copiato insieme all'app.

**Zero configurazione richiesta!** L'applicazione è completamente plug-and-play.

## 🛠️ Requisiti

- Python 3.8 o superiore
- Flask (installato automaticamente)

## 📝 Note

- Il database viene creato automaticamente al primo avvio
- I dati sono salvati localmente in `data/calendario.db`
- Funziona completamente offline
- Supporta solo un utente alla volta (uso locale)

## 📚 Documentazione

- 📖 **[Guida Utente Completa](docs/GUIDA_UTENTE.md)** - Manuale dettagliato
- 📦 **[Guida Distribuzione](docs/GUIDA_DISTRIBUZIONE.md)** - Build e deploy
- 🤝 **[Contributing](docs/CONTRIBUTING.md)** - Come contribuire

## 🤝 Contribuire

I contributi sono benvenuti! Leggi [CONTRIBUTING.md](docs/CONTRIBUTING.md) per:
- Setup ambiente di sviluppo
- Linee guida codice
- Processo di pull request
- Aree di contributo

## 📄 Licenza

MIT License - Vedi file [LICENSE](LICENSE)

## 🐛 Segnalazione Bug

Apri una [Issue su GitHub](https://github.com/HafSimba/Calendario/issues) con:
- Descrizione del problema
- Passi per riprodurlo
- Sistema operativo e versione Python
- Screenshot (se applicabile)

---

Sviluppato con ❤️ usando Python + Flask + SQLite

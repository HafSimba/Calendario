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

## 🚀 Avvio Rapido

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```

### Windows
Doppio click su `run.bat`

### Manuale
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

## 📁 Struttura File

```
Calendario/
├── app.py              # Applicazione Flask principale
├── requirements.txt    # Dipendenze Python
├── run.sh             # Script avvio Linux/macOS
├── run.bat            # Script avvio Windows
├── esempio_import.csv  # File CSV di esempio
├── README.md          # Questa guida
├── templates/
│   └── index.html     # Interfaccia utente
└── data/
    └── calendario.db  # Database SQLite (creato automaticamente)
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

**Separatore**: punto e virgola (;)

Vedi `esempio_import.csv` per un esempio completo.

## 🔄 Portabilità

Per trasferire l'app su un altro PC:

1. Copia l'intera cartella `Calendario/`
2. Sul nuovo PC, esegui `run.sh` (Linux/Mac) o `run.bat` (Windows)
3. L'ambiente virtuale verrà creato automaticamente

Il database `data/calendario.db` contiene tutti i dati e viene copiato insieme all'app.

## 🛠️ Requisiti

- Python 3.8 o superiore
- Flask (installato automaticamente)

## 📝 Note

- Il database viene creato automaticamente al primo avvio
- I dati sono salvati localmente in `data/calendario.db`
- Funziona completamente offline
- Supporta solo un utente alla volta (uso locale)

---

Sviluppato con ❤️ usando Python + Flask + SQLite

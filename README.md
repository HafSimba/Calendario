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

## 🚀 Avvio Rapido (100% Automatico)

### Windows - Plug & Play 🎯
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

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```
Lo script installerà automaticamente tutto il necessario al primo avvio.

### Avvio Manuale (Opzionale)
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

---

Sviluppato con ❤️ usando Python + Flask + SQLite

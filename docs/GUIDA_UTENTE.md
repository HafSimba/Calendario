# 📖 Guida Utente - Calendario Presenze/Assenze

## 🚀 Installazione e Primo Avvio

### Windows
1. Scarica il progetto (ZIP o clone)
2. **Doppio click** su `run.bat`
3. Al primo avvio:
   - Conferma installazione dipendenze
   - Attendi 1-2 minuti
   - Il browser si aprirà automaticamente
4. Successivi avvii: Istantanei!

### Linux / macOS
```bash
chmod +x run.sh
./run.sh
```

### Via Docker
```bash
docker-compose up -d
# Apri: http://localhost:5000
```

## 📋 Funzionalità Principali

### 🎯 Visualizzazioni

#### Modalità Cubi (Default)
- Giorni mostrati come card 3D
- Navigazione con frecce ← →
- Click su un cubo per vedere dettagli del giorno
- Giorno corrente evidenziato

#### Modalità Lista
- Vista tabellare completa
- Ordinamento per data
- Tutte le lezioni visibili

**Cambiare vista:** Click su pulsanti 🎯 **Cubi** / 📋 **Lista**

### ➕ Aggiungere Lezioni

**Metodo 1 - Manuale:**
1. Click su **➕ Nuova Lezione**
2. Compila form:
   - Giorno e data
   - Aula
   - Orario inizio/fine
   - Nome lezione
   - Professore
   - Note (opzionale)
3. Click **💾 Salva**

**Metodo 2 - Import CSV:**
1. Click su **📥 Importa CSV**
2. Trascina file o click per selezionare
3. Usa formato: `examples/esempio_import.csv`
4. Click **📥 Importa**

### ✏️ Modificare Lezioni

**Nella vista cubi:**
1. Click sul cubo del giorno
2. Nella card lezione, click **✏️ Modifica**

**Nella vista lista:**
- Click sull'icona matita ✏️ nella riga

### ✅ Gestire Presenze/Assenze

**3 Opzioni disponibili:**

#### 1. ✅ Presente
- Lezione frequentata completamente

#### 2. ✗ Assente (Completo)
- Lezione saltata completamente

#### 3. ⏱ Assente Parziale
- Frequentata solo parte della lezione
- Specifica orario assenza:
  - **Da:** Ora inizio assenza (es: 10:00)
  - **A:** Ora fine assenza (es: 11:30)

**Come impostare:**
1. Click sul cubo/riga della lezione
2. Click sul badge presenza
3. Seleziona opzione
4. Se parziale: imposta orari
5. Click **💾 Salva Presenza**

### 🔍 Ricerca e Filtri

**Barra di ricerca:**
- Cerca per nome lezione, professore, aula
- Aggiorna risultati in tempo reale

**Filtro Presenza:**
- Tutte
- Solo presenze ✅
- Solo assenze ✗
- Solo parziali ⏱

**Filtro Mese:**
- Dropdown con tutti i mesi disponibili

**Filtro Data:**
- Seleziona data specifica

### 📊 Statistiche

Dashboard in alto mostra:
- **Totale Lezioni** - Numero lezioni inserite
- **Presenze** - Lezioni frequentate
- **Assenze** - Lezioni saltate (complete + parziali)
- **% Presenza** - Percentuale presenze sul totale
- **Ore Presenti** - Ore effettive di frequenza
- **Ore Totali** - Somma ore di tutte le lezioni

> 💡 Le assenze parziali contano come assenze nelle statistiche

### 📤 Esportare Dati

1. Click su **📤 Esporta CSV**
2. File scaricato: `calendario_presenze_YYYYMMDD.csv`
3. Apribile con Excel, Google Sheets, ecc.

**Formato export:**
```csv
giorno;data;aula;orario_inizio;orario_fine;totale_ore;nome_lezione;professore;presente;note
```

### 🗑️ Eliminare Lezioni

**Nella vista lista:**
- Click sull'icona cestino 🗑️
- Conferma eliminazione

> ⚠️ L'eliminazione è permanente!

## 💾 Backup e Ripristino

### Dove sono i dati?
Tutti i dati sono in: `data/calendario.db`

### Backup
1. **Manuale:** Copia `data/calendario.db` in luogo sicuro
2. **CSV:** Esporta regolarmente i dati

### Ripristino
1. Chiudi l'applicazione
2. Sostituisci `data/calendario.db` con il backup
3. Riavvia l'applicazione

## 🔧 Risoluzione Problemi

### ❌ "Python non trovato" (Windows)
**Soluzione:**
1. Scarica Python da: https://www.python.org/downloads/
2. Durante installazione: ✅ **"Add Python to PATH"**
3. Riavvia `run.bat`

### ❌ "Porta 5000 già in uso"
**Soluzione 1:** Chiudi altre istanze dell'app
**Soluzione 2:** Cambia porta in `app.py`:
```python
if __name__ == '__main__':
    app.run(port=5001)  # Usa porta diversa
```

### ❌ Il browser non si apre
**Soluzione:** Apri manualmente:
```
http://127.0.0.1:5000
```

### ❌ "Template not found"
**Soluzione:** Verifica che le cartelle esistano:
```
Calendario/
├── templates/
│   └── index.html
└── static/
    └── app.js
```

### ❌ CSV import fallito
**Cause comuni:**
- Formato non corretto
- Separatore sbagliato (usa `;`)
- Date in formato errato (usa YYYY-MM-DD)
- Colonne mancanti

**Soluzione:** Usa `examples/esempio_import.csv` come template

### ❌ Database locked
**Soluzione:**
1. Chiudi tutte le istanze dell'app
2. Riavvia

### ❌ Modifiche non salvate
**Verifica:**
- Hai cliccato "Salva"?
- Console browser per errori (F12)
- Connessione alla porta 5000 attiva?

## 📱 Utilizzo Mobile

L'interfaccia è responsive e utilizzabile da:
- Tablet
- Smartphone (landscape consigliato)

**Nota:** È un'app locale, accessibile solo dal PC dove è in esecuzione.

## 🔐 Sicurezza e Privacy

- ✅ **Completamente offline** dopo primo avvio
- ✅ **Dati solo sul tuo PC** (nessun cloud)
- ✅ **Nessuna telemetria** o tracking
- ✅ **Open source** - Codice ispezionabile

### Port Forwarding (Attenzione!)
**Non esporre** l'app su internet senza:
- Autenticazione
- HTTPS/SSL
- Firewall configurato

## 📚 Formato CSV per Import/Export

### Colonne richieste (separatore `;`):

| Colonna | Tipo | Esempio | Note |
|---------|------|---------|------|
| giorno | Testo | Lunedì | Nome giorno |
| data | Data | 2025-12-01 | Formato YYYY-MM-DD |
| aula | Testo | Aula 101 | Nome/numero aula |
| orario_inizio | Ora | 09:00 | Formato HH:MM |
| orario_fine | Ora | 11:00 | Formato HH:MM |
| totale_ore | Numero | 2 | Calcolato automaticamente |
| nome_lezione | Testo | Matematica | Nome corso/materia |
| professore | Testo | Prof. Rossi | Nome docente |
| presente | Boolean | Sì/No | Stato presenza |
| note | Testo | Prima lezione | Opzionale |

### Esempio file CSV:
```csv
giorno;data;aula;orario_inizio;orario_fine;totale_ore;nome_lezione;professore;presente;note
Lunedì;2025-12-01;Aula 101;09:00;11:00;2;Matematica;Prof. Rossi;No;
Martedì;2025-12-02;Aula 202;14:00;16:00;2;Fisica;Prof. Bianchi;Sì;
```

## ⌨️ Scorciatoie Tastiera

- **Ctrl + F** - Focus ricerca
- **ESC** - Chiudi modal
- **←** / **→** - Naviga carousel (vista cubi)

## 💡 Tips & Tricks

### 1. Import rapido
Prepara CSV in Excel/Google Sheets, poi esporta con `;` come separatore

### 2. Backup automatico
Copia `data/calendario.db` su cloud (Dropbox, Google Drive) regolarmente

### 3. Multi-dispositivo
Copia intera cartella su chiavetta USB - funziona ovunque!

### 4. Filtri combinati
Usa ricerca + filtro mese per trovare rapidamente lezioni

### 5. Statistiche accurate
Imposta assenze parziali con orari precisi per calcoli corretti

## 🆘 Serve Aiuto?

- 📖 Leggi: [Documentazione completa](./GUIDA_DISTRIBUZIONE.md)
- 🐛 Bug? Apri issue su GitHub
- 💬 Discussioni: GitHub Discussions
- 📧 Email: [Il tuo contatto]

---

**Buon lavoro! 📚**

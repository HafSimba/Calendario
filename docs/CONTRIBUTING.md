# 🤝 Contribuire al Progetto

Grazie per l'interesse nel contribuire a **Calendario Presenze/Assenze**!

## 📥 Setup Ambiente di Sviluppo

### 1. Clone del Repository
```bash
git clone https://github.com/HafSimba/Calendario.git
cd Calendario
```

### 2. Setup Ambiente Virtuale
```bash
# Crea ambiente virtuale
python -m venv .venv

# Attiva ambiente
source .venv/bin/activate  # Linux/macOS
# oppure: .venv\Scripts\activate  # Windows
```

### 3. Installa Dipendenze
```bash
# Dipendenze base
pip install -r requirements.txt

# Per build eseguibili (opzionale)
pip install pyinstaller
```

### 4. Avvia App in Modalità Dev
```bash
python app.py
# Apri: http://127.0.0.1:5000
```

## 🔧 Struttura Progetto

```
Calendario/
├── app.py                  # Applicazione Flask principale
├── templates/              # Template HTML/Jinja2
│   └── index.html
├── static/                 # File statici (CSS/JS)
│   └── app.js
├── data/                   # Database SQLite
│   └── .gitkeep
├── scripts/                # Script di build e utility
│   ├── build_exe.py       # Build eseguibile Windows
│   ├── create_package.py  # Crea pacchetto distribuzione
│   └── menu.bat           # Menu interattivo Windows
├── docs/                   # Documentazione
├── examples/               # File di esempio
│   └── esempio_import.csv
├── run.bat / run.sh       # Launcher cross-platform
└── requirements.txt        # Dipendenze Python
```

## 🐛 Segnalazione Bug

Apri una [Issue](https://github.com/HafSimba/Calendario/issues) con:
- ✅ Descrizione dettagliata del problema
- ✅ Passi per riprodurlo
- ✅ Comportamento atteso vs reale
- ✅ Screenshot (se applicabile)
- ✅ Sistema operativo e versione Python
- ✅ Output di `pip list` (se rilevante)

## 💡 Proporre Funzionalità

1. Apri una [Issue](https://github.com/HafSimba/Calendario/issues) con label `enhancement`
2. Descrivi la funzionalità proposta
3. Spiega il caso d'uso e i benefici
4. Attendi feedback prima di implementare

## 🔄 Workflow per Contributi

### 1. Fork e Branch
```bash
# Fork del repository (tramite GitHub UI)
git clone https://github.com/TUO_USERNAME/Calendario.git
cd Calendario

# Crea branch per la tua feature
git checkout -b feature/nome-funzionalita
```

### 2. Sviluppo
- Scrivi codice seguendo lo stile esistente
- Testa localmente tutte le modifiche
- Aggiungi commenti dove necessario
- Mantieni commit piccoli e focalizzati

### 3. Commit
```bash
git add .
git commit -m "feat: Aggiunge [descrizione breve]

- Dettaglio 1
- Dettaglio 2
- Riferimento issue #123"
```

**Convenzioni commit:**
- `feat:` - Nuova funzionalità
- `fix:` - Correzione bug
- `docs:` - Solo documentazione
- `style:` - Formattazione, punto e virgola mancanti, ecc.
- `refactor:` - Refactoring codice
- `test:` - Aggiunta test
- `chore:` - Manutenzione (build, dipendenze)

### 4. Push e Pull Request
```bash
git push origin feature/nome-funzionalita
```

Poi su GitHub:
1. Vai al tuo fork
2. Click su "Pull Request"
3. Compila il template con:
   - Descrizione delle modifiche
   - Riferimento a issue correlate
   - Screenshot (se UI)
   - Checklist test effettuati

## ✅ Checklist Pre-Commit

Prima di fare commit, verifica:
- [ ] Il codice è testato e funziona
- [ ] Non ci sono dati personali nel commit
- [ ] Non ci sono file `data/*.db` (database)
- [ ] Non ci sono cartelle `venv/` o `.venv/`
- [ ] La documentazione è aggiornata (se necessario)
- [ ] Il commit segue le convenzioni

```bash
# Verifica file da committare
git status

# Verifica diff
git diff

# Verifica che .gitignore funzioni
git status --ignored
```

## 🧪 Testing

Prima di aprire una PR, testa:

### Test Base
```bash
# 1. Avvio app
python app.py
# Verifica che si apra su http://127.0.0.1:5000

# 2. Test funzionalità principali
- Aggiungi una lezione
- Modifica presenza
- Import CSV (usa examples/esempio_import.csv)
- Export CSV
- Filtri e ricerca
- Statistiche
```

### Test Build Eseguibile (Opzionale)
```bash
cd scripts
python build_exe.py
# Verifica che dist/CalendarioPresenze.exe funzioni
```

### Test Cross-Platform
Se possibile, testa su:
- Windows 10/11
- Linux (Ubuntu/Debian)
- macOS

## 📚 Linee Guida Codice

### Python
- Segui PEP 8
- Usa docstring per funzioni
- Nomi variabili descrittivi
- Commenti dove il codice non è auto-esplicativo

```python
def calcola_ore(orario_inizio, orario_fine):
    """Calcola le ore totali tra due orari.
    
    Args:
        orario_inizio (str): Orario inizio formato HH:MM
        orario_fine (str): Orario fine formato HH:MM
    
    Returns:
        float: Ore totali arrotondate a 2 decimali
    """
    # Implementazione...
```

### JavaScript
- Usa `const` e `let`, evita `var`
- Funzioni arrow quando appropriato
- Commenti JSDoc per funzioni pubbliche

### HTML/CSS
- Indentazione consistente (2 o 4 spazi)
- Classi CSS semantiche
- Responsive design (mobile-first)

## 🔒 Sicurezza

**NON committare mai:**
- Database con dati reali (`data/*.db`)
- Credenziali o API keys
- File di configurazione personali
- CSV con informazioni sensibili

Se trovi vulnerabilità di sicurezza, **NON aprire issue pubbliche**.
Contatta privatamente tramite email/GitHub Security Advisory.

## 📦 Build e Distribuzione

### Creare Eseguibile Windows
```bash
cd scripts
python build_exe.py
# Output: dist/CalendarioPresenze.exe
```

### Creare Pacchetto Distribuzione
```bash
cd scripts
python create_package.py
# Output: CalendarioPresenze_v1.0_YYYYMMDD.zip
```

### Build Docker
```bash
docker build -t calendario-presenze .
docker run -p 5000:5000 calendario-presenze
```

## 🎯 Aree di Contributo

Siamo interessati a contributi in:

- 🐛 **Bug fixes** - Sempre benvenuti!
- ✨ **Nuove funzionalità** - Discussi prima tramite issue
- 📚 **Documentazione** - Miglioramenti, traduzioni
- 🎨 **UI/UX** - Design, responsive, accessibilità
- 🧪 **Testing** - Unit test, integration test
- 🌍 **Internazionalizzazione** - Traduzioni in altre lingue
- ⚡ **Performance** - Ottimizzazioni
- 🔧 **Tooling** - Script, automazione, CI/CD

## 📝 Stile Documentazione

- File Markdown con formattazione corretta
- Esempi di codice con syntax highlighting
- Screenshot per feature UI
- Link relativi per file interni

## 🙏 Riconoscimenti

Tutti i contributori saranno aggiunti al file `CONTRIBUTORS.md`.

## 📄 Licenza

Contribuendo al progetto, accetti che i tuoi contributi saranno rilasciati sotto la [MIT License](../LICENSE).

## 💬 Domande?

- Apri una [Discussion](https://github.com/HafSimba/Calendario/discussions)
- Controlla le [Issues esistenti](https://github.com/HafSimba/Calendario/issues)
- Leggi la [documentazione completa](./GUIDA_DISTRIBUZIONE.md)

---

**Grazie per contribuire! 🎉**

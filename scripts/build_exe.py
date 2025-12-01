#!/usr/bin/env python3
"""
Script per creare eseguibile Windows standalone dell'applicazione
Genera un file .exe che include Python, Flask e tutte le dipendenze
"""

import os
import sys
import subprocess
import shutil

def run_command(cmd, description):
    """Esegue un comando e mostra il progresso"""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print('='*60)
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ ERRORE: {result.stderr}")
        return False
    print(f"✅ Completato!")
    return True

def main():
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     📦 BUILD ESEGUIBILE WINDOWS - Calendario Presenze         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Vai alla directory root del progetto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)
    print(f"📁 Directory progetto: {root_dir}\n")
    
    # Verifica PyInstaller
    print("\n[1/6] Verifica PyInstaller...")
    result = subprocess.run("pip show pyinstaller", shell=True, capture_output=True)
    if result.returncode != 0:
        print("⚠️  PyInstaller non trovato. Installazione in corso...")
        if not run_command("pip install pyinstaller", "Installazione PyInstaller"):
            return False
    else:
        print("✅ PyInstaller già installato")
    
    # Pulizia build precedenti
    print("\n[2/6] Pulizia build precedenti...")
    for folder in ['build', 'dist', '__pycache__']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"  Rimosso: {folder}/")
    if os.path.exists('CalendarioPresenze.spec'):
        os.remove('CalendarioPresenze.spec')
        print("  Rimosso: CalendarioPresenze.spec")
    print("✅ Pulizia completata")
    
    # Build eseguibile
    print("\n[3/6] Compilazione eseguibile (può richiedere 2-3 minuti)...")
    
    # Comando PyInstaller con tutte le opzioni
    cmd = [
        "pyinstaller",
        "--onefile",                    # Un singolo file .exe
        "--windowed",                   # No console window (commenta per debug)
        "--name=CalendarioPresenze",    # Nome eseguibile
        "--icon=NONE",                  # Nessuna icona (puoi aggiungerne una)
        "--add-data=templates;templates",  # Includi templates
        "--add-data=data;data",            # Includi database (se esiste)
        "--hidden-import=flask",
        "--hidden-import=sqlite3",
        "--clean",
        "app.py"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ ERRORE durante la compilazione:\n{result.stderr}")
        return False
    print("✅ Compilazione completata!")
    
    # Verifica output
    print("\n[4/6] Verifica file generati...")
    exe_path = os.path.join("dist", "CalendarioPresenze.exe")
    if os.path.exists(exe_path):
        size_mb = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"✅ Eseguibile creato: {exe_path}")
        print(f"   Dimensione: {size_mb:.1f} MB")
    else:
        print("❌ Eseguibile non trovato!")
        return False
    
    # Copia file necessari nella cartella dist
    print("\n[5/6] Copia file di supporto...")
    
    # Crea cartella templates in dist se non esiste
    dist_templates = os.path.join("dist", "templates")
    if not os.path.exists(dist_templates):
        os.makedirs(dist_templates)
    
    # Copia template
    if os.path.exists("templates/index.html"):
        shutil.copy2("templates/index.html", dist_templates)
        print("  ✅ templates/index.html")
    
    # Copia static
    if os.path.exists("static"):
        dist_static = os.path.join("dist", "static")
        if os.path.exists(dist_static):
            shutil.rmtree(dist_static)
        shutil.copytree("static", dist_static)
        print("  ✅ static/")
    
    # Copia file di esempio
    if os.path.exists("examples/esempio_import.csv"):
        shutil.copy2("examples/esempio_import.csv", "dist")
        print("  ✅ examples/esempio_import.csv")
    
    # Copia documentazione principale
    for file in ["README.md", "LICENSE"]:
        if os.path.exists(file):
            shutil.copy2(file, "dist")
            print(f"  ✅ {file}")
    
    # Crea cartella data vuota
    dist_data = os.path.join("dist", "data")
    if not os.path.exists(dist_data):
        os.makedirs(dist_data)
        print("  ✅ data/ (vuota)")
    
    # Crea README per la distribuzione
    print("\n[6/6] Creazione file di istruzioni...")
    with open("dist/LEGGI_PRIMA.txt", "w", encoding="utf-8") as f:
        f.write("""╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     📅  CALENDARIO PRESENZE/ASSENZE - Versione Portable       ║
║         Nessuna installazione richiesta!                      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝


🚀 AVVIO IMMEDIATO
═══════════════════════════════════════════════════════════════

1. Doppio click su "CalendarioPresenze.exe"
2. Attendi 5-10 secondi (primo avvio più lento)
3. Il browser si aprirà automaticamente!


📋 COSA CONTIENE QUESTO PACCHETTO?
═══════════════════════════════════════════════════════════════

✅ CalendarioPresenze.exe    → Applicazione completa standalone
✅ templates/                → File interfaccia utente
✅ static/                   → Risorse JavaScript e CSS
✅ data/                     → Database (creato al primo avvio)
✅ esempio_import.csv        → Template per importare lezioni
✅ README.md                 → Documentazione completa
✅ ISTRUZIONI.txt            → Guida rapida


📁 REQUISITI
═══════════════════════════════════════════════════════════════

✅ Windows 7/8/10/11 (64-bit)
✅ 30 MB spazio disco
✅ Nessun software aggiuntivo
✅ Funziona completamente OFFLINE!


💡 VANTAGGI VERSIONE PORTABLE
═══════════════════════════════════════════════════════════════

• Non richiede Python installato
• Non richiede permessi amministratore
• Funziona da chiavetta USB
• Copia e incolla su qualsiasi PC
• Database viaggia nella cartella data/


🔧 RISOLUZIONE PROBLEMI
═══════════════════════════════════════════════════════════════

❌ Windows Defender blocca l'eseguibile?
   → Normale per app non firmate
   → Click su "Maggiori informazioni" → "Esegui comunque"

❌ Antivirus lo mette in quarantena?
   → Aggiungi eccezione per CalendarioPresenze.exe
   → È un falso positivo comune per app PyInstaller

❌ Finestra si chiude subito?
   → Verifica che le cartelle templates/ e static/ siano presenti
   → Esegui da prompt: CalendarioPresenze.exe (per vedere errori)

❌ Porta 5000 già in uso?
   → Chiudi altre istanze dell'app
   → Oppure modifica la porta in app.py e ricompila


📦 DISTRIBUZIONE
═══════════════════════════════════════════════════════════════

Per condividere l'app con altri utenti:

1. Comprimi l'intera cartella "dist" in un file ZIP
2. Invia il ZIP all'utente
3. L'utente deve:
   - Estrarre il ZIP
   - Doppio click su CalendarioPresenze.exe
   - Fine! Funziona subito!


═══════════════════════════════════════════════════════════════
Versione: 1.0 Portable
Build: PyInstaller
═══════════════════════════════════════════════════════════════
""")
    print("✅ LEGGI_PRIMA.txt creato")
    
    # Crea anche un launcher batch opzionale
    with open("dist/AVVIA_CON_CONSOLE.bat", "w", encoding="utf-8") as f:
        f.write("""@echo off
echo Avvio Calendario Presenze con console di debug...
echo Attendi qualche secondo...
echo.
CalendarioPresenze.exe
pause
""")
    print("✅ AVVIA_CON_CONSOLE.bat creato")
    
    print(f"""
{'='*60}
  ✅ BUILD COMPLETATO CON SUCCESSO!
{'='*60}

📦 Eseguibile pronto in: dist/CalendarioPresenze.exe
   Dimensione: {size_mb:.1f} MB

📁 La cartella "dist/" contiene tutto il necessario:
   - CalendarioPresenze.exe
   - templates/
   - static/
   - data/
   - File di documentazione

🚀 PROSSIMI PASSI:

1. Testa l'eseguibile:
   cd dist
   CalendarioPresenze.exe

2. Per distribuire:
   - Comprimi la cartella "dist" in un ZIP
   - Rinomina il ZIP in "CalendarioPresenze_v1.0_Portable.zip"
   - Condividi!

3. Per aggiornare:
   - Modifica app.py o i template
   - Esegui di nuovo: python build_exe.py

{'='*60}
⚠️  IMPORTANTE: Non eliminare le cartelle templates/ e static/
    L'eseguibile ha bisogno di questi file per funzionare!
{'='*60}
""")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Build fallito!")
        sys.exit(1)
    else:
        print("\n✅ Tutto completato!")
        sys.exit(0)

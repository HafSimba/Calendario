#!/usr/bin/env python3
"""
Script per creare pacchetto ZIP di distribuzione
Include tutto il necessario per distribuzione plug-and-play
"""

import os
import shutil
import zipfile
from datetime import datetime

def create_distribution_zip():
    """Crea ZIP con tutti i file necessari per distribuzione"""
    
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     📦 CREAZIONE PACCHETTO DISTRIBUZIONE                      ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Vai alla directory root del progetto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)
    print(f"📁 Directory progetto: {root_dir}\n")
    
    # Nome e versione
    version = "1.0"
    date_str = datetime.now().strftime("%Y%m%d")
    zip_name = f"CalendarioPresenze_v{version}_{date_str}.zip"
    
    print(f"📦 Creazione: {zip_name}\n")
    
    # File da includere
    files_to_include = [
        'app.py',
        'requirements.txt',
        'run.bat',
        'run.sh',
        'README.md',
        'LICENSE',
        'Dockerfile',
        'docker-compose.yml',
        '.gitignore'
    ]
    
    # Directory da includere
    dirs_to_include = [
        'templates',
        'static',
        'docs',
        'scripts',
        'examples'
    ]
    
    # Crea ZIP
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        
        # Aggiungi file
        print("📄 Aggiunta file...")
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file, f"CalendarioPresenze/{file}")
                print(f"  ✅ {file}")
            else:
                print(f"  ⚠️  {file} non trovato, skip")
        
        # Aggiungi directory
        print("\n📁 Aggiunta directory...")
        for dir_name in dirs_to_include:
            if os.path.exists(dir_name):
                for root, dirs, files in os.walk(dir_name):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.join("CalendarioPresenze", file_path)
                        zipf.write(file_path, arcname)
                print(f"  ✅ {dir_name}/")
            else:
                print(f"  ⚠️  {dir_name}/ non trovata, skip")
        
        # Crea directory data vuota
        zipf.writestr(zipfile.ZipInfo("CalendarioPresenze/data/.keep"), "")
        print(f"  ✅ data/ (vuota)")
    
    # Info finali
    size_mb = os.path.getsize(zip_name) / (1024 * 1024)
    
    print(f"""
{'='*60}
  ✅ PACCHETTO CREATO CON SUCCESSO!
{'='*60}

📦 File: {zip_name}
💾 Dimensione: {size_mb:.2f} MB

📋 Contenuto:
   - Script di avvio automatico (run.bat / run.sh)
   - Applicazione Flask completa
   - Template e static files
   - Documentazione completa
   - File di esempio CSV
   - Dockerfile per deploy server

🚀 Distribuzione:
   1. Invia {zip_name} agli utenti
   2. Loro estraggono il file
   3. Eseguono run.bat (Windows) o run.sh (Linux/macOS)
   4. L'app si installa e avvia automaticamente!

📝 Note:
   - Prima esecuzione: installa dipendenze (richiede internet)
   - Esecuzioni successive: avvio istantaneo offline
   - Il database viene creato automaticamente nella cartella data/

{'='*60}
    """)

if __name__ == "__main__":
    try:
        create_distribution_zip()
        print("✅ Completato!\n")
    except Exception as e:
        print(f"\n❌ Errore: {e}\n")
        exit(1)

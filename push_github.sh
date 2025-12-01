#!/bin/bash
# Script per preparare e pushare su GitHub

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     🚀 PUSH AUTOMATICO SU GITHUB                              ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Verifica che siamo nella directory corretta
if [ ! -f "app.py" ]; then
    echo "❌ Errore: Esegui questo script dalla cartella Calendario!"
    exit 1
fi

echo "📋 Step 1: Verifica file sensibili..."
if git ls-files | grep -qE "lezioni_corso.csv|calendariotocsv.md"; then
    echo "⚠️  ATTENZIONE: File con dati personali trovati nel tracking!"
    echo "Rimuovili con: git rm --cached <file>"
    exit 1
fi
echo "✅ Nessun file sensibile tracciato"

echo ""
echo "📋 Step 2: Rimozione database dal tracking (se presente)..."
if git ls-files | grep -q "data/.*\.db"; then
    git rm --cached data/*.db 2>/dev/null || true
    echo "✅ Database rimosso dal tracking"
else
    echo "✅ Database già non tracciato"
fi

echo ""
echo "📋 Step 3: Aggiungo file necessari..."
git add .gitignore
git add GITHUB.md LICENSE PUSH_GITHUB.txt data/.gitkeep esempio_import.csv
git add README.md GUIDA_DISTRIBUZIONE.md ISTRUZIONI.txt DISTRIBUZIONE_FACILE.txt
git add app.py templates/ static/ requirements.txt requirements-build.txt
git add run.bat run.sh build_exe.py build_exe.bat create_package.py menu.bat
git add app_desktop.py Dockerfile docker-compose.yml
echo "✅ File aggiunti"

echo ""
echo "📋 Step 4: Stato repository..."
git status

echo ""
echo "═══════════════════════════════════════════════════════════════"
read -p "Procedere con il commit? (s/n): " confirm

if [ "$confirm" != "s" ]; then
    echo "❌ Operazione annullata"
    exit 0
fi

echo ""
echo "📋 Step 5: Commit..."
git commit -m "Aggiorna progetto per distribuzione GitHub

- Configurato .gitignore per escludere dati sensibili
- Rimosso database dal tracking (solo struttura)
- Aggiunto esempio_import.csv come template
- Aggiunti LICENSE (MIT) e documentazione GitHub
- Aggiunti script di build e distribuzione
- Mantenuta struttura cartelle con .gitkeep"

echo ""
echo "📋 Step 6: Push su origin main..."
git push origin main

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     ✅ PUSH COMPLETATO CON SUCCESSO!                          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🎯 Prossimi passi:"
echo "   1. Vai su GitHub.com nel tuo repository"
echo "   2. Verifica che tutto sia corretto"
echo "   3. Crea una Release (opzionale)"
echo "   4. Condividi il link!"
echo ""

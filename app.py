#!/usr/bin/env python3
"""
Calendario Presenze/Assenze - Applicazione Flask
Applicazione portabile per tracciare le presenze alle lezioni.
"""

import os
import csv
import io
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file
import sqlite3

app = Flask(__name__)

# Database path - relativo alla cartella dell'app per portabilità
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(DATA_DIR, 'calendario.db')

def get_db():
    """Connessione al database SQLite."""
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inizializza il database con lo schema."""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS lezioni (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            giorno TEXT NOT NULL,
            data TEXT NOT NULL,
            aula TEXT,
            orario_inizio TEXT,
            orario_fine TEXT,
            totale_ore REAL,
            nome_lezione TEXT,
            professore TEXT,
            presente INTEGER DEFAULT 0,
            assenza_da TEXT,
            assenza_a TEXT,
            note TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def calcola_ore(orario_inizio, orario_fine):
    """Calcola le ore totali tra due orari (formato HH:MM)."""
    try:
        if not orario_inizio or not orario_fine:
            return 0
        fmt = "%H:%M"
        inizio = datetime.strptime(orario_inizio, fmt)
        fine = datetime.strptime(orario_fine, fmt)
        delta = fine - inizio
        return round(delta.seconds / 3600, 2)
    except:
        return 0

@app.route('/')
def index():
    """Pagina principale con il calendario."""
    return render_template('index.html')

@app.route('/api/lezioni', methods=['GET'])
def get_lezioni():
    """Ottiene tutte le lezioni."""
    conn = get_db()
    cursor = conn.execute('''
        SELECT * FROM lezioni ORDER BY data ASC, orario_inizio ASC
    ''')
    lezioni = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(lezioni)

@app.route('/api/lezioni', methods=['POST'])
def add_lezione():
    """Aggiunge una nuova lezione."""
    data = request.json
    
    # Calcola automaticamente le ore se non fornite
    totale_ore = data.get('totale_ore')
    if not totale_ore:
        totale_ore = calcola_ore(data.get('orario_inizio'), data.get('orario_fine'))
    
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO lezioni (giorno, data, aula, orario_inizio, orario_fine, 
                            totale_ore, nome_lezione, professore, presente, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('giorno', ''),
        data.get('data', ''),
        data.get('aula', ''),
        data.get('orario_inizio', ''),
        data.get('orario_fine', ''),
        totale_ore,
        data.get('nome_lezione', ''),
        data.get('professore', ''),
        1 if data.get('presente') else 0,
        data.get('note', '')
    ))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'success': True})

@app.route('/api/lezioni/<int:id>', methods=['PUT'])
def update_lezione(id):
    """Aggiorna una lezione esistente."""
    data = request.json
    
    # Calcola automaticamente le ore se non fornite
    totale_ore = data.get('totale_ore')
    if not totale_ore:
        totale_ore = calcola_ore(data.get('orario_inizio'), data.get('orario_fine'))
    
    conn = get_db()
    conn.execute('''
        UPDATE lezioni SET 
            giorno = ?, data = ?, aula = ?, orario_inizio = ?, orario_fine = ?,
            totale_ore = ?, nome_lezione = ?, professore = ?, presente = ?, note = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', (
        data.get('giorno', ''),
        data.get('data', ''),
        data.get('aula', ''),
        data.get('orario_inizio', ''),
        data.get('orario_fine', ''),
        totale_ore,
        data.get('nome_lezione', ''),
        data.get('professore', ''),
        1 if data.get('presente') else 0,
        data.get('note', ''),
        id
    ))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/lezioni/<int:id>', methods=['DELETE'])
def delete_lezione(id):
    """Elimina una lezione."""
    conn = get_db()
    conn.execute('DELETE FROM lezioni WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/lezioni/<int:id>/presenza', methods=['PATCH'])
def toggle_presenza(id):
    """Cambia lo stato presenza/assenza con supporto per assenze parziali."""
    data = request.json
    presente = 1 if data.get('presente') else 0
    assenza_da = data.get('assenza_da')
    assenza_a = data.get('assenza_a')
    
    conn = get_db()
    conn.execute('''
        UPDATE lezioni SET presente = ?, assenza_da = ?, assenza_a = ?, 
                          updated_at = CURRENT_TIMESTAMP 
        WHERE id = ?
    ''', (presente, assenza_da, assenza_a, id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/import-csv', methods=['POST'])
def import_csv():
    """Importa lezioni da un file CSV."""
    if 'file' not in request.files:
        return jsonify({'error': 'Nessun file caricato'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nessun file selezionato'}), 400
    
    try:
        # Leggi il CSV
        stream = io.StringIO(file.stream.read().decode('utf-8-sig'))
        reader = csv.DictReader(stream, delimiter=';')
        
        # Mapping flessibile dei nomi colonne
        column_mapping = {
            'giorno': ['giorno', 'day', 'giorni'],
            'data': ['data', 'date', 'data_lezione'],
            'aula': ['aula', 'room', 'classroom', 'stanza'],
            'orario_inizio': ['orario_inizio', 'inizio', 'start', 'ora_inizio', 'orario inizio'],
            'orario_fine': ['orario_fine', 'fine', 'end', 'ora_fine', 'orario fine'],
            'totale_ore': ['totale_ore', 'ore', 'hours', 'totale ore', 'durata'],
            'nome_lezione': ['nome_lezione', 'lezione', 'materia', 'corso', 'nome lezione', 'subject'],
            'professore': ['professore', 'docente', 'teacher', 'prof'],
            'presente': ['presente', 'presence', 'presenze', 'present'],
            'note': ['note', 'notes', 'commenti']
        }
        
        def find_column(row, field):
            """Trova il valore usando mapping flessibile."""
            for possible_name in column_mapping.get(field, [field]):
                for key in row.keys():
                    if key.lower().strip() == possible_name.lower():
                        return row[key]
            return ''
        
        conn = get_db()
        imported = 0
        
        for row in reader:
            orario_inizio = find_column(row, 'orario_inizio')
            orario_fine = find_column(row, 'orario_fine')
            totale_ore = find_column(row, 'totale_ore')
            
            if not totale_ore:
                totale_ore = calcola_ore(orario_inizio, orario_fine)
            
            presente_val = find_column(row, 'presente')
            presente = 1 if presente_val and presente_val.lower() in ['1', 'si', 'sì', 'yes', 'true', 'presente', 'x'] else 0
            
            conn.execute('''
                INSERT INTO lezioni (giorno, data, aula, orario_inizio, orario_fine, 
                                    totale_ore, nome_lezione, professore, presente, note)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                find_column(row, 'giorno'),
                find_column(row, 'data'),
                find_column(row, 'aula'),
                orario_inizio,
                orario_fine,
                totale_ore,
                find_column(row, 'nome_lezione'),
                find_column(row, 'professore'),
                presente,
                find_column(row, 'note')
            ))
            imported += 1
        
        conn.commit()
        conn.close()
        return jsonify({'success': True, 'imported': imported})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/export-csv')
def export_csv():
    """Esporta tutte le lezioni in CSV."""
    conn = get_db()
    cursor = conn.execute('SELECT * FROM lezioni ORDER BY data ASC')
    lezioni = cursor.fetchall()
    conn.close()
    
    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    
    # Header
    writer.writerow(['giorno', 'data', 'aula', 'orario_inizio', 'orario_fine', 
                     'totale_ore', 'nome_lezione', 'professore', 'presente', 'note'])
    
    for lezione in lezioni:
        writer.writerow([
            lezione['giorno'],
            lezione['data'],
            lezione['aula'],
            lezione['orario_inizio'],
            lezione['orario_fine'],
            lezione['totale_ore'],
            lezione['nome_lezione'],
            lezione['professore'],
            'Sì' if lezione['presente'] else 'No',
            lezione['note'] or ''
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8-sig')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'calendario_presenze_{datetime.now().strftime("%Y%m%d")}.csv'
    )

@app.route('/api/stats')
def get_stats():
    """Ottiene statistiche sulle presenze."""
    conn = get_db()
    cursor = conn.execute('''
        SELECT 
            COUNT(*) as totale_lezioni,
            SUM(CASE WHEN presente = 1 THEN 1 ELSE 0 END) as presenze,
            SUM(CASE WHEN presente = 0 THEN 1 ELSE 0 END) as assenze,
            SUM(CASE WHEN presente = 1 THEN totale_ore ELSE 0 END) as ore_presenti,
            SUM(totale_ore) as ore_totali
        FROM lezioni
    ''')
    row = cursor.fetchone()
    conn.close()
    
    totale = row['totale_lezioni'] or 0
    presenze = row['presenze'] or 0
    
    return jsonify({
        'totale_lezioni': totale,
        'presenze': presenze,
        'assenze': row['assenze'] or 0,
        'percentuale_presenza': round((presenze / totale * 100), 1) if totale > 0 else 0,
        'ore_presenti': row['ore_presenti'] or 0,
        'ore_totali': row['ore_totali'] or 0
    })

@app.route('/api/clear-all', methods=['DELETE'])
def clear_all():
    """Cancella tutti i dati."""
    conn = get_db()
    conn.execute('DELETE FROM lezioni')
    conn.commit()
    conn.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    print("=" * 50)
    print("  CALENDARIO PRESENZE/ASSENZE")
    print("  Apri il browser su: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=False, host='127.0.0.1', port=5000)

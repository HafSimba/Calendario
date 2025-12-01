#!/usr/bin/env python3
"""Script per aggiungere le colonne assenza_da e assenza_a al database"""
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'data', 'calendario.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE lezioni ADD COLUMN assenza_da TEXT")
    print("✓ Colonna assenza_da aggiunta")
except:
    print("⚠ Colonna assenza_da già esistente")

try:
    cursor.execute("ALTER TABLE lezioni ADD COLUMN assenza_a TEXT")
    print("✓ Colonna assenza_a aggiunta")
except:
    print("⚠ Colonna assenza_a già esistente")

conn.commit()
conn.close()
print("✓ Migrazione completata!")

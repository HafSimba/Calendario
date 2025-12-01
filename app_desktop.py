"""
Alternative: App Desktop con Eel (Python + Chrome embedded)
Più leggero di Electron, più moderno di PyInstaller
"""

# Installa con: pip install eel

import eel
import os
import sys
from app import app as flask_app

# Configura Eel per usare la cartella templates
eel.init('templates')

@eel.expose
def get_lezioni():
    """Espone API Flask a JavaScript"""
    with flask_app.test_client() as client:
        response = client.get('/api/lezioni')
        return response.get_json()

@eel.expose
def add_lezione(data):
    """Aggiunge lezione via Eel"""
    with flask_app.test_client() as client:
        response = client.post('/api/lezioni', json=data)
        return response.get_json()

def main():
    """Avvia app desktop"""
    # Avvia server Flask in background
    import threading
    server_thread = threading.Thread(target=lambda: flask_app.run(port=5000, debug=False, use_reloader=False))
    server_thread.daemon = True
    server_thread.start()
    
    # Avvia interfaccia Eel
    try:
        eel.start('index.html', size=(1400, 900), port=8080)
    except:
        # Fallback a browser normale
        import webbrowser
        webbrowser.open('http://127.0.0.1:5000')
        flask_app.run(port=5000, debug=False)

if __name__ == '__main__':
    main()

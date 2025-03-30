import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000  # Puoi usare qualsiasi porta, ma 8000 è una scelta comune

# Avvia il server sulla directory corrente
Handler = SimpleHTTPRequestHandler
os.chdir(os.path.abspath('.'))  # Cambia la directory per essere la root del progetto
with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

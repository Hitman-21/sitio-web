import http.server
import socketserver

puerto = 8000  # Puedes cambiar el número de puerto si lo deseas

# Configura el servidor web para servir archivos estáticos desde la carpeta actual
handler = http.server.SimpleHTTPRequestHandler

# Crea un servidor web en el puerto especificado
with socketserver.TCPServer(("", puerto), handler) as httpd:
    print(f"Servidor web en el puerto {puerto}")
    
    # Inicia el servidor y manténlo en ejecución
    httpd.serve_forever()

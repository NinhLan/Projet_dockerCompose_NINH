#!/usr/bin/env python3

# Importation des bibliothèques système python.
# Ces bibliothèques seront utilisées pour créer le serveur web.
import http.server
import socketserver

# Cette variable va gérer les requêtes de notre client sur le serveur.
handler = http.server.SimpleHTTPRequestHandler

# Ici nous définissons que nous voulons démarrer le serveur sur le port 1234.
# Essayez de vous souvenir de cette information, elle nous sera très utile plus tard avec docker-compose.
with socketserver.TCPServer(("", 1234), handler) as httpd :
  # Cette instruction va maintenir le serveur en fonctionnement, en attendant les requêtes du client.
  httpd.serve_forever()

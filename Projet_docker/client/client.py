#!/usr/bin/env python3

# Importation de la bibliothèque système python.
# Cette bibliothèque est utilisée pour télécharger le fichier 'index.html' du serveur.
import urllib.request

# Cette variable contient la requête sur 'http://localhost:1234/'.
# localhost : Cela signifie que le serveur est local.
# 1234 : Rappelez-vous que nous avons défini 1234 comme le port du serveur.
fp = urllib.request.urlopen("http://localhost:1234/")
fp = urllib.request.urlopen("http://localhost:1234/")

# 'encodedContent' correspond à la réponse du serveur encodée ('index.html').
# 'decodedContent' correspond à la réponse du serveur décodée (ce que nous voulons afficher).
encodedContent = fp.read()
decodedContent = encoded
Content.decode("utf8")

# Affiche le fichier du serveur : 'index.html'.
print(decodedContent)

# Fermez la connexion au serveur.
fp.close()

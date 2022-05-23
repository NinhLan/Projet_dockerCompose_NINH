# Dockerfile doit toujours commencer par importer l'image de base.
# Nous utilisons le mot clé 'FROM' pour le faire.
# Dans notre exemple, nous voulons importer l'image python (de DockerHub).
# Donc, nous écrivons 'python' pour le nom de l'image et 'latest' pour la version.
FROM python:latest

# Afin de lancer notre code python, nous devons importer le fichier 'serveur.py' et 'index.html'.
# Nous utilisons le mot clé 'ADD' pour ce faire.
# Pour rappel, le premier paramètre 'serveur.py' est le nom du fichier sur l'hôte.
# Le second paramètre '/serveur/' est le chemin où placer le fichier sur l'image.
# Ici, nous plaçons les fichiers dans le dossier '/serveur/' de l'image.
ADD serveur.py /serveur/
ADD index.html /serveur/

# Je voudrais introduire quelque chose de nouveau, la commande 'WORKDIR'.
# Cette commande change le répertoire de base de votre image.
# Ici nous définissons '/serveur/' comme répertoire de base (où toutes les commandes seront exécutées).
WORKDIR /serveur/

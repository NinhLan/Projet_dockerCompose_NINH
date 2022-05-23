# Projet_dockerCompose_NINH

## L’objectif du projet
Dans la cadre de ce module, je me decide de faire un projet de Docker Compose qui contient 2 coteneur différent(Serveur et client).

L'objectif de ce projet est de créer un petit site web (serveur) en Python qui contiendra une phrase. Cette phrase doit être récupérée par un programme (client) en Python qui affichera la phrase.


## Créer le projet

Pour créer mon application client/serveur, j'ai créé un dossier sur ma VM linux. Il contient à la racine le fichier et les dossiers suivants :  

* Un fichier __'docker-compose.yml'__  (fichier docker-compose qui contient les instructions nécessaires à la création des différents services).  
* Un dossier __'serveur'__  (ce dossier contient les fichiers nécessaires à la mise en place du serveur).  
* Un dossier __'client'__  (ce dossier contient les fichiers nécessaires à la mise en place du client).  

L'architecture des dossier de mon projet est ci-dessous :  

```
Projet_docker/
├── client/
├── serveur/
└── docker-compose.yml
```
## Créer un client
### 1. Créer des fichiers  
Dans le dossier j’ai créé des ficher suivant :  
* Un fichier __'client.py'__ (fichier python qui contiendra le code du client).
* Un fichier __'Dockerfile'__ (fichier docker qui contiendra les instructions nécessaires pour créer l'environnement du client).  
Normalement, vous devriez avoir cette architecture de dossier dans le chemin suivant 'client/' :

```
.
├── client.py
└── Dockerfile
```
### 2. Edite fichier Python.  
Ce code me permet de récupérer le contenu de la page web du serveur et de l'afficher.
```
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
```

### 3. Edit the Docker file  
Quant au serveur, nous allons créer un Dockerfile de base qui sera chargé d'exécuter notre fichier Python.  

```
FROM python:latest

# Nous importons *client.py* dans le dossier */client/*.
ADD client.py /client/

# Je voudrais introduire quelque chose de nouveau, la commande *WORKDIR*.
# Cette commande change le répertoire de base de votre image.
# Ici nous définissons */client/* comme répertoire de base.
WORKDIR /client/

```
## Créer un serveur
### 1. Créer des fichiers   
Dans le dossier j’ai créé des ficher suivant :  
* Un fichier 'serveur.py' (fichier python qui contient le code du serveur).
* Un fichier 'index.html' (fichier HTML qui contiendra la phrase à afficher).
* Un fichier 'Dockerfile' (fichier docker qui contiendra les instructions nécessaires pour créer l'environnement du serveur).
Architecture de dossier dans le chemin suivant 'serveur/' :

```
.
├─── Dockerfile
├─── index.html
└─── serveur.py

```
### 2. Ficher python  
Ce code permet de créer un simple serveur web à l'intérieur de ce dossier. Il récupérera le contenu du fichier index.html pour le partager sur une page web.
```
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

```

### 3. Fichier HTML  
```
Bonjour, je suis Thi Hoa Lan NINH – étudiante d’EPISEN
```
Le serveur partagera ce fichier au démarrage, et cette phrase s'affichera.

### 4. Fichier Docker file  
Ici, nous allons créer un Dockerfile de base qui sera chargé d'exécuter notre fichier Python. Pour ce faire, nous allons utiliser l'image officielle créée pour exécuter Python.

```
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
```

 ## Docker Compose  
Maintenant nous allons éditer le fichier 'docker-compose.yml' à la racine du dépôt.
```
# docker-compose fonctionne avec des services.
# 1 service = 1 conteneur.
# Par exemple, un service peut être un serveur, un client
# Nous utilisons le mot clé 'services' pour commencer à créer des services.
services :
  # Car nous voulons créer : un serveur et un client.
  # Cela fait deux services.
  # Premier service (conteneur) : le serveur.
  # Il va vous permettre de définir à quoi correspond le service.
  # Nous utilisons le mot clé 'serveur' pour le serveur.
  serveur :
    # Le mot clé "build" permet de définir
    # le chemin vers le Dockerfile à utiliser pour créer l'image
    # qui vous permettra d'exécuter le service.
    # Ici, 'serveur/' correspond au chemin d'accès au dossier du serveur
    # qui contient le Dockerfile à utiliser.
    build : serveur/

    # La commande à exécuter une fois l'image créée.
    # La commande suivante exécutera "python ./serveur.py".
    commande : python ./serveur.py

    # Rappelez-vous que nous avons défini dans 'serveur/serveur.py' 1234 comme port.
    # Si nous voulons accéder au serveur depuis notre ordinateur (en dehors du conteneur),
    # nous devons partager le port du contenu avec le port de notre ordinateur.
    # Pour ce faire, le mot clé 'ports' nous aidera.
    # Sa syntaxe est la suivante : [port que nous voulons sur notre machine] : [port que nous voulons récupérer dans le conteneur]
    # Dans notre cas, nous voulons utiliser le port 1234 sur notre machine et
    # récupérer le port 1234 dans le conteneur (car c'est sur ce port que
    # nous diffusons le serveur).
    ports :
      - 1234:1234

  # Deuxième service (conteneur) : le client.
  # Nous utilisons le mot clé 'client' pour le serveur.
  client :
    # Ici 'client/ correspond au chemin vers le dossier client
    # qui contient le Dockerfile à utiliser.
    build : client/

    # La commande à exécuter une fois l'image créée.
    # La commande suivante exécutera "python ./client.py".
    commande : python ./client.py

    # Le mot clé 'network_mode' est utilisé pour définir le type de réseau.
    # Ici, nous définissons que le conteneur peut accéder à 'localhost' de l'ordinateur.
    network_mode : host

    # Le mot clé 'depends_on' permet de définir si le service
    # doit attendre que d'autres services soient prêts avant de se lancer.
    # Ici, nous voulons que le service 'client' attende que le service 'serveur' soit prêt.
    depends_on :
      - serveur
```
##Build Docker-Compose
Une fois le docker-compose mis en place, il faut construire votre application client/serveur. Cette étape correspond à la commande 'docker build' mais appliquée aux différents services.

```
$ docker-compose build
```

## Run Docker-Compose
Le docker-compose est build. Il est maintenant temps de démarrer. Cette étape correspond à la commande 'docker run' mais appliquée aux différents services.
```
$ docker-compose up
```
## Résultat

Maintenant, on peut voir s’afficher la phrase qu’on a mis dans html dans notre terminal.  

![alt text](https://github.com/NinhLan/Projet_dockerCompose_NINH/blob/5439c9e47e2948a2e2d0eb857901f582970703d2/images/b.png?raw=true)
 
Ou dans une navigateur web  

![alt text](https://github.com/NinhLan/Projet_dockerCompose_NINH/blob/5439c9e47e2948a2e2d0eb857901f582970703d2/images/a.png?raw=true)
 

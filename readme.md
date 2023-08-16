# Construction de l'image
    docker build -t launch_another .
Pour générer l'image launch_another. On se place sur le répertoire où se trouve le Dockerfile.
# Suppression du conteneur
    docker rm launch_another_c 
# Lancement du conteneur
    docker run --name launch_another_c -v /var/run/docker.sock:/var/run/docker.sock launch_another
On a besoin de monter le volume pour accéder à la socket de docker et de se connecter avec dans le *main.py*.
    
    client = docker.from_env()
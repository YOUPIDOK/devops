# Utilisation de l'image Python 3.8
FROM python:3.8

# Définition du répertoire de travail
WORKDIR /app

# Copie du script Python dans le conteneur
COPY main.py /app/main.py

# Installation des dépendances
RUN pip install mysql-connector-python

# Exposition du port sur lequel le serveur écoute
EXPOSE 8000

# Commande pour exécuter le script Python
CMD ["python", "main.py"]
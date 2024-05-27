Plan de développement
1. Analyse des besoins / Cahier des charges:
  

    Étudier les exigences du projet : Lire attentivement les spécifications et les besoins du client.
    Définir les fonctionnalités : Déterminer les fonctionnalités de la calculatrice NPI (Notation Polonaise Inverse), de l’API REST, de la base de données et de l'exportation en CSV.

2. Architecture du projet

    Choisir la stack technologique : Python, FastAPI, SQLite/PostgreSQL, Docker, Docker Compose.
    Définir l’architecture : Microservices, MVC (Model-View-Controller).

3. Conception de l'algorithme

    Conception de l’algorithme NPI : Rédiger un pseudo-code ou diagramme de flux pour l’algorithme de calcul.
    Implémentation de la calculatrice : Développer et tester l’algorithme en Python.

4. Développement de l'API REST

    Création du squelette de l'API : Initialiser un projet FastAPI.
    Développer les endpoints :
        Endpoint pour réaliser les opérations.
        Endpoint pour exporter les données en CSV.

5. Gestion de la base de données

    Modélisation de la base de données : Définir les tables pour stocker les opérations et les résultats.
    Connexion à la base de données : Configurer SQLAlchemy ou Tortoise ORM avec FastAPI.

6. Tests et validation

    Tests unitaires : Écrire des tests unitaires pour chaque composant.
    Tests d’intégration : Tester l’intégration des différents composants (API, base de données, Docker).
    Revue de code : Faire une revue de code avec l’équipe ou individuellement.

7. Déploiement

    Configuration de Docker : Écrire des Dockerfile pour le projet.
    Docker Compose : Configurer docker-compose.yml pour orchestrer les services.
    Déploiement : Déployer les conteneurs Docker sur un serveur.

Répartition des tâches

    En équipe :
        Développeur 1 : Conception et développement de l’algorithme NPI.
        Développeur 2 : Développement des endpoints de l’API REST.
        Développeur 3 : Gestion de la base de données et intégration avec FastAPI.
        Développeur 4 : Configuration de Docker et Docker Compose.
    En solo : Suivre les étapes séquentiellement en commençant par l’algorithme, puis l’API, la base de données, et enfin Docker.

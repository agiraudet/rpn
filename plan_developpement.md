# Plan de Développement pour le Projet de Calculatrice RPN

## Phase 1 : Planification et Collecte des Exigences

1. **Exigences** :
   Nous devons ajouter une calculatrice à un outil de valorisation. Certaines technologies nous sont imposées, à savoir Python (FastAPI) pour le backend, et React pour le frontend, mais nous sommes libres de choisir, par exemple, la base de données. Cette calculatrice doit :

   - Utiliser la notation NPI
   - Enregistrer les opérations et les résultats dans une base de données
   - Permettre de récupérer ces données dans un fichier .csv

2. **Jalons** :

   - **Backend**:
     - Développer l'algorithme de la calculatrice
     - Concevoir l'API
     - Implémentation
   - Développer l'environnement Docker pour le déploiement
   - Tester le backend
   - **Frontend**:
     - Design
     - Implémentation
   - Tester l'application

3. **Allocation des Ressources** :
   - **En solo** : Réaliser les tâches une par une, du backend vers le frontend, en suivant l'ordre des jalons établis.
   - **En équipe** : Faire en amont le design de l'API (sa documentation), afin de permettre aux développeurs backend et frontend de travailler simultanément.

## Phase 2 : Conception

1. **Conception de l'API** :
   - **Endpoints** :
     - **GET /** : Point d'entrée par défaut de l'API. Retourne un HelloWorld.
     - **POST /calculator** : Calcule l'expression en NPI envoyée, retourne l'expression et le résultat.

2. **Architecture Système** :
   - **Docker Compose** : Afin de garder une structure simple et facile à maintenir, chaque service s'exécutera dans son propre conteneur : backend, frontend, db.

3. **Conception Frontend** :
   - **UI/UX** : Design
   - **Implémentation**

## Phase 3 : Implémentation

1. **Mise en Place du Contrôle de Version**

2. **Développement Backend** :
   - Développement de l'algo NPI
   - Configuration de l'environnement
   - Implémentation des endpoints de l'API
   - Ajout de la base de données
   - Test

3. **Développement Frontend** :
   - Configuration de l'environnement
   - Création des composants
   - Intégration à l'API
   - Design/Style
   - Test

4. **Configuration Docker** :
   - Créer un Dockerfile par service
   - Créer un fichier docker-compose pour orchestrer l'ensemble

## Phase 4 : Tests

   Mettre en place des tests automatisés et des tests utilisateurs pour vérifier que notre solution convient bien à ses besoins.

## Phase 6 : Documentation et Remise

1. **Documentation** :
   - **Documentation du Code** : Documenter la base de code avec des commentaires et des fichiers README.
   - **Documentation de l'API** : Documenter l'API en utilisant la documentation auto-générée de FastAPI.
   - **Guide Utilisateur** : Créer un guide utilisateur pour utiliser la calculatrice.

## Phase 7 : Maintenance

1. **Surveillance et Journalisation** :
   - **Surveillance** : Mettre en place une surveillance pour suivre les performances et la santé de l'application.
   - **Journalisation** : Implémenter la journalisation pour capturer les événements et les erreurs de l'application.

2. **Corrections de Bugs et Améliorations** :
   - **Suivi des Problèmes** : Utiliser l'outil de gestion de projet pour suivre et résoudre les bugs et les demandes d'améliorations.

## Phase 8 : Amélioration

   Avec davantage de temps, il serait très intéressant d'améliorer chacun de ces services en place :
   - Backend : Ajouter des options plus fines de sélection pour le CSV (de date à date, quantité de données, etc.).
   - Base de données : Ajouter un système de sauvegarde régulier.
   - Frontend : Travailler à un design plus valorisant.
   - Environnement : s'assurer que les secrets type mot de passe db sont placés dans un .env et non hard-codés.

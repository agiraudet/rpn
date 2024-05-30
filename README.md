# Calculatrice RPN

Ce projet consiste en une calculatrice utilisant la notation polonaise inverse (RPN). Il utilise Python avec FastAPI pour le backend et React pour le frontend.

## Plan de Développement

Consultez le fichier [plan_developpement.md](https://github.com/agiraudet/rpn/blob/main/plan_developpement.md) pour obtenir le plan détaillé du développement du projet.

## Lancer l'Application

Pour lancer l'application, utilisez Docker Compose :

```bash
docker-compose up
```

Sur les systèmes Fedora, vous pouvez utiliser Podman Compose :

```bash
podman-compose up
```

## Tester l'Application

Une fois l'application lancée, vous pouvez accéder aux URL suivantes :

- **Backend** : [http://localhost:8000/docs](http://localhost:8000/docs) (Documentation auto-générée de l'API FastAPI)
- **Frontend** : [http://localhost:3000](http://localhost:3000) (Interface utilisateur de l'application React)

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](https://github.com/agiraudet/rpn/blob/main/LICENSE) pour plus d'informations.

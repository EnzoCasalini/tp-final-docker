# Workshop 3 – Architecture Web avec Docker 🐳

## 🚀 Objectif

Ce projet a pour but de créer une architecture microservices avec Docker et Docker Compose, comprenant :

- 🐬 Une base de données MySQL
- ⚙️ Une API FastAPI avec routes pour admin et utilisateur
- 🎛️ Un front administrateur pour ajouter des adresses
- 👀 Un front utilisateur pour visualiser les adresses
- 🌐 Un reverse proxy Nginx pour centraliser l'accès sur le port 80

---

## 🧱 Structure du projet

```
tp-final-docker/
├── docker-compose.yml
├── api/
│   ├── Dockerfile
│   ├── app/                 # Code FastAPI
│   ├── requirements.txt     # Dépendances Python
│   └── migrations/          # SQL d'initialisation
├── front_admin/
│   ├── Dockerfile
│   └── index.html           # Formulaire d'ajout
├── front_users/
│   ├── Dockerfile
│   └── index.html           # Affichage des adresses
└── reverse-proxy/
    └── default.conf         # Config Nginx
```

---

## ▶️ Lancer le projet

Assurez-vous d’avoir [Docker](https://www.docker.com/) installé.

Dans le dossier racine du projet :

```bash
docker-compose up --build
```

---

## 🧪 Tester le projet en local

Une fois les services lancés, accédez aux interfaces suivantes :

| Composant           | URL                               | Description                                 |
|---------------------|------------------------------------|---------------------------------------------|
| 🎛️ Front Admin       | http://localhost/admin            | Ajouter une adresse via un formulaire       |
| 👀 Front Utilisateur | http://localhost/user             | Voir la liste des adresses enregistrées     |
| 🔌 API – GET         | http://localhost/api/user/adresses| Retourne les adresses au format JSON        |
| 🔌 API – POST        | [POST] http://localhost/api/admin/adresses | Crée une nouvelle adresse (via formulaire)  |

### ✔️ Test via `curl`

```bash
# Voir les adresses
curl http://localhost/api/user/adresses

# Ajouter une adresse
curl -X POST http://localhost/api/admin/adresses \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "numero_rue=42&nom_rue=Rue des Tests&ville=DockerCity&code_postal=42000"
```

---

## 💾 Persistance des données

Les données MySQL sont stockées dans un **volume Docker** (`db-data`), ce qui permet de conserver les adresses **entre chaque redémarrage** :

```bash
docker-compose down     # Les données sont conservées
docker-compose down -v  # ⚠️ Supprime aussi les données
```

---

## 📦 Dépendances

- `mysql:8.0.36`
- `nginx:1.25.3-alpine`
- `python:3.11.7-slim`
- `fastapi`, `uvicorn`, `mysql-connector-python`

---

## 👨‍💻 Auteurs

- CASALINI Enzo 
- CASTELLO Andréas 
- NGUYEN Chandler
- BALIVET Sinclair

---

🎉 **Bon test et bonne démo !**

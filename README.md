# Workshop 3 – Architecture Web avec Docker 🐳

## 🚀 Objectif
Architecture microservices avec :
- Base de données MySQL
- API (FastAPI)
- Front administrateur (ajout d’adresses)
- Front utilisateur (visualisation)
- Reverse proxy Nginx

## 🧱 Structure
- `api/`: code Python FastAPI + migrations SQL
- `front_admin/`: formulaire HTML d’ajout
- `front_users/`: affichage des adresses
- `reverse-proxy/`: config Nginx
- `docker-compose.yml`: configuration des services

## ▶️ Lancer le projet

```bash
docker-compose up --build
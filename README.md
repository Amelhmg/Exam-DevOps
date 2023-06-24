# Exam-DevOps
Application Python

## Utilisation
1. Lancez le serveur Flask :
   python3 exam.py
2. Utilisez les points d'accès suivants pour interagir avec l'API :
- ` /<nb_rows>` : Remplit la base de données avec le nombre spécifié.
- ` /select` : Récupère les informations de tous les utilisateurs depuis la base de données.

## Exemples
Pour remplir la base de données avec 10 enregistrements utilisateur, effectuez la requête suivante : http://localhost:8800/10
Pour récupérer les informations de tous les utilisateurs, effectuez la requête suivante : http://localhost:8800/select


## Technologies Utilisées
- Python 3
- Flask
- SQLite





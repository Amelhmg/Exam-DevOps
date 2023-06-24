## Code Source
Le code source de ce projet se trouve dans la branche `master` de ce dépôt. Assurez-vous de consulter cette branche pour accéder au code.

# Exam-DevOps
Application Python

## Utilisation
1. Lancez le serveur Flask :
   python3 exam.py
2. Utilisez les points d'accès suivants pour interagir avec l'API :
- ` /<nb_rows>` : Remplit la base de données avec le nombre spécifié.
- ` /select` : Récupère les informations de tous les utilisateurs depuis la base de données.
  ou
  
  Vous pouvez également accéder à l'API en ouvrant le fichier `index.html` dans votre navigateur. La page `index.html` vous permettra 
  d'interagir avec l'API en utilisant une interface conviviale.



## Exemples
1.Pour remplir la base de données avec 10 enregistrements utilisateur, effectuez la requête suivante : http://localhost:8800/10

2.Pour récupérer les informations de tous les utilisateurs, effectuez la requête suivante : http://localhost:8800/select


## Technologies Utilisées
- Python 3
- Flask
- SQLite





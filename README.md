## Code Source
Le code source de ce projet se trouve dans la branche `master` de ce dépôt. Assurez-vous de consulter cette branche pour accéder au code.

# Exam-DevOps

Application de Gestion des Utilisateurs

Cette application Python vous permet de gérer une liste d'utilisateurs en calculant leur âge et en offrant la possibilité de les supprimer de la base de données. 
Elle utilise une base de données SQLite pour stocker les informations des utilisateurs, telles que leur nom, prénom et date de naissance.

## Fonctionnalités

- **Calcul de l'âge :** L'application utilise la date de naissance de chaque utilisateur pour calculer automatiquement leur âge en fonction de la date actuelle. Cette fonctionnalité vous permet d'obtenir rapidement l'âge des utilisateurs enregistrés.

- **Suppression d'utilisateurs :** Vous avez la possibilité de supprimer des utilisateurs de la base de données. Cette fonctionnalité est utile si vous souhaitez retirer des utilisateurs de la liste pour une raison quelconque.


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





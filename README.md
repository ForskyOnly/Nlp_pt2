# Computer Vision Détection d'objet 


## Context du projet
### Consignes

Vous travaillez pour un psychologue qui conseille à ses patients d'écrire sur un journal intime numérique entre les séances. 
Il aimerait que vous développiez pour lui un outil capable d'utiliser ces écrits pour l'aider dans son travail sans être obligé de lire chacun des textes.

ce projet est la suite du projet NLP que vous trouverez [Ici](https://github.com/ForskyOnly/NLP) 





## Le projet: 
### User Story :
- En tant que psychologue je veux avoir accès à un espace de connexion particulier pour y visualiser la répartition des émotions de mes patients actifs sur une certaine période de temps
- En tant que psychologue je veux pouvoir visualiser la répartition des émotions d’un de mes patients en recherchant par son nom et prénom
- En tant que psychologue je veux pouvoir rechercher tous les textes contenant une certaines expressions avec la possibilité de filtrer par émotions et par nom/prénom de patient
- En tant que psychologue, je veux pouvoir me créer un nouveau patient avec un mot de passe par défaut, un nom et un prénom.
- En tant que patient je veux pouvoir accéder à un espace privé de connexion
- En tant que patient je veux pouvoir créer un nouveau texte.
- En tant qu psychologue je veux que les textes écrits par les patients soient automatiquement évalués par le modèle hugging face déployé

- Les informations sur les patients et psychologues doivent être enregistrées dans une base postgres.
- Les textes et les évaluations dans une base elastic search
- L’application développée avec django
- Crée une Image avec docker-compose pour regroupper les bases de données 


## Fichiers présent dans le depot: 

- best.pt : Ce fichier contient le modéle entrainer pour détecter les signes 
- sing_language.ipynb : Ce fichier contient l'import du dataset, le modéle entrainer pour la problématique et quelques visualisation concernant les score obtenu par le modéle 
- requirements.txt : Ce fichier contient les bibliothéque nécessaire pour installer et utiliser l'application
- main.py : Ce fichier contient le programme principal de l'application streamlit 

## Installation

1. Clonez [ce dépôt.](https://github.com/ForskyOnly/Nlp_pt2)
2. déplacer vous dans le répertoire "nlp_projet" de l'application
3. Executez dans le terminal `docker-compose build` pour crée l'image
4. Executez dans le terminal `docker-compose up` pour lancer l'image
5. naviguez ver `http://0.0.0.0:8000/` pour voir le site


## Bibliothèque utilisées

- Django==4.2.3
- django-elasticsearch-dsl==7.3
- docker==6.1.1
- elastic-transport==8.4.0
- elasticsearch==7.17.9
- elasticsearch-dsl==7.4.1
- python-dotenv==1.0.0
- sqlparse==0.4.4
- transformers==4.30.2
- psycopg2==2.9.6
- faker==8.14.0



## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.


## Contributeurs: 

- [Rubic](https://github.com/ForskyOnly)
- [Noura](https://github.com/Amineelbb)




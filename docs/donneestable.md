
{% set num = 5 %}
{% set titre = "Données en table"%}
{% set theme = "donneestable"%}


{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Format csv",[],0) }}

1. Consulter le site [data.gouv.fr](https://data.gouv.fr/){target=_blank} et notamment sa [page de documentation](https://doc.data.gouv.fr/){target=_blank}. Quels sont les objectifs de ce site ?
2. Consulter cette [page](https://www.data.gouv.fr/fr/datasets/menus-des-cantines-des-colleges/) du site `data.gouv.fr`. Quelles données peut-on télécharger sur cette page ? Sous quel forme sont-elles proposées ?
3. Prévisualiser les données au format `csv`. Faites des recherches sur ce format de données.
4. Expliquer rapidement comment sont représentées des données au format `csv`

{{ titre_activite("Lecture et traitement",["notebook"]) }}
{{ telecharger("Jupyter Notebook","notebook/MenuCantine.ipynb")}}

{{ titre_activite("Tri d'une table",[]) }}

Le fichier [Médailles Tokyo 2021](./files/C5/Tokyo2021.csv) présente au format `csv` le tableau des médailles des jeux olympiques de Tokyo 2021.

1. Quelques révisions
    1. Télécharger ce fichier et l'ouvrir pour en avoir un aperçu, quels sont les descripteurs de ce fichier `csv` ?
    2. Comment sont classés les pays ?
    3. Recopier et compléter le programme Python suivant qui permet (à l'aide du module `csv`) de lire ce fichier sous la forme d'une liste de dictionnaires dont les clés sont les descripteurs.

        ```python3
        import csv
        # Attention : préciser éventuellement le chemin d'accès complet du fichier
        fichier_medailles=open(.......,"r",encoding="utf-8")
        # Lecture sous forme de dictionnaire 
        medailles = list(csv.DictReader(...........,delimiter=','))
        fichier_medailles......()
        ```

    4. Que contient la variable `medailles[0]["Total"]` ? 
    5. De quel type est cette variable ?

        !!! Warning "A retenir (source de bugs)"
            Même une quantité numérique lue à partir d'un fichier   `csv` est une chaine de caractère pour Python. Penser à convertir en type numérique (`int` ou `float` avant d'effectuer comparaisons et tris)

2. On souhaite lister les pays par nombre total de médailles (et pas par nombre de médaille d'or). On doit donc trier la liste de dictionnaire avec le critère de la clé `Total`. Pour cela :

    1. créer une fonction qui renvoie la valeur associée à la clé `Total` :
    ```python
    def total_medailles(pays):
        return int(pays["Total"])
    ```
    2. utiliser la fonction `sorted` de python en précisant que cette fonction est la **clé** (`key`) de tri 
    ```python
    medailles_par_total = sorted(medailles,key = total_medailles)
    ```
    3. Afficher les cinq premières lignes du nouveau dictionnaire `medailles_par_total`, le résultat est-il celui attendu ? Quel est le problème ?

    4. Afficher (ou rechercher) l'aide sur la fonction `sorted` de Python, en déduire comment effectuer un tri par ordre décroissant.

3. On décide d'effectuer un classement par points, en attribuant 10 points à une médaille d'or, 4 à une médaille d'argent et 1 à une médaille de bronze. 
    1. Ecrire le programme Python permettant d'effectuer ce classement.
    2. Donner la liste  des 10 premiers pays avec ce nouveau classement.


## Cours

{{ cours("C5/C5-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}} 


## Exercices

{{ exo("Fichier `csv`",[],0)}}
1. Corriger le fichier `pays.csv` ci-dessous afin qu'il soit correct :
```csv
Nom;Capitale;Surface(km2);Population(M)
France;Paris;551695,67
Allemagne;Berlin;83
Espagne;505992;47
```
2. Le programme Python suivant permet d'ouvrir ce fichier et de créer la liste de dictionnaires `pays`, corriger les erreurs commises à la ligne 2 :
```python linenums="1"
import csv
fichier_pays.open("pays.csv","read")
pays = list(csv.Dictreader(fichier_pays,delimiter=";")
fichier_pays.close()
```

{{ exo("Personnages célèbres de l'histoire de l'informatique",[]) }}
On reprend l'exemple de fichier `csv` d'informaticiens célèbres vu en cours :
```csv
Nom;Prénom;Naissance
Pascal;Blaise;1623
Lovelace;Ada;1815
Boole;George;1815
```

1. Faire une copie de fichier sous le nom `informaticiens.txt`
2. Ajouter les descripteurs suivant `décès` (pour l'année de la mort), `nationalité`, `sexe` et `contribution`. Ce dernier champ contient les contributions du personnage à l'histoire de l'informatique. 
3. Faire des recherches sur le *Web* afin de pouvoir compléter ces champs pour chacun des trois personnages ci-dessus

    !!! aide 
        Pour Blaise Pascal, on peut par exemple écrire *"Invention de la première machine à calculer"* dans le champ `contribution`.

4. Ajouter un enregistrement de votre choix à ce fichier `csv`.
5. Ecrire un programme Python permettant de lire ce fichier `csv` et de créer la liste de dictionnaires `celebres`.
6. Trier ce dictionnaire par date de naissance.


{{ exo("Statistiques des prénoms donnés en France",[]) }}
Le but de l'exercice est de réutiliser un fichier de données du site [data.gouv.fr](https://data.gouv.fr)} pour en extraire des informations. Il s'agit des prénoms donnés en France entre 1900 et 2019.

1. Télécharger le fichier à partir de l'adresse suivante : [fichier des prénoms](https://www.data.gouv.fr/fr/datasets/ficher-des-prenoms-de-1900-a-2019/){target=_blank}
2. Ce fichier peut-il être ouvert avec un tableur ? Pourquoi ?
3. Ecrire un programme Python permettant de lire ce fichier et de créer la liste de dictionnaires `prenoms`.

    !!! Aide 
        * le délimiteur de champ est le point-virgule `;`

4. Donner la liste des descripteurs de ce fichier et leur signification.
5. Recherche le nombre de fois où votre prénom à été attribué dans votre département l'année de votre naissance.
6. Quels ont été les trois prénoms les plus attribués à la Réunion en 2000 ?
7. Le prénom Dominique est mixte, en 2000 donner le nombre de personnes de chacun des deux sexes portant ce prénom.
8. Rechercher les prénoms rares (attribués moins de 4 fois) à la Réunion en 2005.

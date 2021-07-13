
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
{{ telecharger("Jupyter Notebook","C2/C2-act1.pdf")}}

 

## Cours

{{ cours("C3/C3-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}} 


## Exercices

{{ exo("Personnages célèbres de l'histoire de l'informatique",[],0) }}


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



{% set num = 3 %}
{% set titre = "Données en table"%}
{% set theme = "donneestable"%}
{% set num_qcm = [] %}

{% set num_exo=1 %}
{% set num_act=1 %}



{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,"Format csv",["notebook"]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Jupyter Notebook","C2/C2-act1.pdf")}}

## Cours

{{ cours("C3/C3-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo(num_exo,"Personnages célèbres de l'histoire de l'informatique",[]) }}
{% set num_exo=num_exo+1 %}

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



{% set num = 4 %}
{% set titre = "Recherche dans une liste"%}
{% set theme = "algorithmique"%}
{% set num_qcm = [] %}

{% set num_exo=1 %}
{% set num_act=1 %}

 

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,"Complexité d'un algorithme",[]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Jupyter notebook","notebook/Recherche dans une liste.ipynb")}}

{{ titre_activite(num_act,"Correction d'un algorithme",[]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Fiche d'activité","pdf/C4/C4-act2.pdf")}}

{{ titre_activite(num_act,"Terminaison d'un algorithme",[]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Fiche d'activité","pdf/C4/C4-act2.pdf")}}

## Cours

{{ cours("C4/C4-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}}
 

## Exercices

{{ exo(num_exo,"",[]) }}
{% set num_exo=num_exo+1 %}


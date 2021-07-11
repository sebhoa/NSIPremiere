
{% set num = 3 %}
{% set titre = "Initiation à Python avec Turtle"%}
{% set theme = "python"%}
{% set num_qcm = [] %}

{% set num_exo=1 %}
{% set num_act=1 %}



{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,"Module turtle",["notebook"]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Jupyter Notebook","C2/C2-act1.pdf")}}


## Cours

{{ cours("") }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo(num_exo,"Rectangles",[]) }}
{% set num_exo=num_exo+1 %}



{% set num = 12 %}
{% set titre = "Interaction dans une page Web"%}
{% set theme = "web" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Javascript",[],0) }}


## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("A venir",[],0) }}



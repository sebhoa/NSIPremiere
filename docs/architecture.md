
{% set num = 4 %}
{% set titre = "Architecture matérielle"%}
{% set theme = "os" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Composants d'un ordinateur",[],0) }}


{{ titre_activite("Architecture de Von Neumann",[]) }}


{{ titre_activite("Booléens",[]) }}

## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Parties d'un ordinateur",[],0) }}


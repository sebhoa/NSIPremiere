
{% set num = 7 %}
{% set titre = "Architecture matérielle"%}
{% set theme = "os" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Composants d'un ordinateur",[],0) }}


{{ titre_activite("Architecture de Von Neumann",[]) }}


{{ titre_activite("Booléens",[]) }}

## Cours

{{ cours("CHEMIN VERS PDF DE COURS") }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Parties d'un ordinateur",[],0) }}


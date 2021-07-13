
{% set num = 1 %}
{% set titre = "TITRE CHAPITRE ICI"%}
{% set theme = "os" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("TITRE ACTIVITE 1",[],0) }}


CONTENU ACTIVITE 1

{{ titre_activite("TITRE ACTIVITE 2",[]) }}


CONTENU ACTIVITE 2

...

## Cours

{{ cours("CHEMIN VERS PDF DE COURS") }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("TITRE EXO 1",[],0) }}


CONTENU EXO 1


{{ exo("TITRE EXO 2",[]) }}


CONTENU EXO 2


{{ exo("TITRE EXO 3",[]) }}


CONTENU EXO 3
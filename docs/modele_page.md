
{% set num = 1 %}
{% set titre = "TITRE CHAPITRE ICI"%}
{% set theme = "THEME"%}
{% set num_qcm = [LISTE NUMEROS QCM] %}

{% set num_exo=1 %}
{% set num_act=1 %}



{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,TITRE ACTIVITE 1,[ICONES EVENTUELLES]) }}
{% set num_act=num_act+1 %}

CONTENU ACTIVITE 1

{{ titre_activite(num_act,TITRE ACTIVITE 2,[ICONES EVENTUELLES]) }}
{% set num_act=num_act+1 %}

CONTENU ACTIVITE 2

...

## Cours

{{ cours("CHEMIN VERS PDF DE COURS") }}


## QCM

{{affiche_qcm(num_qcm)}}


## Exercices

{{ exo(num_exo,TITRE EXO 1,[LISTE ICONE]) }}
{% set num_exo=num_exo+1 %}

CONTENU EXO 1


{{ exo(num_exo,TITRE EXO 2,[LISTE ICONE]) }}
{% set num_exo=num_exo+1 %}

CONTENU EXO 2


{{ exo(num_exo,TITRE EXO 3,[LISTE ICONE]) }}
{% set num_exo=num_exo+1 %}

CONTENU EXO 3
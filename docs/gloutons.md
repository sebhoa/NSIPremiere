
{% set num = 8 %}
{% set titre = "Algorithmes gloutons"%}
{% set theme = "algorithmique" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Introduction",["oral"],0) }}

![Problème du sac à dos](./images/C8/pbsac.png){: .imgcentre}

1. Quel est le problème illustré par l'image ci-dessous ?
2. Proposer une réponse à ce problème.

{{ titre_activite("Problème du sac à dos",["notebook"]) }}

{{ telecharger("Jupyter notebook","notebook/SacDos.ipynb")}}



{{ titre_activite("Problème du rendu de monnaie",["notebook"]) }}
{{ telecharger("Jupyter notebook","notebook/RenduMonnaie.ipynb")}}


## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Un problème du sac à dos",[],0) }}


<!-- --> |
:-------:|
:material-bag-personal:{  .sacdos } |
Max  : 15 kg|



Objet|Poids|Valeur|
-----|-----|------|
:material-key-variant:{ .objet }  |20|100|


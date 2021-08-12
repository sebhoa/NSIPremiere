
{% set num = 6 %}
{% set titre = "Le web"%}
{% set theme = "web" %}

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 
 
{{ titre_activite("Modèle client serveur",["video"],0) }}
<div class="centre"><iframe src="https://player.vimeo.com/video/138623558?color=b50067&title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>

En faisant vos propres recherches et en vous aidant de la vidéo ci-dessus, répondre aux questions suivantes :

1. Quand et par qui a été inventé *le Web* ?
2. Peut-on dire *Internet* à la place du *Web* ?
3. Sur quel principe de fonctionnement repose *le Web* ?


{{ titre_activite("Les éléments d'une page Web",[]) }}

{{ titre_activite("L'apparence d'une page Web",[]) }}

## Cours

{{ cours("C6/C6-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo("Corrections",[],0)}}

Corriger les erreurs dans les fragments de code HTML suivant :

1. `<h> Mon titre principal </h>`
2. `<href="http://www.wikipedia.fr">un lien vers Wikipedia</href>`
3. `<p> Ce paragraphe contient un <a href="autre_page.html">lien vers une autre page</p></a>`


{{ exo("Structurer une page Web",[]) }}





{{ exo("Modifier l'apparence d'une page web",[]) }}



{{ exo("Créer un mini-site",[]) }}

Réaliser  un mini site *Web*, en utilisant le html et les feuilles de style. Le sujet du site est au choix, par exemple : votre CV, vos films préférés, un site de recette de cuisines, un site sur un sport ou une de vos passions, ou sur une célébrité (sportif, acteur, chanteur ...) . Respecter le cahier des charges suivant :

* au moins 5 pages reliées entre elles par des liens internes et des liens vers des sites extérieurs
* au moins 5 images, attention à utiliser des images *libres de droits* ou à créer vos propres illustrations pour votre site
* au moins une page de votre site devra contenir des informations organisées sous la forme d'un tableau et donc utiliser les balises `<table>` et `<table>`.
* L'apparence du site sera uniformisé (c'est à dire que d'une page à l'autre on retrouvera les mêmes couleurs et la même présentation). Vous devrez pour cela utiliser une feuille de style dans un fichier séparé.


{% set num = 2 %}
{% set titre = "Codage des entiers et des caractères"%}
{% set theme = "typesbase"%}
{% set num_qcm = [8] %}

{% set num_exo=1 %}
{% set num_act=1 %}



{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,"Numération binaire",["papier"]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Fiche d'activité","C2/C2-act1.pdf")}}

{{ titre_activite(num_act,"Numération hexadécimale",["papier"]) }}
{% set num_act=num_act+1 %}

{{ telecharger("Fiche d'activité","C2/C2-act2.pdf")}}


{{ titre_activite(num_act,"Encodage des caractères",["video"]) }}
{% set num_act=num_act+1 %}

<div class="centre"><iframe width="560" height="315" src="https://www.youtube.com/embed/MijmeoH9LT4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe></div>
En utilisant la video ci-dessus et en faisant éventuellement vos propres recherches sur le *Web*, répondre brièvement aux questions suivantes :

1. L'encodage {{ sc("ascii")}}
    1. Combien de caractères pouvaient être codés en {{ sc("ascii") }} ?
    2. Expliquer rapidement pourquoi ce système était limité et à du être étendu
2. L'encodage Latin-1
    1. Sur combien de bits était encodé chaque caractère ?
    2. Combien de caractères au maximum étaient représentées ?
    3. Ce système était-il universel ?
3. L'encodage {{ sc("utf-8")}}
    1. Un caractère est-il toujours encodé sur le même nombre de bits ?
    2. Cet encodage est-il compatible avec l'ancienne norme {{ sc("ascii")}} ?



## Cours

{{ cours("C2/C2-cours.pdf") }}

## QCM

{{qcm_chapitre(num)}}
  
## Exercices

{{ exo(num_exo,"Passer d'une base à l'autre",[]) }}
{% set num_exo=num_exo+1 %}

Recopier et compléter le tableau de conversion suivant :

| Ecriture décimale | Ecriture binaire | Ecriture hexadécimale |
|-------------------|------------------|-----------------------|
|$(201)_{10}$   | ...           | ...               |   
|               |               |    $(EA)_{16}$    |
|$(57)_{10}$    |               |                   |
|               |$(00100001)_2$ |                   |
|$(128)_{10}$   | ...           | ...               |   
|$(163)_{10}$   | ...           | ...               |
|               |               |    $(5B)_{16}$    |   
|               |$(10010101)_2$ |                   |
|               |$(10010010)_2$ |                   |

{{ exo(num_exo,"Un peu de reflexion ...",[]) }}
{% set num_exo=num_exo+1 %}

1. Quel est le plus grand entier positif écrit en utilisant 10 chiffres en base 2 ?
2. Que peut-on dire d'un nombre dont l"écriture en base 2 ne contient qu'un seul chiffre 1 ?
3.  1. En base 10, comment reconnaît-on un nombre divisible par 10 ? 
    2. L'écriture en base 2 d'un nombre divisible par 2 se termine forcément par quel chiffre ? Justifier.
    3. De façon générale, soit $b$ un entier supérieur ou égal à 2, que peut-on dire de l'écriture en base $b$ d'un nombre divisible par $b$ .
4. En base 10, un million s'écrit avec 7 chiffres, combien en faut-il pour l'écrire en base 2 ?

{{ exo(num_exo,"Enigme",[]) }}
{% set num_exo=num_exo+1 %}
Il manque des chiffres (remplacés par des ?) dans le nombre binaire suivant : $?001??111?$

1. Retrouver les chiffres manquants en utilisant les indices suivants:
    * il n'y a pas de zéros non significatifs dans ce nombre
    * ce nombre est divisible par 2
    * il y a un nombre impair de 0 dans l'écriture binaire de ce nombre
    * l'écriture décimale de ce nombre dépasse $(355)_{10}$
2. Donner l'écriture décimale de nombre.
3. Donner son écriture hexadécimale

{{ exo(num_exo,"Enigme",["python"]) }}

1. Lancer Python en ligne de commande, comme vu dans le chapitre précédent.
2. Tester la fonction `bin` de Python, en affichant par exemple `bin(201)` et `bin(57)`. Rapprocher les résultats obtenus avec les réponses de l'exercice 1. Émettre une hypothèse sur cette fonction.
3. Valider votre hypothèse en faisant afficher l'aide de la fonction `bin`.
4. Reprendre les questions précédentes pour la fonction `hex`

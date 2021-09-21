
{% set num = 5 %}
{% set titre = "Initiation à Python avec Turtle"%}
{% set theme = "python"%}


{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Retour sur le jeu du pendu",["notebook"],0) }}

#### 1. Rappels
1. Télécharger ci-dessous le programme déjà entamé sur le jeu du pendu :
{{ telecharger("Debut du jeu du pendu","./files/C5/debut-pendu.py")}}
2. Ouvrir ce fichier dans VS Code, que nous utiliserons à présent comme éditeur
3. Relire ce fichier

#### 2. Interaction avec le joueur

Pour demander une lettre  on utilise `feuille.textinput(titre,question)` qui crée une fenêtre dans laquelle l'utilisateur peut taper sa réponse. Les paramètres `titre` et `question` permettent de spécifier le titre de cette fenêtre et d'écrire le texte de la question.
Par exemple :

```python
lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
```
 affichera :
![textinput](./images/C5/textinput.png){.imgcentre}

#### 3. A la découverte des boucles non bornées
La boucle `for`, déjà rencontrée permet de répéter des instructions un nombre **déterminé** de fois, on parle dans ce cas, de **boucles bornées**. La situation ici est différente, on ne connaît pas le nombre d'erreurs que va commettre le joueur avant de découvrir le mot. On utilise une **boucle non bornée** en spécifiant sa condition d'arrêt, en français cela donne : *tant que* le nombre d'erreurs possibles (limité à 6), n'est pas atteint répéter la demande d'une lettre. Ou encore en Python:

```python
nb_erreurs = 0
while nb_erreurs<7:
    lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
```

1. Inclure ces lignes dans le programme du pendu et constater que la boucle est pour le moment infinie puisque la variable `nb_erreurs` reste à 0.
2. Utiliser la combinaison de touches ++ctrl+c++ pour interrompre l'exécution de la boucle.

### 4. Les instructions conditionnelles

Il faut donc modifier `nb_erreurs` en fonction de la réponse du joueur : si la lettre ne fait pas partie du mot, alors on incrémente le nombre d'erreurs :
```python
nb_erreurs = 0
while nb_erreurs<7:
    lettre=feuille.textinput("Proposer une lettre","Quelle lettre proposez-vous ?")
    if lettre not in MOT:
        nb_erreurs+=1
```
Remplacer la boucle précédente par celle-ci dans le programme du pendu, et vérifier qu'à présent la boucle se termine après 7 erreurs.

### 5. Dessin du pendu correspondant au nombre d'erreurs

Compléter la boucle `while` en y écrivant une instruction conditionnelle permettant de tracer le début du pendu (en appelant la fonction `pendu_1()`) lorsque la première erreur est commise.


## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}

## Exercices

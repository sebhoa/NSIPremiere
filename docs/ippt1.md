
{% set num = 3 %}
{% set titre = "Initiation à Python avec Turtle"%}
{% set theme = "python"%}


{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Desssiner avec le module turtle",["notebook"],0) }}


{{ telecharger("Jupyter Notebook","./notebook/pendu1.ipynb")}}


{{ titre_activite("Premières fonctions",["notebook"]) }}


{{ telecharger("Jupyter Notebook","./notebook/pendu2.ipynb")}}

{{ titre_activite("Boucles",["notebook"]) }}


{{ telecharger("Jupyter Notebook","./notebook/pendu3.ipynb")}}


## Cours

{{ aff_cours(num) }}


## QCM

{{qcm_chapitre(num)}}

## Exercices

{{ exo("Quelques dessins avec turtle",[],0) }}
Ecrire un programme Python permettant de dessiner les figures suivante :
!!! Aide
    On donne le squelette de programme suivant qui servira de point de départ :
    ```python3
        import turtle
        papier = turtle.Screen()
        crayon = turtle.Turtle()
        crayon.pensize(5)
        crayon.color("navy")
    ```

1. La lettre H <br>
![lettre H](./images/C3/ex1a.png){: .imgcentre}

2. Une croix centrée sur l'origine <br>

    !!! Attention
        * La longueur totale d'une branche de couleur est de 200 pixels
        * Les couleurs des branches sont *navy* et *darkred*
        * La branche de couleur *navy* fait un angle de 45° avec l'horizontale
    ![croix centrée sur l'origine](./images/C3/ex1b.png){: .imgcentre}

3. Des cercles <br>
![cercles](./images/C3/ex1c.png){: .imgcentre}

{{ exo("Utilisation d'une fonction",[])}}

!!! Rappel
    On donne ci-dessous le code de la fonction `ligne(x1,y1,x2,y2)` vue dans l'activité 2, elle permet de tracer la ligne joignant les points d'extrémités `(x1,y1)` et `(x2,y2)`
    ```python3
        def ligne(x1,y1,x2,y2):
            crayon.penup()
            crayon.goto(x1,y1)
            crayon.pendown()
            crayon.goto(x2,y2)
    ```

1. En utilisant la fonction `ligne`, construire la grille de morpion suivante :
![Grille de morpion](./images/C3/ex2a.png){: .imgcentre}
2. Dessiner de nouveau la [lettre H de l'exercice 1](#exercice-1-quelques-dessins-avec-turtle) en vous aidant de cette fonction. 
3. Comparer les deux programmes (avec et sans fonction), qu'en pensez-vous ?

{{ exo("Ecrire une fonction",[])}}

Le but de l'exercice est de pouvoir dessiner une croix dans l'une quelconque des cases de la grille de morpion de l'exercice précédent. Comme par exemple dans la case supérieure droite tel qu'illustré ci-dessous.
![Grille de morpion avec croix](./images/C3/ex3a.png){: .imgcentre}
Les croix ont toujours la même couleur (*green*) et la même taille (des branches de longueur 40 pixels), seule la position de leur centre varie. On décide donc, d'écrire une fonction `croix(x,y)` qui trace la croix à partir du point de coordonnées `(x,y)`

1. Recopier et compléter l'écriture de la fonction croix (pour l'instant seule la branche supérieure droite est tracée):
```python3
    def croix(x,y):
        crayon.penup()
        crayon.goto(x,y)
        crayon.pendown()
        crayon.setheading(45)
        crayon.forward(40)
        ...
```
2. Utilisation de la fonction
    1. Quel appel à la fonction `croix` permet de tracer la croix se situant dans la case supérieure droite ?
    2. Quel sera le résultat de l'instruction `croix(-100,0)` ?

{{ exo("Une fonction cercle",[])}}

1. En vous inspirant de l'exercice 3, écrire une fonction `cercle(x,y)` qui permet de tracer un cercle de rayon 35 et de couleur *darkred* dans l'une quelconque des cases de la grille de morpion. Comme par exemple ci-dessous dans la case inférieure droite.
![Grille de morpion avec cercle](./images/C3/ex4a.png){: .imgcentre}
2. Reproduire la grille de morpion suivante en utilisant les fonctions `croix` et `cercle` :
![Grille de morpion avec cercle](./images/C3/ex4b.png){: .imgcentre}

{{ exo("Grille",[]) }}

Le but de l'exercice est d'utiliser les boucles pour tracer la grille suivante :
![grille](./images/C3/grille.png){: .imgcentre}

On donne le squelette de programme suivante qui fixe les paramètres du dessin et contient la fonction `ligne(x1,y1,x2,y2)` vue dans les notebooks d'activité permettant de tracer une ligne allant du point de coordonnées `(x1,y1)` au point de coordonnées `(x2,y2)`.

```python
    import turtle

    # Création du "papier" et du "crayon"
    crayon = turtle.Turtle()
    papier = turtle.Screen()
    # Taille, dimension et couleur pour le papier et le crayon
    papier.bgcolor("beige")
    papier.setup(width=500,height=500)
    crayon.color("navy")
    crayon.pensize(5)

    def ligne(x1,y1,x2,y2):
        crayon.penup()
        crayon.goto(x1,y1)
        crayon.pendown()
        crayon.goto(x2,y2)
```

1. Ecrire une boucle `for` permettant de tracer les lignes horizontales.

    !!! Aide
        En cas de difficultés, écrire le tracé normal des lignes (sans boucle). Observer vos instructions de façon à repérer les variables qui doivent être modifiées et celles qui restent fixes.

2. Ecrire une boucle `for` permettant de tracer les lignes verticales.

{{ exo("Quelques figures avec `turtle`",[]) }}
Construire les figures suivantes (le repère est là pour vous aider et ne doit pas être reproduit):

1. L'escalier
![escalier](./images/C3/escalier.png){: .imgcentre}
2. Cercles concentriques (les couleurs alternent entre `blue` et `lightblue`, le crayon a une épaisseur de 10, les cercles ont pour rayon 10,20,30, ...)
![cercles](./images/C3/cercles.png){: .imgcentre}

{{ exo("Polygone régulier",["maths"]) }}

1. Ecrire une fonction `triangle_equilateral(c)` qui trace un triangle équilatéral de côte `c` à partir de la position courante de la tortue.
2. Ecrire une fonction `carre(c)` qui trace un carré de côte `c` à partir de la position courante de la tortue.
3. Ecrire une fonction `polygone_regulier(n,c)` qui trace un polygone régulier de côte `c` à partir de la position courante de la tortue.
    
    !!! Rappel
 
        * Un polygone régulier est un polygone dont tous les côtés sont de la même longueur et tous les angles sont égaux.
        * Les angles d'un polygone régulier à $n$ côtés mesurent $\dfrac{360}{n}$

{{ exo("Drapeau",[]) }}

Le module `turtle` permet aussi de colorier des surfaces, pour cela: <br>
:octicons-triangle-right-16: on fixe la couleur de remplissage avec  `crayon.fillcolor()` <br>
:octicons-triangle-right-16: avant de commencer le dessin de la surface, on écrit `crayon.begin_fill()`<br>
:octicons-triangle-right-16: à la fin de la construction de la surface, on écrit  `crayon.end_fill()`<br>
Par exemple, pour dessiner un  cercle rempli en rouge :
```python
crayon.fillcolor("red")
crayon.begin_fill()
crayon.circle(50)
crayon.end_fill()
```

1. Ecrire et tester une fonction `rectangle_rempli(x,y,largeur,longueur,couleur)` qui trace un rectangle rempli avec la couleur `couleur`, de dimensions `largeur x longueur` et dont le coin inférieur gauche est situé au point de coordonnées `(x,y)`
2. En utilisant la fonction ci-dessus, écrire un programme Python permettant de dessiner un drapeau français de dimension `300` sur `200` (chacun des trois rectangles formant le drapeau est de dimensions `100x200`)


{{ exo("Panneau de signalisation",[]) }}
Ecrire un programme Python permettant de dessiner le panneau de signalisation de votre choix. Quelques exemples sont proposés ci-dessous.<br>
![sens interdit](./images/C3/sensinterdit.jpg){width=150px} &nbsp;
![croisement](./images/C3/croisement.svg){width=150px}  &nbsp;
![stop](./images/C3/stop.svg){width=150px}  &nbsp;
![doublesens](./images/C3/doublesens.png){width=150px} 
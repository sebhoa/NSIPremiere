
{% set num = 4 %}
{% set titre = "Recherche dans une liste"%}
{% set theme = "algorithmique"%}

 

{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite("Complexité d'un algorithme",[],0) }}


{{ telecharger("Jupyter notebook","notebook/Recherche dans une liste.ipynb")}}

{{ titre_activite("Correction d'un algorithme",[]) }}


{{ telecharger("Fiche d'activité","pdf/C4/C4-act2.pdf")}}

{{ titre_activite("Terminaison d'un algorithme",[]) }}


{{ telecharger("Fiche d'activité","pdf/C4/C4-act2.pdf")}}

## Cours

{{ cours("C4/C4-cours.pdf") }}


## QCM

{{qcm_chapitre(num)}}
 
## Exercices

{{ exo("Analyser un programme",[],0)}}
On considère la fonction Python suivante :
```python
    def cherche_position(element,liste):
        for pos in range(len(liste)):
            if liste[pos]==element:
                return pos
        return -1
```

1. Prédire la valeur renvoyée par `cherche_position("Y",["P","Y","T","H","O","N"])` puis vérifier en testant la fonction.
2. Même question pour `cherche_position("A",["P","Y","T","H","O","N"])`
3. Même question pour `cherche_position("M",["P","R","O","G","R","A","M","M","E"])`
4. Que fait cette fonction ? Ecrire sa chaîne de documentation.

{{ exo("Predire des temps d'exécution",[],)}}

1. Si un algorithme de recherche linéaire s'exécute environ en 0.002 s sur une liste de $10\,000$ éléments, en combien de temps environ devrait-il s'exécuter pour une liste de un million d'éléments ?
2. Si on double la taille d'une liste, le temps d'exécution d'un algorithme de recherche dichotomique va-t-il aussi doubler ? Justifier.

{{ exo("Puissance",["maths"],)}}
On considère la fonction Python suivante :
```python
def puissance(x,n):
    p = 1
    for k in range(n):
        p = p * x
    return p
```

1. Que fait cette fonction ? Ecrire sa chaîne de documentation.
2. Proposer des préconditions sur les arguments.
3. Montrer que l'algorithme utilisé dans cette fonction a une complexité linéaire.


{{ exo("Factorielle",["maths"]) }}

En mathématiques, on appel *factorielle* d'un entier et $n$ et on note $n!$ le produit de cet entier par tous ceux qui le précèdent à l'exception de zéro, et on convient d'autre part que $O!=1$. Par exemple : <br>
$5!= 5 \times 4 \times 3 \times 2 \times 1 = 120.$<br>
On considère la fonction Python suivante :

```python
   def factorielle(n):
       '''Renvoie factorielle de n, avec n un entier positif ou nul'''
       if n==0:
           return 1
        else:
            fact=1
            for i in range(n):
                fact=fact*i
            return fact
```

1. Ecrire une instruction `assert` permettant de vérifier que cette fonction renvoie bien 120 pour factorielle de 5.
2. On suppose qu'on appelle `factorielle(5)`, donner les valeurs prises par la variable `fact` lors des passages successifs dans la boucle `for`.
3. Vérifier que la propriété *"la variable `fact` contient $k!$ après $k$ tours de boucle"* est un invariant de boucle.
4. Que peut-on en déduire ?

{{ exo("Nombre de chiffres d'un nombre",[]) }}
On considère la fonction suivante :

```python
def nombre_chiffres(n):
    '''Renvoie le nombre de chiffres de l'entier naturel n en base 10'''
    k=0
    while n>0:
        n=n/10
        k=k+1
    return k
```

1. Ecrire un jeu de test pour cette fonction
2. Le résultat de `nombre_chiffres(0)` est-il correct ? Sinon corriger cette fonction.
3. Ajouter des préconditions sous forme d'instruction `assert` sur la variable `n`.
4. Justifier que ce programme termine en utilisant la méthode du variant de boucle.
5. Proposer une fonction similaire qui renvoie le nombre de bits nécessaire pour écrire un entier donné en base 2.


{{ exo("Suite de Syracuse et terminaison",["maths"]) }}

On peut lire sur [wikipedia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){target=_blank} que :
> *"En mathématiques, on appelle suite de Syracuse une suite d'entiers naturels définie de la manière suivante : on part d'un nombre entier strictement positif ; s’il est pair, on le divise par 2 ; s’il est impair, on le multiplie par 3 et on ajoute 1. En répétant l’opération, on obtient une suite d'entiers strictement positifs dont chacun ne dépend que de son prédécesseur.<br>
Par exemple, à partir de 14, on construit la suite des nombres : 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2… C'est ce qu'on appelle la suite de Syracuse du nombre 14."* 

1. Donner la suite de Syracuse du nombre 12.
2. Même question pour le nombre 29.
3. Ecrire une fonction `syracuse` qui renvoie la liste des valeurs de la suite de syracuse d'un entier naturel postif `n` donné en paramètre. On arrêtera notre liste dès que la valeur 1 y est ajoutée.
4. Ecrire un jeu de test pour votre fonction.
5. Recherche sur le *Web* ce qu'on appelle *conjecture de Syracuse* (ou *conjecture de Collatz*). Consulter par exemple la page [wikipedia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse){target=_blank} citée ci-dessus.
6. Que pouvez-vous en conclure sur la preuve de la terminaison de la fonction `syracuse` ?


{{ exo("Exponentiation rapide",["dur","maths"]) }}
On considère la fonction Python suivante où `x` est un nombre quelconque et `n` un entier positif :
```python
def puissance_rapide(x,n):
    p=1
    while n>0:
        if n%2==1:
            p = p *x
        x = x*x
        n = n //2
    return p
```

1. Tester cette fonction avec `x=2` et les valeurs suivantes de `n` : 4, 5, 8 et 10.
2. Que fait cette fonction ?
3. Donner les valeurs successives prises par les variables `p`, `x` et `n` lors de l'appel de cette fonction avec `x=2` et `n=9` en recopiant et en complétant le tableau suivant :

    | Variables | `p` | `x` | `n` |
    |-----------|-----|-----|-----|
    | Initialisation| 1 | 2 | 9 |
    | Tour 1 | ... | ... | ... |
    | Tour 2 | ... | ... | ... |
    | Tour 3 | ... | ... | ... |

4. Déterminer la complexité de cet algorithme (on pourra déterminer le nombre de tours de boucle nécessaire en fonction de `n`)


# Cours de NSI en Première

## Présentation générale
Parmi les thèmes du [programme officiel](https://eduscol.education.fr/2068/programmes-et-ressources-en-numerique-et-sciences-informatiques-voie-g), quatre sont traités de façon transversale sur l'année :

* <span class='projet'>{{icone("projet")}} Démarche de projet</span> 
* <span class='histoire'>{{icone("histoire")}} Histoire de l'informatique</span> 
* <span class='typesconstruits'>{{icone("typesconstruits")}}Types construits</span> 
* <span class='python'>{{icone("python")}}Langages et programmation</span>

Les contenus de ces chapitres reviennent donc régulièrement dans ceux des autres thèmes :

* {{icone("typesbase")}} Types et valeurs de base.
* {{icone("donneestable")}} Traitement de données en tables.
* {{icone("web")}} Interactions entre l'homme et la machine sur le *Web*.
* {{icone("os")}} Architectures matérielles et systèmes d'exploitation.
* {{icone("algorithmique")}} Algorithmique.


## Contenu des thèmes transversaux 

### {{ sec_titre("histoire","Histoire de l'informatique")}}

| Contenus | Capacités attendues | Commentaires
|----------|---------------------|-------------
|Événements clés de l'histoire de l'informatique|Situer dans le temps les principaux événements de l’histoire de l’informatique et leurs protagonistes.| Ces repères historiques seront construits au fur et à mesure de la présentation des concepts et techniques.

### {{ sec_titre("projet","Projet") }}

> *Une part de l'horaire de l'enseignement d'au moins un quart du total en classe de première doit être réservée à la conception et à l'élaboration de projets conduits par des groupes de deux à quatre élèves.*

### {{ sec_titre("typesconstruits","Types construits") }}

| Contenus | Capacités attendues | Commentaires
|----------|---------------------|-------------
|p-uplets. p-uplets nommés|Ecrire une fonction renvoyant un p-uplet de valeurs||
|Tableau indexé, tableau donné en compréhension|Lire et modifier les élements d'un tableau grâce à leurs index.<br> Construire un tableau par compréhension.<br> Utiliser des tableaux de tableaux pour représenter des matrices : notation `a[i][j]`.<br> Itérer sur les élements d'un tableau| Seuls les tableaux dont les éléments sont du même type sont présentés.<br>Aucune connaisance des tranches (*slices*) n'est exigible.<br> L'aspect dynamique des tableaux de Python n'est pas évoqué.<br> Python identifie listes et tableaux.<br> Il n'est pas fait référence aux tableaux de la bibliothèque Numpy.|
|Dictionnaires par clés et valeurs|Construire une entrée de dictionnaire.<br>Itérer sur les éléments d'un dictionnaire.|Il est possible de présenter les données EXIF d'une image sous la forme d'un enregistrement.<br>En Python, les p-uplets nommés sont implémentés par des dictionnaires. Utiliser les méthodes *keys()*, *values()* et *items()*.|

### {{ sec_titre("python","Langages et programmation") }}
| Contenus | Capacités attendues | Commentaires
|----------|---------------------|-------------
|Constructions élémentaires|Mettre en évidence un corpus de constructions élémentaires | Séquences, affectation, conditionnelles, boucles bornées, boucles non bornées, appels de fonction|
|Diversité et unité des langages de programmation|Repérer, dans un nouveau langage de programmation, les traits communs et les traits particuliers à ce langage| Les manières dont un même programme simple s'écrit dans différents langages sont comparées.|
|Spécification|Prototyper une fonction.<br>Décrire les préconditions sur les arguments.<br>Décrire des postconditions sur les résultats.|Des assertions peuvent être utilisées pour garantir des préconditions ou des postconditions.|
Mise au point de programmes|Utiliser des jeux de tests.|L'importance de la qualité et du nombre de tests est mise en évidence.<br>Le succès d'un jeu de tests ne garantit pas la correction d'un programme|
Utilisation de bibliothèques|Utiliser la documentation d'une bibliothèque|Aucune connaissance exhaustive d'une bibliothèque particulière n'est exigible|

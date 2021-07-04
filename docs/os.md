
{% set num = 1 %}
{% set titre = "Systèmes d'exploitation"%}
{% set theme = "os"%}
{% set num_qcm = [0,1,2,3,4,5,6,7] %}

{% set num_exo=1 %}
{% set num_act=1 %}



{{ titre_chapitre(num,titre,theme)}}
 
## Activités 

{{ titre_activite(num_act,"Découverte des OS, logiciels libres",[]) }}
{% set num_act=num_act+1 %}


1. Rendez-vous sur la  [page de téléchargement du logiciel vlc](https://www.videolan.org/vlc/index.fr.html){target=_blank}. :
    * Pourquoi faut-il télécharger une version différente de VLC suivant qu'on utilise Windows, MacOS, Linux ou Android ?
    * Pouvez vous associer chaque icône au logiciel qu'il représente ?
2. En faisant  des recherches sur le *Web*, rédiger une réponse brève aux questions suivantes :
    * Que sont Windows, MacOS, Linux et Android ?
    * Quel est le rôle de ces logiciels sur un ordinateur ?
    * Que signifie le mot **libre** dans la phrase : "*VLC est un lecteur multimédia gratuit et libre* "?

{{ titre_activite(num_act,"Initiation à la ligne de commande",[])}}
{% set num_act=num_act+1 %}


Cette initiation se fait à travers la réalisation de **missions** dans un mini jeu d'aventures. Pour démarrer cette activité

1. lancer un terminal 
2. dans ce terminal taper `./gameshell` et laisser vous guider par les instructions à l'écran
3. Parallèlement à l'exécution des missions :
    * Noter les commandes que vous utilisez et leur signification
    * Tenir à jour un plan du monde dans lequel se déroule le jeu

!!! maison "Poursuivre ce travail à la maison"
    Le but est d'atteindre la mission 15, vous pouvez  poursuivre ce travail à la maison en installant **Gameshell**, suivre les instructions que vous trouverez sur [cette page](https://linuxfr.org/news/gameshell-le-retour){target=_blank}.

## Cours

{{ cours("C1/C1-cours.pdf") }}




## QCM

{{qcm_chapitre(num)}}


## Exercices

{{ exo(num_exo,"Calendrier",["capacite"]) }}
{% set num_exo=num_exo+1 %}
1. Ouvrir un terminal et y tester la commande ``cal``
2. Lire la documentation de cette commande
3. Quel était le jour de la semaine le 26 juin 1815 ?
4. Quel commande faut-il écrire pour afficher le calendrier du mois de mai 1970 ?

{{ exo(num_exo,"Python en ligne de commande",["python"]) }}
{% set num_exo=num_exo+1 %}

Le langage Python peut être invoqué à partir de la ligne de commande, taper simplement `python` dans un terminal. L'invite de commande se transforme en `>>>`, on dit que Python est en mode console. vous pouvez quitter Python en tapant `exit()`.

1. Utiliser Python comme calculatrice <br>En mode console, Python vous fournira directement les résultats de calculs, taper par exemple  :
    1. `15+5*5`, dans quel ordre les opérations sont-elles effectuées ?
    2. `2**5`, de quelle opération s'agit-il ?

        !!! aide "Aide"
            Tester d'autres valeurs par exemple `7**2` ou `2**3` pour vous aider

    3. `20%3`  et  `20//3`, de quelle opération s'agit-il ? (tester d'autres valeurs si nécessaires)
    4. En utilisant Python, donner le résultat de $9^{10} - 10^9$.
    5. En utilisant Python, convertir 17899132 minutes en jours, heures et minutes. 

2. Obtenir de l'aide en python
    1. Tester les commandes `chr(33)`,  `chr(72)`, `chr(125)`
    2. Pour connaître l'utilité de cette commande taper `help(chr)`

{{ exo(num_exo,"Ecrire dans un fichier",[]) }}
{% set num_exo=num_exo+1 %}
!!! rappel "Rappel"
    * La commande `touch` permet de créer un fichier vide, par exemple `touch bidule.txt` crée un fichier vide nommé `bidule.txt` dans le répertoire courant.
    * La commande `cat` permet d'afficher le contenu d'un fichier dans le terminal
1. Créer un fichier vide appelé `monfichier.txt`
1. La commande `echo`
    1. Tester la commande `echo`, en tapant par exemple `echo "Bonjour tout le monde"`
    2. Pour écrire dans un fichier on peut *rediriger* la sortie de la commande `echo` à l'aide du caractère `>`. Tester en tapant par exemple `echo "NSI c'est génial !" > monfichier.txt`
    3. Afficher la contenu du fichier pour vérifier qu'il a été modifié.
2. Un éditeur de texte dans le terminal
    1. Taper la commande `nano monfichier.txt`
    2. Utiliser cet éditeur de texte minimal afin de modifier le fichier puis l'enregistrer.

        !!! aide "Aide"
            Les commandes principales s'affichent en bas de page, le caractère `^` désigne la touche ++ctrl++ 

{{ exo(num_exo,"Ranger un dossier",[]) }}
{% set num_exo=num_exo+1 %}

1. Faire une copie du répertoire `a_ranger` que vous trouverez dans le dossier partagé.
2. Lister le contenu de ce dossier, quel type de fichier contient-t-il ?
3. Dans le dossier `a_ranger`, créer les dossiers `Texte`,`Htlm` et `Python`. 
4. Déplacer les fichiers de chaque type dans le dossier correspondant

    !!! aide "Aide"
            Déplacer les fichiers un à un serait long à fastidieux. Penser à utiliser le caractère `*` qui remplace n'importe quel suite de caractère dans les noms de fichiers.

{{ exo(num_exo,"Enigme",["dur"]) }}
{% set num_exo=num_exo+1 %}
1. Trouver six lettres en utilisant uniquement la ligne de commande et les indices suivants :
    * Lettre n° 1 : "*cachée dans le dossier `EnigmeNSI` que vous trouverez dans le dossier partagé*"
    * Lettre n° 2 : "*son code {{sc("ascii")}} est 71*"
    * Lettre n° 3 : "*deuxième lettre du jour de la semaine du 23 juin 1912*"
    * Lettre n° 4 : "*La commande `wc` vous permettra de compter le nombre de caractères du fichier lettre 4 qui se trouve dans `EnigmeNSI` Diviser le résultat obtenu par 1956 pour avoir la position dans l'alphabet de la quatrième lettre"
    * Lettre n° 5 : "Lorsque cette lettre est donnée en option à la commande `cp`, elle permet de copier un dossier et tout ce qu'il contient"
    * Lettre n°6 : La taille en kilo octet du fichier `last` qui se trouve dans `/usr/bin` vous donnera le rang dans l'alphabet de la sixième lettre.
2. Remettre dans l'ordre les six lettres obtenus pour trouver le nom d'un célèbre informaticien.





import csv

QCMFILE = "qcm.csv"

    
def define_env(env):
    env.variables['transversal']=["histoire","projet","typesconstruits","python"]
    env.variables['projet'] = {"icone":":fontawesome-solid-lightbulb:","style":"projet"}
    env.variables['typesconstruits'] = {"icone":":fontawesome-solid-cubes:","style":"typesconstruits"}
    env.variables['python'] = {"icone":":fontawesome-brands-python:","style":"python"}
    env.variables['themes']={
        "histoire":"Histoire de l'informatique",
        "projet":"Projet",
        "typesbase":"Représentation des données : types et valeurs de bases",
        "typesconstruits":"Représentation des données : types construits",
        "donneestable":"Traitement de données en table",
        "web":"Interactions entre l'homme et la machine sur le web",
        "os":"Architectures matérielles et systèmes d'exploitation",
        "algorithmique":"Algorithmique",
        "python":"Langages et programmation"
    }
    env.variables['icones'] = {
        "histoire":':fontawesome-solid-university:{title="'+env.variables['themes']['histoire']+'"}',
        "projet":':fontawesome-solid-lightbulb:{title="'+env.variables['themes']['projet']+'"}',
        "typesbase":':fontawesome-solid-cube:{title="'+env.variables['themes']['typesbase']+'"}',
        "typesconstruits":':fontawesome-solid-cubes:{title="'+env.variables['themes']['typesconstruits']+'"}',
        "donneestable":':fontawesome-solid-table:{title="'+env.variables['themes']['donneestable']+'"}',
        "web":':fontawesome-solid-code:{title="'+env.variables['themes']['web']+'"}',
        "os":':fontawesome-solid-microchip:{title="'+env.variables['themes']['os']+'"}',
        "algorithmique":':fontawesome-solid-cogs:{title="'+env.variables['themes']['algorithmique']+'"}',
        "python":':fontawesome-brands-python:{title="'+env.variables['themes']['python']+'"}'
    }
    env.variables['icones_exo']={
        "dur": ":fontawesome-solid-bomb:{title='Exercice difficile'}",
        "rappel": ":fontawesome-solid-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Exercice de recherche'}",
        "capacite": ":fontawesome-solid-puzzle-piece:{title='Exercice testant une capacité du chapitre'}",
        "python": ":fontawesome-brands-python:{title='Exercice en lien avec la programmation en Python'}",
        "bac": ":fontawesome-solid-graduation-cap:{title='Exercice extrait du Bac'}",
        "maths": ":fontawesome-solid-infinity:{title='Exercice en lien avec les mathématiques'}"
    }
    env.variables['icones_act']={
        "rappel": ":fontawesome-solid-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Activité de recherche'}",
        "oral": ":fontawesome-solid-comments:{title='Activité oral'}",
        "papier": ":fontawesome-solid-edit:{title='Activité à réaliser sur feuille'}",
        "vscode": ":material-microsoft-visual-studio-code:{title='Activité utilisant VS Code'}",
        "video": ":fontawesome-solid-film:{title='Activité utilisant un support vidéo'}",
        "notebook": ":fontawesome-solid-book:{title='Activité utilisant un jupyter notebook'}",
        "python": ":fontawesome-brands-python:{title='Activité en lien avec la programmation en Python'}"
    }
    env.variables['devant_exo']=':black_small_square:'
    env.variables['devant_act']=':black_small_square:'
    env.variables['num_exo']=1
    env.variables['num_act']=1

    env.variables['progression']={
        1 : ["os","Systèmes d'exploitation",3,"os.md"],
        2 : ["typesbase","Représentation des entiers et des caractères",2,"codage.md"],
        3 : ["python","Initiation à Python avec Turtle - Partie 1",3,"ippt1.md"],
        4 : ["os","Architecture matérielle",1,"architecture.md"],
        5 : ["python","Initiation à Python avec Turtle - Partie 2",3,"ippt1.md"],
        6 : ["algorithmique","Notions d'algorithmique",2,"notionsalgo.md"],
        7 : ["donneestable","Lecture et traitement de données en table",2,"donneestable.md"],
        8 : ["web","Le web",2,"leweb.md"],
        9 : ["algorithmique","Algorithmes de tri",2,"algostri.md"],
        10 : ["typesbase","Représentation des entiers négatifs",1,"negatifs.md"],
        11: ["os","Réseau",1,"reseau.md"],
        12: ["web","Interaction dans une page web",1,"interactionweb.md"],
        13: ["algorithmique","Algorithmes gloutons",2,"gloutons.md"],
        14: ["donneestable","Fusion de tables",1,"fusiontable.md"],
        15: ["os","Interface homme-machine",2,"interface.md"],
        16: ["typesbase","Notion de nombre flottant",1,"flottant.md"],
        17: ["algorithmique","Algorithme des k plus proches voisins",2,"knn.md"]
    }

    with open(QCMFILE,"r",encoding="utf-8") as f:
        questions = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm']=questions

    
    
    env.variables['nchap']=0
    env.variables['nelements']=0
    
    # Titres des items travaillés sur l'année
    @env.macro
    def sec_titre(theme,titre):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {titre}"
    
    @env.macro
    def icone(theme):
        return env.variables.icones[theme]
    
    @env.macro
    def titre_chapitre(numero,titre,theme):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['progression'][numero][1]
        ligne=f"# <span class='numchapitre'>C{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne
    
    @env.macro
    def titre_activite(titre,licones,numero=1):
        if numero==0:
            env.variables['num_act']=1
        ligne=f"### {env.variables['devant_act']}   Activité {env.variables['num_act']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_act'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_act']=env.variables['num_act']+1
        return ligne
    

    @env.macro
    def exo(titre,licones,numero=1):
        if numero==0:
            env.variables['num_exo']=1
        ligne=f"### {env.variables['devant_exo']}   Exercice {env.variables['num_exo']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_exo'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_exo']=env.variables['num_exo']+1
        return ligne
    
    @env.macro
    def liens(fichier,type=".pdf"):
        location="./pdf/"+fichier[0:2]+"/"
        return f"[:fontawesome-solid-download:]({location}{fichier}.pdf) [:fontawesome-regular-file:]({location}{fichier}.tex)"

    @env.macro
    def telecharger(description,fichier):
        liens =f"[{description} :fontawesome-solid-download:](./{fichier})"
        liens+="{.md-button}"
        return "<span class='centre'>"+liens+"</span>"

    @env.macro
    def cours(fichier):
        ccours = '''
Vous pouvez télécharger une copie au format pdf du diaporama de synthèse de cours présenté en classe :

<span class='centre'>[Diaporama de cours :fontawesome-regular-file-pdf:](./pdf/'''+fichier+'''){.md-button}</span>
!!! warning "Attention"
    Ce diaporama ne vous donne que quelques points de repères lors de vos révisions. Il devrait être complété par la relecture attentive de vos **propres** notes de cours et par une révision approfondie des exercices.'''
        return ccours
    
    @env.macro
    def aff_cours(num):
        fichier=f'C{num}/C{num}-cours.pdf'
        return cours(fichier)

    @env.macro
    def affiche_question(num,index):
        lenonce = env.variables.qcm[num]["enonce"]
        # Traitement si enoncé sur plusieurs lignes
        nl = lenonce.find('\n')
        if nl>0:
            lenonce=lenonce.replace("\n",'"\n',1)
            lenonce=lenonce.replace("\n",'\n    ')
        else:
            lenonce+='"'
        # Traitement si image
        limg = env.variables.qcm[num]["image"]
        if limg!='':
            lenonce+=f'\n \t ![illustration](./images/C{env.variables.qcm[num]["chapitre"]}/{limg})'
            lenonce+='{: .imgcentre}\n'
        modele = f'''
!!! fabquestion "**{index}.** {lenonce}
    === "Réponses"
        - [ ] a) {env.variables.qcm[num]["reponseA"]}
        - [ ] b) {env.variables.qcm[num]["reponseB"]}
        - [ ] c) {env.variables.qcm[num]["reponseC"]}
        - [ ] d) {env.variables.qcm[num]["reponseD"]}
    === "Correction"\n'''
        for rep in "ABCD":
            clerep = "reponse"+rep
            if env.variables.qcm[num]["bonne_reponse"]==rep:
                modele+=f"        - [x] {rep.lower()}) =={env.variables.qcm[num][clerep]}== \n"
            else:
                modele+=f"        - [ ] {rep.lower()}) ~~{env.variables.qcm[num][clerep]}~~ \n"
        return modele

    @env.macro
    def affiche_qcm(liste_question):
        qcm = ""
        for index in range(len(liste_question)):
            qcm+=affiche_question(liste_question[index],index+1)
        return qcm
    
    @env.macro
    def qcm_chapitre(num_chap):
        index=1
        qcmc=""
        for num in range(len(env.variables.qcm)):
            if int(env.variables.qcm[num]["chapitre"])==num_chap:
                qcmc+=affiche_question(num,index)
                index+=1
        return qcmc

    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'

    @env.macro
    def chapitre(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[C{num}- {titre}]({lien}) | {duree}\n"

    @env.macro
    def affiche_progression():
        ret='''
| |Titre        | Durée |
|-|-------------|-------|
        '''
        for k in env.variables.progression:
           ret+=chapitre(k,env.variables['progression'][k][0],env.variables['progression'][k][1],env.variables['progression'][k][2],env.variables['progression'][k][3])
        return ret
    
    @env.macro
    def genere_nav():
        ret='''```\n'''
        for k in env.variables.progression:
            da = env.variables['progression'][k]
            ret+=f'  - "C{k}-{da[1]}" : {da[3]}\n'
        return ret+'```\n'
    
    @env.macro
    def ok():
        return ":fontawesome-solid-check:{.vert title='Compatible'}"
    
    @env.macro
    def nok():
        return ":fontawesome-solid-times:{.rouge title='Non compatible'}"

    @env.macro
    def sujets(annee):
        aff="\n"
        aff+= "|Numéro | Lien de téléchargement| Repère de l'épreuve | Nom de fichier |\n"
        aff+= "|-------|-----------------------|---------------------|----------------|\n"
        FNAME = f"./docs/officiels/Sujets/BNS{annee}/lsujet{annee}.txt"
        with open(FNAME,"r",encoding="utf-8") as f:
            nums=1
            for s in f:
                lf=s.split(",",1)
                aff+=f"|{nums}|[Sujet N°{nums}](./officiels/Sujets/BNS{annee}/{lf[0]}) | {lf[1][:-1]} | {lf[0]} |\n "
                nums+=1
        return aff
    
    

    



    

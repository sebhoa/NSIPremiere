
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
        "bac": ":fontawesome-solid-graduation-cap:{title='Exercice extrait du Bac'}"
    }
    env.variables['icones_act']={
        "rappel": ":fontawesome-solid-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Activité de recherche'}",
        "oral": ":fontawesome-regular-comment:{title='Activité oral'}",
        "papier": ":fontawesome-solid-edit:{title='Activité à réaliser sur feuille'}",
        "vscode": ":material-microsoft-visual-studio-code:{title='Activité utilisant VS Code'}",
        "video": ":fontawesome-solid-film:{title='Activité utilisant un support vidéo'}"
    }
    env.variables['devant_exo']=':black_small_square:'
    env.variables['devant_act']=':black_small_square:'

    with open(QCMFILE,"r",encoding="utf-8") as f:
        questions = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm']=questions

   
    
    env.variables['nchap']=0
    env.variables['nelements']=0
    
    # Titres des items travaillés sur l'année
    @env.macro
    def sec_titre(theme,titre):
            icone = env.variables.icones[theme]
            if theme in env.variables["transversal"]:
                return f"<span class='{theme}'> {icone} &nbsp; {titre} </span>"
            else:
                return f"{icone} &nbsp; {titre}"
    
    @env.macro
    def chapitre(theme,titre,duree):
        env.variables['nchap']+=1
        icone = env.variables["icones"][theme]
        num = env.variables['nchap']
        return f"|{icone}|[C{num}- {titre}](#C{num}) | {duree}"
    
    @env.macro
    def icone(theme):
        return env.variables.icones[theme]
    
    @env.macro
    def titre_chapitre(numero,titre,theme):
        # Position de l'ancre pour repérage dans la page
        ligne=f"# <span class='numchapitre'>C{numero}</span> {titre} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne
    
    @env.macro
    def titre_activite(numero,titre,licones):
        ligne=f"### {env.variables['devant_act']}   Activité {numero} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_act'][icone]}</span>"
            ligne+="</span>"
        return ligne
    

    @env.macro
    def exo(numero,titre,licones):
        ligne=f"### {env.variables['devant_exo']}   Exercice {numero} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_exo'][icone]}</span>"
            ligne+="</span>"
        return ligne
    
    @env.macro
    def liens(fichier,type=".pdf"):
        location="./pdf/"+fichier[0:2]+"/"
        return f"[:fontawesome-solid-download:]({location}{fichier}.pdf) [:fontawesome-regular-file:]({location}{fichier}.tex)"

    @env.macro
    def telecharger(description,fichier):
        liens =f"[{description} :fontawesome-solid-download:](./pdf/{fichier})"
        liens+="{.md-button}"
        return liens

    @env.macro
    def cours(fichier):
        ccours = '''
Vous pouvez télécharger une copie au format pdf du diaporama de synthèse de cours présenté en classe :

[Diaporama de cours :fontawesome-solid-download:](./pdf/'''+fichier+'''){.md-button}
!!! warning "Attention"
    Ce diaporama ne vous donne que quelques points de repères lors de vos révisions. Il devrait être complété par la relecture attentive de vos **propres** notes de cours et par une révision approfondie des exercices.'''
        return ccours

    @env.macro
    def affiche_question(num,index):
        modele = f'''
!!! fabquestion "**{index}.** {env.variables.qcm[num]["enonce"]}"
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
        f= open("resultat.txt","w")
        f.write(modele)
        f.close()
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
        print("Nombre questions : ",len(env.variables.qcm))
        for num in range(len(env.variables.qcm)):
            if int(env.variables.qcm[num]["chapitre"])==num_chap:
                qcmc+=affiche_question(num,index)
                index+=1
        return qcmc

    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'


    



    

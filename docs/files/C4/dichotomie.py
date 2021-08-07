
def recherche_dichotomie(element,liste):
    debut = 0
    fin = len(liste)-1
    while fin-debut>0:
        milieu = (debut+fin)//2
        print(debut,fin,milieu)
        if element>liste[milieu]:
            debut=milieu+1
        else:
            fin=milieu
    print(debut,fin,milieu)
    if element==liste[debut]:
        return True
    else:
        return False

print(recherche_dichotomie(4,[1,4,7,12,13,14]))
classeur = {
    "positif": [],
    "negatif": []
}

def ranger(classeur, nombre):
    # classeur : dictionnaire taille 2
    #nombre : int 
    #range nombre dans "positif" ou "négatif" de classeur selon le signe
    num = int(input("entrer un nombre pour le ranger"))
    if num <= 0:
              classeur["négatif"] = num
    else:
        classeur["positif"] = num

    return classeur

def trier(classeur, nombre):
    if nombre >0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)

    return classeur
        

trier(classeur, -4)
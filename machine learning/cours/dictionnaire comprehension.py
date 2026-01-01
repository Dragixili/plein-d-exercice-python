liste_2 = [i**2 for i in range(10)]

liste_2 = [i**2 for i in range(10)]#ceci s'appele une liste compréhension
print(liste_2)

import time
start = time.time()

liste_1 = []
for i in range(1000000):
    liste_1.append(i**2)

end = time.time()
print(end-start)

#plus rapide
start = time.time()

liste_2 = [i**2 for i in range(1000000)]

end = time.time()
print(end-start)

liste_3 = [[i for i in range(3)]for j in range(3)]#permet de faire une nested liste (liste dans une liste qu'on multiplie)
liste_3

dictionnaire = {'0': 'pierre',
                '1': 'jean',
                '2': 'julie',
                '3': 'sophie'}

prenoms = ['pierre', 'jean', 'julie', 'sophie']

dico = {k:v for k, v in enumerate(prenoms)}#k:v permet de créer un dictionnaire avec une dictionnaire compréhension
print(dico)

dico.keys()

dico.values()

ages = [24, 35, 78 ,12]


dico_2 = {prenom:age for prenom, age in zip(prenoms, ages) if age > 30}#on peut mettre une condition


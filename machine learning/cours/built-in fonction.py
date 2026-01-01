#fonction les plus utilisé en machine learning
abs()#donne la valeur absolue
all()#retourne True seulement si tous les éléments sont = True , ps obligatoire d'étre sur des booléens 
any()#retourne True quand au moins un élément de la liste = True , ps obligatoire d'étre sur des booléens ex(0 = false)liste avec des nombres
bin()
dict()
float()
format()
hex()
input()
int()
list()
len()#donne la longueur de la liste
max()#donne le nombre max dans une liste
min()#donne le nombre min dans une liste
oct()
open()
round()#arrondi à l'unité
str()
sum()#somme de tout les éléments d'une liste
tuple()
type()#retourne le type de la variable

##variable
#on ne peut pas tout convertir en tout
int()#nombre entier
float()#nombre décimal
str()#chaine de caractère

## structure de données

dict()
list()
set()
tuple()

##binaire

bin()
bytes()
hex()
oct()

liste_1 = [0, 45, 57, 89]

tuple_1 = tuple(liste_1)

list(tuple_1)

inventaire = {
    "banane": 35678,
    "pommes": 4563,
    "poires": 58578
}

list(inventaire.keys())

x = int(input("donne l'argent batard"))

x += 10
x
type(x)

#on va remplacé les endroits qu'on veut rendre dynamique par des variable
#pour cela {} à l'endroit et à la fin .format(x, y) dans l'ordre des accolades
#deuxième méthode on utilise f avant le message puis on rentre entre les accolades les variables
x = 40
ville =  "paris"
message = f"la temp est de {x} degC à {ville}".format(x, ville)
print(message)

import numpy as np

parametres = {
    "W1": np.random.randn(2,4),
    "b1": np.zeros((2,1)),
    "W2": np.random.randn(2,2),
    "b2": np.zeros((2,1))
}

for i in range(1,3):
    print("couche", i)
    print(parametres["W"+str(i)])

#on ouvre un ficher et on lui assigne le mode w qui permet d'ouvrir et écrire dans le ficher
f = open('fichier.txt', 'w')

f.write('bonjour')#permet d'écrire dans le ficher
f.close()#ferme le fichier

#r permet d'ouvrir et de lire
f = open('fichier.txt', 'r')
f.read()

with open('fichier.txt', 'r') as f:#pas besoin d'utiliser close car dès le retour à la ligne le ficher se ferme
    print(f.read())

liste_1 = []
with open('fichier.txt', 'w') as f:
    for i in range(10):
        f.write("{}^2 = {} \n".format(i, i**2))#\n permet de revenir à la ligne
        liste_1.append("{}^2 = {}".format(i, i**2))

print(liste_1)

with open('fichier.txt', 'r') as f:
    liste = f.read().splitlines()#splitlines permt d'enlever le retour à la ligne en feqant comprendre à la machine directement
liste

liste_2 = [line.strip() for line in open('fichier.txt', 'r')]
liste_2 #.strip fait que l'ordinateur ne comprend plus \n
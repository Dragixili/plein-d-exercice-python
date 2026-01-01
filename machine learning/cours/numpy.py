# l'attribut shape donne un tuple on peut donc chercher les vlaeurs 
#comme dansune liste
#shape est un attribut immutable
#regarder la doc numpy
import numpy as np

## les constructeurs

#A =  np.array([1, 2, 3])
# ne oas oublié les crochets

# retenir surtout les attribut size et shape pour commencer

B = np.zeros((3, 2)) # ne pas oublié les deuxième paranthèse c'est un tuple
# B est un tableau rempli de zero
# (3, 2) indique le shape du tableau

C = np.ones((3, 4))
# que avec des 1

#lattribut size donne le nombre de valeur dans le tableau
#c'est = au produit des nombre shape

D = np.full((2, 3),7)
# pas souvent utilisé mais permet de remplacer les valeur du tableu par le 
#nombre après les paranthèse tel que 7 dans l'exemple

np.random.randn(3, 4)
#extremement utilisé car créer un tableu avec des valeurs aléatoire centré 
# en 0 (the standard normal distribution curve)
#cette attribut donne des nombres différents après chaque fois qu'on relance le tableau
#pour le fixer on utilise l'attribut seed comme
np.random.seed(0)

np.eye(4)
#cela créer une matrice identité peu utilisé en machine learning
#4 est le nombre que l'on veut avoir sur la diagonale

np.linspace(0, 10, 20)
# + utilisé, il crée un tableau a une dimension avec (un début, une fin, quantité)
#il va répartir sur 20 valeur les calur de 0 a 10 en fesant que chaqu'un des nombres
# est le même ecart tout le temps( le pas)

np.arange(0, 10, 1)
# à l'inverse le 1 cette fois et le pas que l'on fait(début, fin ,pas)

np.linspace(0, 10, 20, dtype=np.float16)
# ce dtype peut être ajputer à tout les constructeru et permet de choisir le nombre
# de bytes que vont prendre nos valeur dans notre mémoire.
# donc plus elle est petite come 16 bytes alors plus le programme va s'éxécuter
# rapidement au contraire un tableau à 64 bytes prendra plus de tmps à ce générer
# utilisé très souvent, ( souvent on garde celui de bas mais le changer peut aider
# à créer un modèle plus rapide à entrainer)

##Manipulation

A = np.zeros((3, 2))
B = np.ones((3, 2))

C = np.hstack((A, B))
#hstack va permetre de de coller nos tableau en 1
# h pour horizontal soit on le colle surt le coté droit
# la structure est np.hstack((Array.A, Array.B))

C.shape 
# nous donne un tableau à toujour 3 colone mais 4 ligne maintenant

D = np.vstack((A, B))
# cette fois on les colle sur le verticale avec le : v
#le tableau après un shape fait (6, 2)

np.concatenate((A, B), axis=0)
# exactement le même résultat que le stack mais on précise l'axe sur 
#lequel on veut les collé 0 comme vstack et 1 comme hstack


# pas besoin de connaître les deux seules une des deux suffie au début 
# plutôt concatenate car si on veut passer en 3 dimensions alors il
# suffit de mettre 2 à l'axis et également cela aidera à la meilleur
# compréhension du système d'axe

D = D.reshape((3,4))
#permet de modifiere le shape d'un tableau ( attention: que si les sizes sont =)
# exemple D(6, 2) peur devenir D(3, 4) car les sizes sont = à 12
# attention également cela change la forme d'on les nombres sont ordonnés

A = np.array([1, 2, 3])
A.shape
#ce code donnera (3,)
# le reshape et alors intérésant car ne pas avoir de valeur après la 
# virgle peut poser problème dans certain code alors on aimerai mettre un 1 après

A = A.reshape((A.shape[0], 1))
A.shape 
# pour résoudre on redimentionne et vu que c'est un tuple on peut y accéder
# avec de l'indexing soit A.shape[0] va récuperer 3 comme valeur 
# extrémement utile pour des calcul matriciel, somme sur certain axe

A = A.squeeze()
# .squeeze permet d'enlever tout les axe où il y a des 1
# cela peut être utile pour certain domaine d'avoir un tableau à 1 axe

D.ravel()
# permet d'applatir un tableau pour qu'il fasse 1 dimension 
# le tableau sera rangé de droite à gauche de haut en bas les 1 après les autres
# cela modifie donc l'odre des valeurs
D.shape 
#donnera (12,)
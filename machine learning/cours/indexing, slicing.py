import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

A[1, 1] 
#indexing

A[0,:] 
# : signifie tout

A[1]
# sacahnt que de base on travail sur l'axe x si on ne lui mets qu'une valeur alors
#il va prendre toute la ligne horizontal d'index 1 l'à : 4 5 6

A [0:2,0:2]
# ici on séléctionne un bloc 0:2 comme début:fin (le 2 c'est l'index de fin il 
# n'est pas pris en compte lors de l'affichage c'les la valeur juste avant qui apparaît)

B = A[0:3, 0:3]
# cela créer un nouveau tableau appartir des valeurs

A[0:2,0:2] = 10 
# permet de remplacer les valeur du carré par des 10

A[:, -2:]
#le -2 permet de partir de la fin et de prendre les deux dernière 

B = np.zeros((4, 4))

B[1:3,1:3] = 1 
# on a pu remplacer le centre du tableau par des 1

C = np.zeros((5, 5))
C[::2, ::2] = 1
# le :: prmet de dire du début à la fin et le deux indique le pas

D = np.random.randint(0, 10, [5, 5])
# créer u tableau de 5 par 5 avec des valeurs de 1 à 10
D < 5
# vérifie par un true ou un false si chacun des nombres du tableau est en dessous
# ou au dessus de 5

D[D<5] = 10
# va remplacer les valeur inférieur à 5 par des 10
# très utile

D[(D<5) & (D>2)] = 10
# possibilité de véifier plusieurs conditions


E = np.random.randint(0, 255,[1024, 720])
E[E>200] = 255

# on peut également comme dans une image changer certaine portion de couleur en une autre
# comme avec des pixels déjà un peu foncé qui deviendrai automatiquement noirs

E[E<5]
#retourne un tableau à 1 dimension contenant les nombres du tableau <5

E[E<5].shape
# nous donne une shape de 14473 alors que celle du tableau de base et de 
# 737280 ce qui veut dire qu'on filtre les nombres du tableau

F = np.random.randn(5, 5)
F[D<5]
# on peut utiliser le boolean index d'un autre tableau pour vérifier le notre
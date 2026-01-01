'''liste_1 = [1, 4 , 7, 8]
villes = [ 'paris', ' tokio', 'londres']
liste_2 = [liste_1, villes]
liste_3 = []'''

villes = ['londre', 'paris', 'lisbonne', 'damas']
villes.append('dublin')#ajoute l'élément a la fin
print(villes)

villes.insert(2,'Madrid')#ajoute l'élément a la place de l'index donné [2, 'madrid]
print(villes)

villes_2 = ['amesterdame', 'rome']
villes.extend(villes_2)#ajoute une liste a la fin d'une autre liste
print(villes)

print(len(villes))#nombre de valeur dans une liste

villes.sort(reverse=True)#sort va trier dans le sens alphabétique et le reverse true va inversé le sens de l'alphabet
print(villes)

#cela marche aussi avec les chiffres
listes_2 = [1, 2, 4, 19, 5, 6]
listes_2.sort()
print(listes_2)

villes.count('paris')#permet de compter le nombre de fois qu'un élément apparait dans une liste
print(villes.count('paris'))

villes[3] = 'paris'#on a ajouter une fois paris ce qui a modifier le nombre d'apparitionb de paris dans la liste
print(villes.count('paris'))

if 'paris' in villes:#vérifie si il y a un élément dans une liste
    print("oui")
else:
    print("non")

for index, valeur in enumerate(villes):#permet d'énumer l'index
    print(index, valeur)

for a, b in zip(villes, listes_2):# zip permet d'aller chercher dans deux listes différente
    print(a, b)


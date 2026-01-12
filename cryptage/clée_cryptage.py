import secrets

alphabet = [chr(i) for i in range(32,127)]
nombre = list(range(len(alphabet)))

clé = {}
clé_décrypte = {}

crypté = ""
décrypté = ""

for i in alphabet:
    valeur = secrets.choice(nombre)
    nombre.remove(valeur)
    clé[i] = alphabet[valeur]
    
message = input(">>> Entrer le message à crypter : ")

for i in message:
    crypté += clé[i]
print(crypté)


for i in clé.keys():
    clé_décrypte[clé[i]] = i

for i in crypté:
    décrypté += clé_décrypte[i]
print(décrypté)






    
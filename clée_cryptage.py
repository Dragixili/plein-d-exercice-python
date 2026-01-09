import random
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
clé = {}
for i in alphabet:
    valeur = random.randrange(0,25)
    clé[i] = alphabet[valeur]
print(clé)
message = input(">>> Entrer le message à crypter : ")
crypté = ""
for i in message:
    crypté += clé[i]
print(crypté)
    
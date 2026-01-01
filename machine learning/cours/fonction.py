f = lambda  x, y: x**2 + y



def e_potentielle_limite(masse, hauteur, limite, g=9.81):#argument dans les paranthèse
    E = masse * hauteur * g
    #print(E)
    return E < limite
    

print('bonjour')
resultat = e_potentielle_limite(masse=80,hauteur=5, limite=3500)

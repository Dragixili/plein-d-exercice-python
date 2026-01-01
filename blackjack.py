import random

class carte:
    def __init__(self, valeur, symbole):
        self.valeur = valeur
        self.symbole = symbole

    def __repr__(self):
        return f"{self.valeur} de {self.symbole}"
    
class deck:
    def __init__(self):
        self.cartes = []
        for symbole in ['carreau', 'coeur', 'pique', 'trèfle']:
            for valeur in (2, 11):
                self.cartes.append(carte(str(valeur), symbole))
            for valeur in ['Valet', 'Dame', 'Roi', 'As']:
                self.cartes.append(carte(valeur, symbole))
        random.shuffle(self.cartes)

    def tirer_une_carte(self):
        if len(self.cartes) == 0:
            return None
        return self.cartes.pop()











import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import ConciseDateFormatter
import re

# faire un graphe de l'évolution des prix


url = "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_ref_est_in20028007.html"
url_2 = "https://www.topachat.com/pages/detail2_cat_est_micro_puis_rubrique_est_wgfx_pcie_puis_ref_est_in20027904.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

response_2 = requests.get(url_2, headers=headers)
response_2.encoding = 'utf-8'
soup_2 = BeautifulSoup(response_2.text, 'html.parser')

# Nom du produit
title_tag = soup.find('h1')
title = title_tag.get_text(strip=True) if title_tag else "Nom non trouvé"

title_tag_2 = soup_2.find('h1')
title_2 = title_tag_2.get_text(strip=True) if title_tag_2 else "Nom non trouvé"

# Prix (uniquement le texte direct, sans enfants)
price_tag = soup.find('div', class_='offer-price__price')
price_tag_2 = soup_2.find('div', class_='offer-price__price')

# ---- Récupération du prix principal ----
if price_tag:
    if price_tag.string:
        price = price_tag.string.strip()
    else:
        price = price_tag.get_text(strip=True, separator=' ').split("dont")[0].strip()
        price = price.replace('\xa0', ' ').replace('�', '€')
else:
    price = "0"

price_clean = re.sub(r"[^0-9.,]", "", price).replace(",", ".")
price = float(price_clean) if price_clean else 0.0

# ---- Récupération du prix principal ----
if price_tag_2:
    if price_tag_2.string:
        price_2 = price_tag_2.string.strip()
    else:
        price_2 = price_tag_2.get_text(strip=True, separator=' ').split("dont")[0].strip()
        price_2 = price_2.replace('\xa0', ' ').replace('�', '€')
else:
    price_2 = "0"

# Nettoyage du prix -> float
price_clean_2 = re.sub(r"[^0-9.,]", "", price_2).replace(",", ".")
price_2 = float(price_clean_2) if price_clean_2 else 0.0

# Affichage

print("Nom du produit :", title)
print("Prix :", price)

print("Nom du produit :", title_2)
print("Prix :", price_2)

x = 0
date = []
prix = []
prix_list_2 = []

## DATE
try:
    with open("dates.txt", "r") as f:
        for ligne in f:
            date.append(ligne.strip())
except FileNotFoundError:
    pass  # si le fichier n'existe pas encore

# ajouter la nouvelle date du jour si pas déjà dedans
a = str(datetime.now().date())
if a not in date:
    date.append(a)
    prix.append(price)           # ajouter le prix du jour
    prix_list_2.append(price_2)  # ajouter le prix du jour produit 2
    x = 1


# réécrire le fichier sans doublons
with open("dates.txt", "w") as f:
    for valeur in date:
        f.write(valeur + "\n")


## PRIX 1
try:
    with open("prix.txt", "r") as f:
        for ligne in f:
            propre = re.sub(r"[^0-9.,]", "", ligne.strip()).replace(",", ".")
            if propre:
                prix.append(float(propre))  # convertir en nombre
except FileNotFoundError:
    pass

if x == 1:
    prix.append(price)

# 🔥 sauvegarde produit 1
with open("prix.txt", "w") as f:
    for valeur in prix:
        f.write(str(valeur) + "\n")


## PRIX 2
try:
    with open("prix_2.txt", "r") as f:
        for ligne in f:
            propre = re.sub(r"[^0-9.,]", "", ligne.strip()).replace(",", ".")
            if propre:
                prix_list_2.append(float(propre))  # convertir en nombre
except FileNotFoundError:
    pass

if x == 1:
    prix_list_2.append(price_2)

# 🔥 sauvegarde produit 2
with open("prix_2.txt", "w") as f:
    for valeur in prix_list_2:
        f.write(str(valeur) + "\n")


plt.plot(date, prix, marker='o', label=title)
plt.plot(date, prix_list_2, marker='o', label=title_2)

plt.xlabel("Date")
plt.ylabel("Prix (€)")
plt.title("Évolution des prix")
plt.legend()
plt.grid()
plt.show()


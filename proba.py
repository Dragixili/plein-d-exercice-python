import random

j = 1000000
dés = [1,2,3,4,5,6]
résultat = []

prob_1 = 0
prob_2 = 0
prob_3 = 0
prob_4 = 0
prob_5 = 0
prob_6 = 0

for i in range(0,j):
    tirage = random.randrange(0,len(dés))
    itération = dés[tirage]
    résultat.append(itération)
    
for i in résultat:
    if i == 1:
        prob_1 += 1
    elif i == 2:
        prob_2 += 1
    elif i == 3:
        prob_3 += 1
    elif i == 4:
        prob_4 += 1
    elif i == 5:
        prob_5 += 1
    else:
        prob_6 += 1
        
prob_1 /= j
prob_2 /= j
prob_3 /= j
prob_4 /= j
prob_5 /= j
prob_6 /= j


print(prob_1,prob_2,prob_3,prob_4,prob_5,prob_6)
    
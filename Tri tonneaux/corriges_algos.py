from activite_tonneaux import *

nb_tonneaux = 8

init(nb_tonneaux, speed = 0)


# Bulle 
for i in range(0, nb_tonneaux-1):
    for k in range(1, nb_tonneaux-i):
        if plus_lourd(k-1, k) == k-1:
            echanger(k,k-1)


# Insertion
for i in range(1, nb_tonneaux):
    k = i
    
    while k > 0 and plus_lourd(k-1, k) == k-1:
        echanger(k,k-1)
        k = k - 1
        
# Sélection
for i in range(nb_tonneaux):
    lighter = i
    for k in range(i+1,nb_tonneaux):
        if plus_lourd(lighter, k) == lighter:
            lighter = k
    echanger(i,lighter)

# Cocktail 
for i in range(0, nb_tonneaux//2):
    for k in range(1, nb_tonneaux-i):
        if plus_lourd(k-1, k) == k-1:
            echanger(k,k-1)
    for k in range(nb_tonneaux-i-1, 1, -1):
        if plus_lourd(k-1, k) == k-1:
            echanger(k,k-1)


fin_activite()
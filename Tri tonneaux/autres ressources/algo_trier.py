from activite_tonneaux import *

nb_tonneaux = 10

init(nb_tonneaux)
initObjects()
etagere_vers_plateau_g(1)
etagere_vers_plateau_d(3)
if peser_tonneau() == -1:
    print("le tonneau de gauche est le plus lourd")
elif peser_tonneau() == +1:
    print("le tonneau de doite est le plus lourd")
else:
    print("les tonneaux ont le même poids")

plateau_d_vers_etagere(3)

fin_activite()
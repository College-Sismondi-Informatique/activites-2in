from activite_tonneaux import *

nb_tonneaux = 10

init(nb_tonneaux)
initObjects()

for i in range(0, nb_tonneaux-1):

    for k in range(i+1, nb_tonneaux):
        etagere_vers_plateau_g(i)
        etagere_vers_plateau_d(k)
        if peser_tonneau() == 1:
            plateau_g_vers_etagere(i)
            plateau_d_vers_etagere(k)
        else:
            plateau_g_vers_etagere(k)
            plateau_d_vers_etagere(i)
        

fin_activite()
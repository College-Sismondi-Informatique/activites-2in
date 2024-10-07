from activite_tonneaux import *

nb_tonneaux = 10

init(nb_tonneaux)
initObjects()


for k in range(1, nb_tonneaux):
    etagere_vers_plateau_g(0)
    etagere_vers_plateau_d(k)
    if peser_tonneau() == 1:
        plateau_g_vers_etagere(0)
        plateau_d_vers_etagere(k)
    else:
        plateau_g_vers_etagere(k)
        plateau_d_vers_etagere(0)
        

fin_activite()
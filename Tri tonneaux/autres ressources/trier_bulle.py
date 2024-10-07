from activite_tonneaux import *

nb_tonneaux = 10

init(nb_tonneaux)
initObjects()

for i in range(0, nb_tonneaux-1):

    for k in range(1, nb_tonneaux-i):
        etagere_vers_plateau_g(k-1)
        etagere_vers_plateau_d(k)
        if peser_tonneau() == -1:
            plateau_g_vers_etagere(k-1)
            plateau_d_vers_etagere(k)
        else:
            plateau_g_vers_etagere(k)
            plateau_d_vers_etagere(k-1)
        
        

fin_activite()
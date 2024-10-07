from activite_tonneaux import *

nb_tonneaux = 10

init(nb_tonneaux)
initObjects()

for i in range(1, nb_tonneaux):

    etagere_vers_plateau_d(i)
    k = i-1
    etagere_vers_plateau_g(k)

    while peser_tonneau() == -1 and k > 0:
        plateau_g_vers_etagere(k+1)
        k = k - 1
        etagere_vers_plateau_g(k)
        
    plateau_d_vers_etagere(k)
    plateau_g_vers_etagere(k+1)
        
        

fin_activite()

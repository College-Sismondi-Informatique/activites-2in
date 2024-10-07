# pour pouvoir utiliser le module
from activite_tonneaux import *

nb_tonneaux = 5

# pour initialiser l'environnement avec le bon nombre de tonneaux
init(nb_tonneaux)
initObjects()

# on met le tonneau à la position 1 sur le plateau de gauche
etagere_vers_plateau_g(1)

# on met le tonneau à la position 3 sur le plateau de droite
etagere_vers_plateau_d(3)

# on compare le poids des tonneaux sur la balance 
p = peser_tonneau() 

if p == -1:
    # le tonneau de gauche est le plus lourd, on les remet à leur place
    print("le tonneau de gauche est le plus lourd")
    plateau_g_vers_etagere(1)
    plateau_d_vers_etagere(3)
elif p == +1:
    # le tonneau de droite est le plus lourd, on permute les places
    print("le tonneau de droite est le plus lourd")
    plateau_g_vers_etagere(3)
    plateau_d_vers_etagere(1)
elif p == 0:
    # ils ont le même poids, on les remet à leur place
    print("les tonneaux ont le même poids")
    plateau_g_vers_etagere(1)
    plateau_d_vers_etagere(3)

plateau_d_vers_etagere(3)

# Obligatoire à la fin du programme pour vérifier que les tonneaux sont bien triés
fin_activite()
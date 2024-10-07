from random import randint
import time
import pygame
from enum import Enum
import random 

# GLOBAL VARIABLES 
COLOR = (255, 100, 98) 
SURFACE_COLOR = (230, 230, 230) 
WIDTH = 600
HEIGHT = 300
POS_BALANCE = (200, 100)

RED = 200, 0, 0
BLACK = 0, 0, 0
GREEN = 0, 200, 0
DARKGREEN = 0, 100, 0
DARKBLUE = (0, 0, 128)

MAX_POIDS = 99

BARREL_SPRITE = pygame.image.load('images/barrel.png')
BALANCE_MILIEU = pygame.image.load('images/balance_milieu.png')
BALANCE_GAUCHE = pygame.image.load('images/balance_gauche.png')
BALANCE_DROIT = pygame.image.load('images/balance_droite.png')

pauseLength = 0.001

TRACE = False

class TonneauEtat(Enum):
    PLATEAU_GAUCHE = 1
    PLATEAU_DROIT = 2
    ETAGERE = 3
    NOTFOUND = 4

class Tonneau(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.font.init()
        super().__init__()         

        self.poids = randint(1, MAX_POIDS)

        self.image = BARREL_SPRITE.copy()

        # c'est le rectangle qui encapsule l'image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x,y)
        
        # afficher le numéro
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = self.font.render(str(self.poids), False, (255, 255, 255))
        image_center = self.image.get_rect().center
        self.image.blit(self.text, self.text.get_rect(center = image_center))

class Etagere(pygame.sprite.Sprite):
    def __init__(self, n): 
        super().__init__()
        tonneaux = [Tonneau(40+50*k, HEIGHT-20) for k in range(n)]
        
    def est_triee(self):
        for k in range(len(self.tonneaux)-1):
            if self.tonneaux[k] == None:
                show_message("Il n'y a pas de tonneau à la position " + str(k))
                return False
            elif self.tonneaux[k+1] == None:
                show_message("Il n'y a pas de tonneau à la position " + str(k+1))
                return False
            if self.tonneaux[k].poids > self.tonneaux[k+1].poids:
                show_message("tonneau à la position " + str(k) +
                             " plus grand que le tonneau à la position "+ str(k+1))
                return False
        return True

class Balance(pygame.sprite.Sprite):
    def __init__(self, x,y): 
        super().__init__()         

        self.image = BALANCE_MILIEU
        
        # c'est le rectangle qui encapsule l'image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Créer les tonneau
        self.tonneau_g = None
        self.tonneau_d = None
        
        self.etat = 0 # 0 pas peser, -1 gauche, +1 droit

    def pese(self):
        '''
            return : etat
        '''
        # pas besoin de repeser 
        if self.etat != 0:
            return self.etat
            
        if self.tonneau_g != None and self.tonneau_d != None:
            if self.tonneau_g.poids < self.tonneau_d.poids:
                self.image = BALANCE_DROIT
                self.tonneau_g.rect.y -= 10
                self.tonneau_d.rect.y += 10
                if TRACE:
                    print("droit")
                self.etat = +1
                
            elif self.tonneau_g.poids > self.tonneau_d.poids:   
                self.image = BALANCE_GAUCHE
                self.tonneau_g.rect.y += 10
                self.tonneau_d.rect.y -= 10
                if TRACE:
                    print("gauche")
                self.etat = -1
            else :
                self.etat = 0
                
        return self.etat
                
            
    def pos_tonneau_g(self, t_g):
        self.tonneau_g = t_g
        
    def pos_tonneau_d(self, t_d):
        self.tonneau_d = t_d

    def enlever_tonneau_g(self):
        t = self.tonneau_g
        self.tonneau_g = None
        
        # remettre l'équilibre
        if self.etat != 0 :
            self.image = BALANCE_MILIEU
            if self.etat != -1 :
                self.tonneau_d.rect.y -= 10
            else:
                self.tonneau_d.rect.y += 10
            self.etat = 0
        
        return t
    
    def enlever_tonneau_d(self):
        t = self.tonneau_d
        self.tonneau_d = None
        # remettre l'équilibre
        if self.etat != 0 :
            self.image = BALANCE_MILIEU
            if self.etat != -1 :
                self.tonneau_g.rect.y += 10
            else:
                self.tonneau_g.rect.y -= 10
            self.etat = 0
        return t
        
def show_message(m):
    ''' Pour afficher des messages '''
    global msg
    print(m)
    msg = m
    
def move_tonneau(t, pos):
    global msg
    while abs(t.rect.centerx - pos[0]) > 1 or abs(t.rect.bottom - pos[1]) > 1:
        if  t.rect.centerx - pos[0] >= 1:
            t.rect.centerx = t.rect.centerx -1
        else:
            t.rect.centerx = t.rect.centerx +1
        if  t.rect.bottom - pos[1] >= 1:
            t.rect.bottom = t.rect.bottom -1
        else:
            t.rect.bottom = t.rect.bottom +1
        display()
        time.sleep(pauseLength/2)
        msg = "" # on remet à zero l'affichage

def etagere_vers_plateau_g(n):
    if etagere.tonneaux[n] == None:
        show_message("Il n'y a pas de tonneau à la position "+ str(n))
    elif balance.tonneau_g != None:
        show_message("Il y a déjà un tonneau sur le plateau de gauche !")
    else:
        move_tonneau(etagere.tonneaux[n], (balance.rect.x+ 35, balance.rect.y+30))
        balance.pos_tonneau_g(etagere.tonneaux[n])
        etagere.tonneaux[n] = None

def etagere_vers_plateau_d(n):
    if etagere.tonneaux[n] == None:
        show_message("Il n'y a pas de tonneau à la position "+ str(n))
    elif balance.tonneau_d != None:
        show_message("Il y a déjà un tonneau sur le plateau de droite !")
    else:    
        move_tonneau(etagere.tonneaux[n], (balance.rect.x+ 165, balance.rect.y+30))
        balance.pos_tonneau_d(etagere.tonneaux[n])
        etagere.tonneaux[n] = None

def plateau_g_vers_etagere(n):
    if etagere.tonneaux[n] != None:
        show_message("Il y a déjà un tonneau à la position "+ str(n))
    else:
        t = balance.enlever_tonneau_g()
        if t == None:
            show_message("Pas de tonneau sur le plateau de gauche !")
        else:
            move_tonneau(t, (40+50*n, HEIGHT-20))
            etagere.tonneaux[n] = t
    
def plateau_d_vers_etagere(n):
    if etagere.tonneaux[n] != None:
        show_message("Il y a déjà un tonneau à la position "+ str(n))
    else:
        t = balance.enlever_tonneau_d()
        if t == None:
            show_message("Pas de tonneau sur le plateau de droite !")
        else:
            move_tonneau(t, (40+50*n, HEIGHT-20))
            etagere.tonneaux[n] = t


def peser_tonneau():
    r = balance.pese()
    display()
    time.sleep(pauseLength*500)
    return r

def dispText(msg):
    global screen
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(msg, True, GREEN, BLACK)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

def display():
    '''
    permet d'afficher tous les objets
    '''
    global screen, all_sprites_list, msg
    all_sprites_list.update() 
    screen.fill(SURFACE_COLOR)
#    screen.blit(BALANCE_MILIEU, POS_BALANCE)
    all_sprites_list.draw(screen)
    dispText(msg)
    pygame.display.flip()


def init(n):
    '''
        param:
            n(int) : le nombre de tonneau 
    '''
    global screen, WIDTH,POS_BALANCE, nb_tonneaux
    
    nb_tonneaux = n
    
    WIDTH = 50+50*nb_tonneaux
    POS_BALANCE = WIDTH/2 - 100, POS_BALANCE[1]
    
    # init de la fenete 
    pygame.init() 
    size = (WIDTH, HEIGHT) 
    screen = pygame.display.set_mode(size) 
    pygame.display.set_caption("Activité trier des tonneaux") 


def initObjects():
    ''' initialisation des variables globales '''
    global all_sprites_list, etagere, balance, msg
    
    msg = ""
    
    all_sprites_list = pygame.sprite.Group() 

    balance = Balance(POS_BALANCE[0], POS_BALANCE[1])
    all_sprites_list.add(balance)

    etagere = Etagere(10)
    etagere.tonneaux = [Tonneau(40+50*k, HEIGHT-20) for k in range(nb_tonneaux)]
    for t in etagere.tonneaux:
        all_sprites_list.add(t)



def fin_activite():
    
    # on vérifie si les tonneaux sont bien triés
    if etagere.est_triee():
        show_message("Félicitations, le tableau est trié!!!")
        dispText("Félicitations, le tableau est trié!!!")
    else:
        show_message("Échec, le tableau n'est pas trié...")
        dispText("Échec, le tableau n'est pas trié...")
        
    
    exit = True
    while exit: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                exit = False

        display()

    pygame.quit()    





from tkinter import *
import math
import random

#fonctions à faire :
  #(OK) # generate -> qui genere et affiche le plateau à l'aide d'un fichier txt 
  #(OK) # show_target -> qui affiche la cible 
  #(OK) # show_robots -> qui affiche les robots 
  #(OK) # keyboard -> qui permet de se déplacer (verticalement et horizontalement)
  #(OK) # deplacement -> qui permet de déplacer un robot lorsqu'on clique dessus
        # maj_pos -> qui permet de réinisialiser la position du robot 
        # clr_mvmt -> qui permet d'affichet les possibles deplacements d'un robot lorsque l'on clique dessus
  #(OK) # click -> click
  #(OK) # position -> qui permet de return une position d'une case  
        # win -> qui permet d'afficher un message lorsque l'un des robots gagne 
        # restart -> qui permet de recommencer une partie 
        # cpt -> qui permet de compter le nombre de deplacements qu'un robot a fait 
        # save -> qui permet de sauvegarder une partie
        # return -> qui permet de revenir en arriere (d'annuler son deplcement)
  #(OK) # obstacle -> qui permet d'arreter le robot lorsqu'il est devant un obstacle 
        # Unfo -> qui permet de revenir en arrière 

#constantes :
        # HEIGHT = 640
        # WIDHT = 640
        # SIZE = 16
        # COTE = 40 (HEIGHT//16)
#variable :
        # tableau = None
        # target = None
        # pos_robot = []
        # robots = []
#bouton :
        # btn_save
        # btn_load





def rectangle_automatique(leCanvas, x0,y0,largeur,hauteur,bordure,couleur1,couleur2,couleur3) :
    leCanvas.create_rectangle(x0+bordure//2, y0+bordure//2, x0+largeur-bordure//2, y0+hauteur-bordure//2, fill=couleur1, activefill=couleur2, outline=couleur3, width=bordure)

def tab():
    tab = [[]]
    for x in range (1, 640):
        for i in range (16):
            while x%16 == 0:
                i+= 1
    for y in range (1, 640):
        for j in range (len(tab[i][j])):
            while y%16 == 0:
                j+= 1

fenetre = Tk()

fenetre.title("robot ricochet")

fenetre.geometry("1000x1000")


canvas = Canvas(fenetre, width=752, height=752, bg='ivory', bd=0, highlightthickness=0)

canvas.place(x=100,y=10)

longueur, largeur = 752, 752
cote_carre = 47

for y in range(0,longueur, cote_carre) :
    for x in range(0,largeur, cote_carre) :
        rectangle_automatique(canvas, x, y, 55, 55, 2, "#ffffcc", "green", "brown")

###############################################################################################""
def robot_rouge():
    pos_robot_r = [0]
    x, y = cote_carre/2 , cote_carre/2
    rayon = 10
    pos_robot_r.append((x, y))
    cercle_rouge = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon), fill="red", command = surligne_deplac_rouge)
    return [cercle_rouge]

def robot_bleu():
    x, y = largeur-(cote_carre/2), cote_carre/2
    rayon = 10
    cercle_bleu = canvas.create_oval((x-rayon, y-rayon), (x+rayon, y + rayon), fill = "blue")
    return [cercle_bleu]

def robot_vert():
    x, y = cote_carre/2, largeur-(cote_carre/2)
    rayon = 10
    cercle_vert = canvas.create_oval((x-rayon, y-rayon), (x+rayon, y+rayon), fill = "green")
    return [cercle_vert]

def robot_jaune():
    x, y = largeur-(cote_carre/2),largeur-(cote_carre/2)
    rayon = 10
    cercle_jaune = canvas.create_oval((x-rayon, y-rayon), (x+rayon, y+rayon), fill = "yellow")
    return[cercle_jaune]

#################################################################################################

def cible_rouge():
    pass
    xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    while (xg-xd != 47) or (yg-yd != 47) and (xg%16 != 0) or (xd%16 != 0) or (yg%16 != 0) or (yd%16 != 0) :
        xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    else:
        carre_rouge = canvas.create_rectangle((xg, yg), (xd, yd), fill = "red")
        return[carre_rouge]

def cible_bleu():
    pass
    xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    while (xg-xd != 47) or (yg-yd != 47) and (xg%16 != 0) or (xd%16 != 0) or (yg%16 != 0) or (yd%16 != 0) :
        xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    else:
        carre_bleu = canvas.create_rectangle((xg, yg), (xd, yd), fill = "bleu")
        return[carre_bleu]

def cible_vert():
    pass
    xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    while (xg-xd != 47) or (yg-yd != 47) and (xg%16 != 0) or (xd%16 != 0) or (yg%16 != 0) or (yd%16 != 0) :
        xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    else:
        carre_vert = canvas.create_rectangle((xg, yg), (xd, yd), fill = "green")
        return[carre_vert]

def cible_jaune():
    pass
    xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    while (xg-xd != 47) or (yg-yd != 47) and (xg%16 != 0) or (xd%16 != 0) or (yg%16 != 0) or (yd%16 != 0) :
        xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    else:
        carre_jaune = canvas.create_rectangle((xg, yg), (xd, yd), fill = "yellow")
        return[carre_jaune]

###########################################################################################################################

def cases_restart():
    for x in range (329, 376):
        for j in range (329, 376):
            rectangle_automatique(canvas, 329, 329, 92, 92, 10, "black", "black", "black")

def restart_game(event):
    pass
    click = False
    for x in range(329, 376):
        for y in range (329, 376):
            if click == True:
                command = lambda : restart()
    canvas.bind("<Button-1>", Clic)
    return


#######################################################################################################


def surligne_deplac_rouge(rob_r):
    pass
    global pos_robot_r
    if Click == (pos_robot_r):
        for x in range (1, 752):
            for y in range (1, 752):
                x += 16
                y += 16
                canvas.bind("<Button-1>",activefill = "red")
        





    






rob_r = robot_rouge()
surligne_deplac_rouge(rob_r)
rob_b = robot_bleu()
rob_v = robot_vert()
rob_j = robot_jaune()
btn_restart = cases_restart()
#restart_game(event)
"""cib_r = cible_rouge()
cib_b = cible_bleu()
cib_v = cible_vert()
cib_j = cible_jaune()"""
fenetre.mainloop()
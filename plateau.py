from tkinter import *
import math
import random




def rectangle_automatique(leCanvas, x0,y0,largeur,hauteur,bordure,couleur1,couleur2,couleur3) :
    leCanvas.create_rectangle(x0+bordure//2, y0+bordure//2, x0+largeur-bordure//2, y0+hauteur-bordure//2, fill=couleur1, activefill=couleur2, outline=couleur3, width=bordure)




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

def robot_rouge():
    x, y = cote_carre/2 , cote_carre/2
    rayon = 10
    cercle_rouge = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon), fill="red")
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

def cible_rouge():
    pass
    xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    while (xg-xd != 47) or (yg-yd != 47) and (xg%16 != 0) or (xd%16 != 0) or (yg%16 != 0) or (yd%16 != 0) :
        xg, yg, xd, yd = random.randint(1, 752), random.randint(1, 752), random.randint(1, 752), random.randint(1, 752)
    else:
        carre_rouge = canvas.create_rectangle((xg, yg), (xd, yd), fill = "red")
        return[carre_rouge]

def cases_restart():
    for x in range (329, 376):
        for j in range (329, 376):
            rectangle_automatique(canvas, 47, 329, 47, 376, 2, "black", "black", "black")




rob_r = robot_rouge()
rob_b = robot_bleu()
rob_v = robot_vert()
rob_j = robot_jaune()
btn_restart = cases_restart()
#cib_r = cible_rouge()
fenetre.mainloop()
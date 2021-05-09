from tkinter import *
import math
import random

#fonctions à faire :
        # plateau -> qui genere et affiche le plateau
        # cibles -> qui genere et affiche les cibles 
        # mouvement -> qui permet aux robots de se déplacer (verticalement et horizontalement)
        # clr_mvmt -> qui permet d'affichet les possibles deplacements d'un robot lorsque l'on clique dessus
        # click -> btn click 
        # win -> qui permet d'afficher un message lorsque l'un des robots gagne 
        # restart -> qui permet de recommencer une partie 
        # cpt -> qui permet de compter le nombre de deplacements qu'un robot a fait 
        # save -> qui permet de sauvegarder une partie
        # return -> qui permet de revenir en arriere (d'annuler son deplcement)
        # edit_plt -> qui permet d'éditer le plateau 
        # obstacle -> qui permet d'arreter le robot lorsqu'il est devant un obstacle 

#variables :
        # longueur = 640
        # largeur = 640
        # cote = 40
        # robot_r
        # robot_b
        # robot_v
        # robot_j
        # cible_r
        # cible_b
        # cible_v
        # cible_j
        # btn_restart
        # btn_save
        # btn_load

#interface graphique#####################################################################################""
window_lenght, window_width = 1000, 1000

def automatic_rectangle(leCanvas, x0, y0, window_lenght, window_width, border, color1, color2, color3) :
    leCanvas.create_rectangle((x0+border)//2, (y0+border)//2, (x0 + window_width - border)//2, (y0 + window_lenght - border)//2, fill=color1, activefill=color2, outline=color3, width=border)

def tab():
    pass
    tab = [[]]
    for x in range (1, 640):
        for i in range (16):
            while x%16 == 0:
                i+= 1
    for y in range (1, 640):
        for j in range (16):
            while y%16 == 0:
                j+= 1

window = Tk()
window.title("robot ricochet")
window.geometry("1000x1000")




canvas = Canvas(window, width=640, height=640, bg='ivory', bd=0)
canvas.place(x=100,y=10)

plate_lenght, plate_width = 640, 640
square_side = 40

for y in range(0,plate_lenght, square_side) :
    for x in range(0,plate_width, square_side) :
        automatic_rectangle(canvas, x, y, 55, 55, 2, "#ffffcc", "grey", "brown")

###############################################################################################


###############################################################################################
plate_lenght, plate_width = 640, 640
square_side = 40

def red_robot():
    x, y = square_side/2 , square_side/2
    radius = 10
    red_circle = canvas.create_oval((x-radius, y-radius),(x+radius, y+radius), fill="red")
    return [red_circle]

def blue_robot():
    x, y = plate_width-(square_side/2), square_side/2
    radius = 10
    blue_circle = canvas.create_oval((x-radius, y-radius), (x+radius, y + radius), fill = "blue")
    return [blue_circle]

def green_robot():
    x, y = square_side/2, plate_width-(square_side/2)
    radius = 10
    green_circle = canvas.create_oval((x-radius, y-radius), (x+radius, y+radius), fill = "green")
    return [green_circle]

def yellow_robot():
    x, y = plate_width - (square_side/2), plate_width - (square_side/2)
    radius = 10
    yellow_circle = canvas.create_oval((x - radius, y - radius), (x + radius, y + radius), fill = "yellow")
    return [yellow_circle]

#################################################################################################
#robots = []
#pos_robot_r = []

def red_target():
    pass
    x_r_t = random.randrange(40, 600, 40)
    y_r_t = random.randrange(40, 600, 40)
    r_t_position = (x_r_t//square_side, y_r_t//square_side)
    pos_robot.append(position_red)
    robots.append(Red)

def blue_target():
    pass
    x_b_t = random.randrange(40, 600, 40)
    y_b_t = random.randrange(40, 600, 40)
    b_t_position = (x_b_t//square_side, y_b_t//square_side)
    pos_robot.append(position_blue)
    robots.append(Blue)

def green_target():
    pass
    x_g_t = random.randrange(40, 600, 40)
    y_g_t = random.randrange(40, 600, 40)
    g_t_position = (x_g_t//square_side, y_g_t//square_side)
    pos_robot.append(position_green)
    robots.append(Green)

def yellow_target():
    pass
    x_y_t = random.randrange(40, 600, 40)
    y_y_t = random.randrange(40, 600, 40)
    y_t_position = (x_y_t//square_side, y_y_t//square_side)
    pos_robot.append(position_yellow)
    robots.append(Yellow)


###########################################################################################################################

def cases_restart():
    for x in range (280, 320):
        for j in range (280, 320):
            automatic_rectangle(canvas, 329, 329, 80, 80, 10, "black", "black", "black")

def restart_game(event):
    pass
    click = False
    for x in range(280, 320):
        for y in range (280, 320):
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
        





    






rob_r = red_robot()
rob_b = blue_robot()
rob_v = green_robot()
rob_j = yellow_robot()
btn_restart = cases_restart()
#tab()
#surligne_deplac_rouge(rob_r)
#restart_game(event)
"""cib_r = red_target()
cib_b = blue_target()
cib_v = green_target()
cib_j = yellow_target()"""
window.mainloop()



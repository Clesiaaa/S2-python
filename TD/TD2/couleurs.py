import tkinter as tk
import random as rd

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i:int, j:int, color:str)->None:
    """Change de couleur seulement un pixel du canvas"""
    rec=canvas.create_rectangle(20,20,10,10, fill=color, outline=color)
    canvas.move(rec, i, j)

def ecran_aleatoire()->None:
    """génère alétoirement les pixels sur la surface du Canvas"""
    for i in range(0, 256, 10): 
    #bitmap(matrice de pixel) de 256x256 sachant que 1 pixel = 10x10 sur notre unité alors chaque pixel sera placé d'un écart de 10, 
    #donc un pas de 10 dans la boucle
        for j in range(0, 256, 10):
            draw_pixel(i, j, color=get_color(rd.randint(0, 255), rd.randint(0, 255),rd.randint(0, 255)))

def degrade_gris()->None:
    """génère un dégradé de gris sur l'ensemble de la surface du Canvas"""
    degrade=[x for x in range(256)]
    for i in range(0, 256, 10):
        for j in range(0 , 256, 10):
            draw_pixel(i, j, color=get_color(degrade[i], degrade[i], degrade[i]))
            #Meme principe que l'ecran aléatoire, sauf qu'on utilise la position i (comprise entre 0(noir) et 255(blanc))
            #i alors tourne dans la boucle (0 + 10 à chaque tour de boucle)
            #print(f"poX={i}, posY={j}, color={degrade[i]}")

def degrade_2D()->None:
    """fait un degrade de rouge-bleu sur la surface du Canvas"""
    for i in range(0, 256, 10):
        for j in range(0, 256, 10):
            draw_pixel(i, j, get_color(i, 0, j))
            #La fonction draw_pixel est appelée avec les coordonnées i et j et la couleur obtenue à partir de 
            #get_color(i, 0, j) en tant qu'argument Cela suggère que draw_pixel prend les coordonnées x, y 
            #et la couleur en tant que paramètres, dessinant ainsi un pixel de la couleur spécifiée aux coordonnées 
            #print(f"poX={i}, posY={j}, color={i, 0, j}")
            
root = tk.Tk()

btn_1 =tk.Button(root, text="Aléatoire", command=ecran_aleatoire)
btn_2 =tk.Button(root, text="Dégradé de gris", command=degrade_gris)
btn_3 =tk.Button(root, text="Dégradé 2D", command=degrade_2D)

canvas =tk.Canvas(root, height=256, width=256, bg="black")

btn_1.grid(row=1, column=1)
btn_2.grid(row=2, column=1)
btn_3.grid(row=3, column=1)

canvas.grid(row=2, column=2)

root.mainloop()
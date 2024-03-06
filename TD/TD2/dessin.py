import tkinter as tk
import random as rd

couleur = "white"
object = []

def undo()->None:
    global object
    if object:
        last_object = object.pop()
        Canvas.delete(last_object)

def demande_couleur()->str:
    """Demande à l'utilisateur la couleur souhaité"""
    global couleur
    couleur = input("Couleur ? : black, white, red, blue, cyan, yellow : ")
    return couleur

def Cercle()->None:
    """Fait apparaitre un cercle de manière aléatoire sur la surface"""
    cercle=Canvas.create_oval(200,200,100,100, fill=couleur)
    object.append(cercle)
    Canvas.move(cercle, rd.randint(100,549), rd.randint(100,549))

def Carre()->None:
    """Fait apparaitre un carré de manière aléatoire sur la surface"""
    carre=Canvas.create_rectangle(200,200,100,100, fill=couleur)
    object.append(carre)
    Canvas.move(carre, rd.randint(100,549), rd.randint(100,549))
    
def Croix()->None:
    """Fait apparaitre une croix de manière aléatoire sur la surface"""
    p1,p2 = rd.randint(100,549),rd.randint(100,549)
    l1=Canvas.create_line(15, 25, 35, 25, fill=couleur)
    l2=Canvas.create_line(25, 35, 25, 15, fill=couleur)
    object.append(l1)
    object.append(l2)
    Canvas.move(l1, p1, p2)
    Canvas.move(l2, p1, p2)

root = tk.Tk()

btn_1 =tk.Button(root, text="Carre", command=Carre)
btn_2 =tk.Button(root, text="Croix", command=Croix)
btn_3 =tk.Button(root, text="Cercle", command=Cercle)
btn_4 =tk.Button(root, text="Choisir Couleurs", command=demande_couleur)
btn_5 =tk.Button(root, text="Undo", command=undo)

Canvas = tk.Canvas(root, bg="black", width=550, height=550)

btn_1.grid(row=1, column=1)
btn_2.grid(row=2, column=1)
btn_3.grid(row=3, column=1)
btn_4.grid(row=1, column=2)
btn_5.grid(row=1, column=3)

Canvas.grid(row=2, column=2)

root.mainloop()
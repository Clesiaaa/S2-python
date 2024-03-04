import tkinter as tk
import random as rd

couleur = "white"

def demande_couleur()->str:
    global couleur
    couleur = input("Couleur ? : black, white, red, blue, cyan, yellow : ")
    return couleur

def Cercle()->None:
    cercle=Canvas.create_oval(200,200,100,100, fill=couleur)
    Canvas.move(cercle, rd.randint(100,549), rd.randint(100,549))

def Carre()->None:
    carre=Canvas.create_rectangle(200,200,100,100, fill=couleur)
    Canvas.move(carre, rd.randint(100,549), rd.randint(100,549))
    
def Croix()->None:
    p1,p2 = rd.randint(100,549),rd.randint(100,549)
    l1=Canvas.create_line(15, 25, 35, 25, fill=couleur)
    l2=Canvas.create_line(25, 35, 25, 15, fill=couleur)
    Canvas.move(l1, p1, p2)
    Canvas.move(l2, p1, p2)

root = tk.Tk()

btn_1 =tk.Button(root, text="Carre", command=Carre)
btn_2 =tk.Button(root, text="Croix", command=Croix)
btn_3 =tk.Button(root, text="Cercle", command=Cercle)
btn_4 =tk.Button(root, text="Choisir Couleurs", command=demande_couleur)

Canvas = tk.Canvas(root, bg="black", width=550, height=550)

btn_1.grid(row=1, column=1)
btn_2.grid(row=2, column=1)
btn_3.grid(row=3, column=1)
btn_4.grid(row=1, column=2)

Canvas.grid(row=2, column=2)

root.mainloop()
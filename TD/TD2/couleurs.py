import tkinter as tk

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i:int, j:int, color:str)->None:
    """Change de couleur seulement un pixel du canvas"""
    rec=canvas.create_rectangle(20,20,10,10, fill=color)
    canvas.move(rec, i, j)
    #print("pixel blanc")
    
root = tk.Tk()

btn_1 =tk.Button(root, text="Aléatoire")
btn_2 =tk.Button(root, text="Dégradé de gris")
btn_3 =tk.Button(root, text="Dégradé 2D")

canvas =tk.Canvas(root, height=256, width=256, bg="black")

btn_1.grid(row=1, column=1)
btn_2.grid(row=2, column=1)
btn_3.grid(row=3, column=1)

canvas.grid(row=2, column=2)

root.mainloop()
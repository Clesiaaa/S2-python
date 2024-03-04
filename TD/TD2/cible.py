import tkinter as tk

n, x, i, w = 25, 0, 0, 10
colors = ["blue", "green", "black", "yellow", "pink", "red"]

root = tk.Tk()

canvas = tk.Canvas(root, bg="black", width=500, height=500)
canvas.pack()

while n != 0:
    couleur = colors[i]
    cercle = canvas.create_oval(499 - x, 499 - x, 100 + x, 100 + x, fill=couleur, outline=couleur)
    canvas.move(cercle, w, w)
    x = x + w
    n = n - 1
    i = i + 1
    if i >= len(colors):
        i = 0

root.mainloop()

#c'est bancale wsh dsl
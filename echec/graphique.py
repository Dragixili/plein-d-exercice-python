from tkinter import *

root = Tk()
root.title("Chess")
root.geometry("660x660")

canvas = Canvas(root, width=660, height=660, bg="beige")
canvas.place(x=0, y=0)

taille = 70
offset = 50

for i in range(8):
    for j in range(8):
        x1 = offset + i * taille
        y1 = offset + j * taille
        x2 = x1  + taille
        y2 = y1 + taille

        couleur = "black" if (i + j) % 2 == 0 else "white"

        canvas.create_rectangle(x1,y1,x2,y2, fill=couleur)

root.mainloop()

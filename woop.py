import tkinter
import random
canvas = tkinter.Canvas(width="600", height="400")
canvas.pack()
subor = open("mozaika.txt","r",encoding="UTF-8")

def mozaika(sirka_platna, vyska_platna):
    x,y = 0,0
    a = int(subor.readline().strip())

    while y < vyska_platna + a:
        while x < sirka_platna + a:
            farba = subor.readline().strip()
            canvas.create_rectangle(x,y,x+a,y+a, fill=farba,outline= farba)
            x += a
        x=0
        y += a




mozaika(600,400)
canvas.mainloop()


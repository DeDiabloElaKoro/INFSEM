from random import *
import turtle
tabula = turtle.Screen()
tabula.tracer(0)
sirka=500
vyska=500
tabula.setup(sirka, vyska)
pero = turtle.Turtle()
subor = open("rozmery.txt", "a",encoding="UTF-8")
def n_farba():
    a=f"#{randrange(256):02x}{randrange(256):02x}{randrange(256):02x}"
    return a
def kruh(r,farba):
    pero.dot(r,farba)
def terc():
    polomer=50
    for i in range(10):
        pero.dot(polomer,n_farba())
        polomer-=5
        subor.write(str(n_farba())+"\n")
def nahodna_poz(n):
    subor.write(str(n) + "\n")
    for i in range(n):
        pero.up()
        x=randrange(-250,250)
        y=randrange(-250,250)
        subor.write(str(x)+"\n")
        subor.write(str(y)+"\n")
        pero.setposition(x,y)
        pero.down()
        terc()

nahodna_poz(10)
subor.close()

pero.hideturtle()
tabula.mainloop()

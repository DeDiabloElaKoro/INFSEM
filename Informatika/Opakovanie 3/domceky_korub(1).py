import turtle
from random import *

def nuholnik(n, a,farba):
    pero.down()
    uhol= (180*(n-2))/n
    pero.fillcolor(farba)
    pero.begin_fill()
    for i in range(n):
        pero.forward(a)
        pero.left(180-uhol)
    pero.end_fill()
    pero.up()
def domcek(f1,f2,a):
    pero.down()
    nuholnik(4,a,f1)
    pero.left(90)
    pero.up()
    pero.forward(a)
    pero.right(90)
    nuholnik(3,a,f2)

def n_farba():
    a=f"#{randrange(256):02x}{randrange(256):02x}{randrange(256):02x}"
    return a
def ulica(rady, stlpce, a):
    for stlp in range(stlpce):
        for rad in range(rady):
            domcek(n_farba(), n_farba(), 50)
            pero.up()
            pero.forward(a + 50)
            pero.right(90)
            pero.forward(50)
            pero.left(90)
            pero.down()
        pero.up()
        pero.setpos(-((rady-1)*50), (stlp+1) * (-150))
        pero.down()
def nahodne_mesto(pocet):
    for i in range(pocet):
        x = randrange(-250, 250)
        y = randrange(-250, 250)
        uhol=randrange(-10,10)
        pero.up()
        pero.setpos(x,y)
        pero.right(uhol)
        domcek(n_farba(),n_farba(),pocet)
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
pero.up()
pero.setpos(-300,0)
pero.down()

#ulica(7,3,50)
#nuholnik(9,50,"red")
#ulica(7, 3, 30)
nahodne_mesto(30)

pero.hideturtle()
tabula.mainloop()

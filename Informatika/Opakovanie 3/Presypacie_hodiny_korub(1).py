import turtle
import random
pero = turtle.Turtle()
tabula = turtle.Screen()
farby=("blue","pink","purple","orange","red")
farby1=("green","brown","grey","black","aqua")


def hodiny(f1,f2,y):
    pero.pensize(5)
    pero.color(f1)
    pero.fillcolor(f2)
    pero.begin_fill()
    pero.forward(y)
    pero.left(120)
    pero.forward(y*2)
    pero.right(120)
    pero.forward(y)
    pero.right(120)
    pero.forward(y*2)
    pero.left(120)
    pero.end_fill()

def vykreslenie(x,y):
    farba1 = random.choice(farby)
    farba2 = random.choice(farby1)
    pero.up()
    pero.setpos(-(y * x/2), 0)
    pero.down()
    for i in range(x):
        hodiny(farba1, farba2, y)
        farba1, farba2 = farba2, farba1
        pero.up()
        pero.forward(y)
        pero.down()


vykreslenie(8,100)

pero.hideturtle()
tabula.mainloop()
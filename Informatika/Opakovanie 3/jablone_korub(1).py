import turtle
import random
tabula = turtle.Screen()
pero = turtle.Turtle()
pero.speed(0)
pero.left(90)
pero.up()

riadky= int(tabula.textinput("Počet riadkov",  "Zadajte počet riadkov :"))
stlpce= int(tabula.textinput("Počet stĺpcov" , "Zadajte počet stĺpcov:"))


def strom(vyska,jablka):
    pero.down()
    pero.width(8)
    pero.color("brown")
    pero.forward(vyska)
    pero.up()
    pero.forward(vyska)
    pero.down()
    pero.dot(vyska*2,"green")
    pero.up()
    for i in range(jablka):
        pero.setheading(random.randrange(360))
        vzd = random.randint(0,vyska-10)
        pero.forward(vzd)
        pero.dot(10,"red")
        pero.right(180)
        pero.forward(vzd)
        pero.up()
    pero.setheading(90)


def sad(x,y):
    try:
        a = -400
        b = 200
        for o in range(x):
            for i in range(y):
                a +=100
                pero.setposition(a, b)
                priemer=random.randint(15,50)
                jablk = random.randint(0,10)
                strom(priemer,jablk)
            a = -400
            b -= 150
            pero.setpos(a,b)
    except ValueError:
        raise ValueError('Zadaná nečíselná hodnota.')
    if x < 0 or y < 0:
        raise ValueError('Zadaná nesprávna hodnota.')


turtle.screensize(canvwidth=500, canvheight=500)
pero.up()
pero.speed(0)

sad(riadky,stlpce)

tabula.mainloop()

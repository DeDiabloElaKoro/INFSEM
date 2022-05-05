import turtle
import math

tabula = turtle.Screen()
pero = turtle.Turtle()

a= int(tabula.textinput("Dĺžka strany a" , "Zadajte dĺžku strany a v cm :"))
b= int(tabula.textinput("Dĺžka strany b",  "Zadajte dĺžku strany b v cm :"))
c= int(tabula.textinput("Dĺžka strany c",  "Zadajte dĺžku strany c v cm :"))

def vypocitaj_uhol_x(x, y, z):
    cos_x = (y ** 2 + z ** 2 - x ** 2) / (2 * y * z)
    return math.degrees(math.acos(cos_x))

def trojuholnik(a,b,c):
    pero.down()
    pero.write("A")
    pero.forward(c)
    pero.write("B")
    pero.left(180)
    beta=vypocitaj_uhol_x(b,c,a)
    pero.right(beta)
    pero.forward(a)
    pero.write("C")
    pero.left(180)
    gamma=vypocitaj_uhol_x(c,a,b)
    pero.right(gamma)
    pero.forward(b)
    alfa=vypocitaj_uhol_x(a,c,b)
    text = f"a={a}cm, b= {b}cm,c= {c}cm"
    text1= f"alfa={round(alfa,1)}°, beta={round(beta,1)}°,gamma={round(gamma,1)}° "
    pero.up()
    pero.setpos(0,-15)
    pero.write(text)
    pero.setpos(0,-30)
    pero.write(text1)
    pero.hideturtle()

if a+b >c and a+c>b and b+c>a:
    trojuholnik(a,b,c)
else:
    print(f"Zadané hodnoty nesĺňajú trojuholníkovú nerovnosť")

pero.hideturtle()
tabula.mainloop()

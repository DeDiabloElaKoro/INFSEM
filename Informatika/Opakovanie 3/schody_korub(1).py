import turtle
tabula = turtle.Screen()
pero =  turtle.Turtle()
pero1=  turtle.Turtle()
vyska= int(tabula.textinput("Schodisko" , "Zadajte výšku schodu (v cm):"))
pocet= int(tabula.textinput("Schodisko",  "Zadajte počet schodov :"))
pero.up()
pero.back(100)
pero.down()
sirka = 63-(2*vyska)
def schod():
    vys=0
    sir=0
    for i in range(pocet):
        pero.left(90)
        pero.forward(vyska)
        pero.right(90)
        pero.forward(sirka)
    pero.right(90)
    pero.forward(vyska*pocet)
    pero.right(90)
    pero.forward(sirka*pocet)
    pero.hideturtle()
    return vyska,sirka
schod()
print(vyska)
def typ_schodov():
    if vyska <=13:
        text = "Rampové schodisko:"
    elif vyska <=15:
        text = "Mierne schodisko:"
    elif vyska <=18:
        text = "Normálne  schodisko:"
    elif vyska <=20:
        text = "Strmé schodisko:"
    elif vyska >20:
        text = "rebríkové  schodisko:"
    text = text + f"výška={vyska*pocet}cm, šírka = {sirka*pocet}cm"
    pero1.up()
    pero1.setpos(-100,-15)
    pero1.write(text)
    pero1.hideturtle()
typ_schodov()
tabula.mainloop()


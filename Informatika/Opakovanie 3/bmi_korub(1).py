import tkinter
canvas = tkinter.Canvas(height=600,width=600)
canvas.pack()
vaha=int(input("Zadaj váhu:"))
vyska=int(input("Zadaj vysku:"))

def bmi(vys,vah):
    vys1=vys/100
    bmii=vah/(vys1*vys1)
    print(bmii)
    return bmii
a=bmi(vyska,vaha)

canvas.create_text(300,150,font="Arial 30",text="vyska"+str(vyska)+"cm, hmotnosť"+str(vaha)+"kg")

def graf():
    canvas.create_rectangle(0,250,262.5,350,fill="yellow")
    canvas.create_rectangle(262.5,250,375,350,fill="green")
    canvas.create_rectangle(375,250,450,350,fill="orange")
    canvas.create_rectangle(450,250,600,350,fill="red")
    if a < 17.5:
        subor="podvýživa"
        farba="yellow"
    elif a >17.5 and a<25:
        subor="ideálna a zdravá váha"
        farba="green"
    elif a > 25 and a<30:
        subor="mierna nadváha"
        farba="orange"
    elif a > 30 and a<40:
        subor="obezita"
        farba="red"
    elif a > 40:
        subor="ťažká obezita"
        farba="black"
    canvas.create_text(300,450,font="Arial 30",text=subor,fill=farba)
    canvas.create_line(a*15,240,a*15,360,width="5")
    canvas.create_text(300,500,font="Arial 30",text= "BMI = "+str(a),fill=farba)
graf()

canvas.mainloop()

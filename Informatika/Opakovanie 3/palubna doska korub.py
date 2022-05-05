import tkinter

canvas = tkinter.Canvas(width=300, height=300,bg="black")
canvas.pack()
x=0
def stupnica():
    y = 0
    rychlost=0
    for i in range(20):
        canvas.create_text(15, y+5,text=rychlost,fill="white")
        canvas.create_line(0, y+10, 100, y+10,fill="white")
        y += 15
        rychlost +=10

def pomal():
    canvas.delete("all")
    stupnica()
    global x
    if x>0:
        x -= 10
        canvas.create_rectangle(130, 0, 280, x, fill="red")
    elif x>=260:
        x = 260
        canvas.create_rectangle(130, 0, 280, x, fill="red")

def rychl():
    canvas.delete("all")
    stupnica()
    global x
    x += 10
    if x <= 260:
        canvas.create_rectangle(130, 0, 280, x, fill="red")
    else:
        x = 260
        canvas.create_rectangle(130, 0, 280, x, fill="red")

button1 = tkinter.Button(text='rychlejšie', command=rychl)
button1.pack()
button2 = tkinter.Button(text='pomalšie', command=pomal)
button2.pack()
stupnica()
canvas.mainloop()

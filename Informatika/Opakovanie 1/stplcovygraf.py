import tkinter
canvas = tkinter.Canvas(width=300, height=500,bg="white")
canvas.pack()
import random
del4 = 0
del5 = 0
for i in range (1000):
    cisla = random.randrange(0,1000)
    if cisla % 5 == 0:
        del5 += 1
    elif cisla % 4 ==0:
        del4 += 1
canvas.create_line(10,10,10,490)
canvas.create_line(10,490,290,490)
canvas.create_rectangle(50,490,100,del4,fill="blue")
canvas.create_text(75,del4-10,text=del4)
canvas.create_rectangle(150,490,200,del5,fill="red")
canvas.create_text(175,del5-10,text=del5)
canvas.mainloop()
print (del4)
print (del5)
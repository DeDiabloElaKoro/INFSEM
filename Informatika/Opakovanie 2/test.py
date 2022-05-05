import math
from tkinter import *
master = Tk()
w = Canvas(master, width=600, height=600)
w.pack()

a=float(input("Zadaj hodnotu a = "))
b=float(input("Zadaj hodnotu b = "))
c=float(input("Zadaj hodnotu c = "))
D=b*b-4*a*c
if D <0:
    print("Rovnica nemá žiadne riešenie")
elif D==0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print(f"Rovnica má jeden dvojnásobný koreň x ={x1}")
else:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print(f"Rovnica má dve riešenia x1 ={x1} a x2 ={x2}")
w.create_line(0,300,600,300)
w.create_line(300,0,300,600)

for i in range(-50,50):
    suradnica= a*(i**2)+b*i+c
    print(suradnica)
    w.create_line(abs(i),abs(suradnica),abs(i)+1,abs(suradnica)+1)
    print(i)
w.mainloop()

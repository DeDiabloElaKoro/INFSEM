import tkinter
canvas = tkinter.Canvas(width="600", height="400")
canvas.pack()
canvas.create_line(100,100,10,100,10,150,100,150,10,150,10,200,100,200)
canvas.mainloop()

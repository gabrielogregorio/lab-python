from tkinter import *

janela = Tk()

lb1 = Label(janela, text="RIGHT W - 1", bg="white")
lb2 = Label(janela, text="BOTTOM G - 2", bg="green")
lb3 = Label(janela, text="LEFT R - 3", bg="red")
lb4 = Label(janela, text="TOP B - 4", bg="blue")

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)

janela["bg"] = "black"


janela.geometry("400x400+0+0")
janela.mainloop()
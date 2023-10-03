from tkinter import *

janela = Tk()

def bt_click():
	print("show")
	lb["text"] = "Tudo certo"
	bt["background"]="red"

bt = Button(janela, width=50, text="ok", command=bt_click) 
bt.place(x=100, y=100)
bt["background"] = "green"

lb = Label(janela, text="Clique me")
lb.place(x=100, y=150)

janela.geometry("300x300+0+0")
janela.mainloop()
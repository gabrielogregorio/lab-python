from tkinter import*

def somar():

	if str(ed.get()).isnumeric() and str(ed2.get()).isnumeric():
		lb["text"] = float(ed.get())+float(ed2.get())
	else:
		lb["text"] = "Isso não é numero!"

janela = Tk()

ed = Entry(janela)
ed.place(x=100,y=100)

ed2 = Entry(janela)
ed2.place(x=100,y=150)

bt = Button(janela, text="Somar", width="20" ,command=somar)
bt.place(x=100,y=200)

lb = Label(janela,text="resultado")
lb.place(x=100,y=250)

janela.geometry("500x500+0+0")
janela["background"] = "blue"
janela.mainloop()

from tkinter import*

janela = Tk()

lb1 = Label(janela, text="ESPAÇO", width="15",height="3", bg="blue")
lbHorizontal = Label(janela, text="Horizontal", bg="yellow")
lbVertical = Label(janela, text="Vertical", bg="red")

lb1.grid(row=0, column=0)
lbHorizontal.grid(row=1, column=0,sticky=W)

lbVertical.grid(row=0, column=1, sticky=N)

janela.geometry("200x100+100+100")
janela.mainloop()
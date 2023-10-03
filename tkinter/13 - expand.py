from tkinter import*

janela = Tk()

lb1 = Label(janela, text="Linha 1", bg="white")
lb2 = Label(janela, text="Linha 2", bg="yellow")
lb3 = Label(janela, text="Linha 3", bg="blue")
lb4 = Label(janela, text="Linha 3", bg="yellow")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

janela.geometry("500x200+-600+200")

janela.mainloop()
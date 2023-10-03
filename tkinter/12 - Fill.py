from tkinter import*

janela = Tk()

lb1 = Label(janela, text="horizntal",bg="white")
lb2 = Label(janela, text="vertical left",bg="green")
lb3 = Label(janela, text="vertical right",bg="pink")
lb4 = Label(janela, text="horizontal baixo", bg="yellow")

lb1.pack(side=TOP, fill=X)
lb4.pack(side=BOTTOM, fill=X)
lb2.pack(side=LEFT, fill=Y)
lb3.pack(side=RIGHT, fill=Y)

janela.geometry("500x200+-600+200")

janela.mainloop()


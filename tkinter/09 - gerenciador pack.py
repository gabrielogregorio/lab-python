from tkinter import*

janela = Tk()

lb1 = Label(janela, text="label 1", bg="green")
lb2 = Label(janela, text="label 2", bg="red")
lb3 = Label(janela, text="label 3", bg="yellow")
lb4 = Label(janela, text="label 4", bg="blue")
lb5 = Label(janela, text="label 5", bg="pink")
lb6 = Label(janela, text="label 6", bg="white")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb4.pack(side=RIGHT)
lb3.pack(side=RIGHT)
lb5.pack()
lb6.pack(side=BOTTOM)


janela.geometry("400x400+0+0")
janela.mainloop()
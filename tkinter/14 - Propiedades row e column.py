from tkinter import*

janela = Tk()

lb1 = Label(janela, text="label 1")
lb2 = Label(janela, text="label 2")
lb1.grid(row=1000,column=1000)
lb2.grid(row=2000,column=2000)


janela.geometry("500x200+-600+200")
janela.mainloop()
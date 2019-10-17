# from tkinter import *

#  OU

from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import NSEW
from tkinter import messagebox

def validar_login():
    if ((ent_login.get() == 'Admin') and (ent_senha.get() == 'Senha')):
        messagebox.showinfo('Sucesso!','Login realizado com sucesso')
    else:
        messagebox.showinfo('Ops','Acesso não autorizado!')

tela = Tk()

lbl_login = Label(tela, text='Login')
ent_login = Entry(tela)

lbl_senha = Label(tela, text='Senha')
ent_senha = Entry(tela)

btn_logar = Button(tela, text='Logar', command=validar_login)

lbl_login.grid(row=1,column=1)
ent_login.grid(row=1,column=2)
lbl_senha.grid(row=2,column=1)
ent_senha.grid(row=2,column=2)
btn_logar.grid(row=3,column=1,columnspan=2)

tela.mainloop()

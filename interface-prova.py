#Retirado da prova Univesp

from tkinter import Tk, Button, Label, Entry, END 
def clicked(): 
    global entry 
    name = entry.get() #O método get serve para retornar um texto
    print('Ola', name) 
    entry.delete(0, END) 
 
root = Tk() 
label = Label(root, text='Nome:') 
label.grid(row=0, column=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
button = Button(root, text='OK', command=clicked) 
button.grid(row=1, column=0, columnspan=2) 
root.mainloop() 

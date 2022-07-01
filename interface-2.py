<<<<<<< HEAD
#Primeiro exemplo: janela com um botão que, quando clicado, exibe o dia e a hora na tela. 

from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
showinfo(message=time)

root = Tk()
button = Button(root, text='Clique', command=clicked)
button.pack()
root.mainloop()
=======
#Primeiro exemplo: janela com um botão que, quando clicado, exibe o dia e a hora na tela. 

from tkinter import Tk, Button, Label
from tkinter.messagebox import showinfo
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S%p\n', localtime())
showinfo(message=time)

root = Tk()
button = Button(root, text='Clique', command=clicked)
button.pack()
root.mainloop()
>>>>>>> 62b89ef61a69aa6939953720a89a55fdaf8ac070

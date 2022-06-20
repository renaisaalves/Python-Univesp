#CRIANDO UMA INTERFACE GRÁFICA (GUI) NO PYTHON

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='ratinho-flores.gif')
image = Label(master=root, image=photo)
image.pack(side=BOTTOM)
text = Label(master=root, font=("Arial", 18), text='Meu primeiro programa com Interface Gráfica!')
text.pack(side=TOP)
root.mainloop()
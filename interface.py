#CRIANDO UMA INTERFACE GRÁFICA (GUI) NO PYTHON

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk
root.mainloop()
'''
root = Tk
photo = PhotoImage(file='ratinho-flores.gif').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Arial", 18), text='Meu primeiro programa com Interface Gráfica!')
text.pack(side=BOTTOM)
root.mainloop() '''
#CRIANDO UMA INTERFACE GRÁFICA (GUI) NO PYTHON

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk()
photo = PhotoImage(file='ratinho-flores.gif')
image = Label(master=root, image=photo)
image.pack(side=BOTTOM)
text = Label(master=root, font=("Calibri", 18), text='Meu primeiro programa com Interface Gráfica!')
text.pack(side=TOP)
root.mainloop()

#tkinter é uma biblioteca GUI do Python que permite fazer Interface Gráfica. 
#Dentro dessa biblioteca, existem várias classes com uma função específica, por exemplo:
#Tk é a principal janela da uma aplicação, ou seja, ela é a janela que abriga todos os elementos. 
#Label serve para exibir textos e bitmaps (imagens).
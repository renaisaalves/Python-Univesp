#CRIANDO UMA INTERFACE GRÁFICA (GUI) NO PYTHON

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk() #cria uma janela principal em branco
photo = PhotoImage(file='ratinho-flores.gif') #imagem
image = Label(master=root, image=photo) #faz a união da janela com a imagem
image.pack(side=BOTTOM) #vai unir tudo para baixo
text = Label(master=root, font=("Calibri", 18), text='Meu primeiro programa com Interface Gráfica!')
text.pack(side=TOP) #vai unir tudo para cima
root.mainloop() #vai fazer funcionar

#tkinter é uma biblioteca GUI do Python que permite fazer Interface Gráfica. 
#Dentro dessa biblioteca, existem várias classes com uma função específica, por exemplo:
#Tk é a principal janela da uma aplicação, ou seja, ela é a janela que abriga todos os elementos. 
#Label serve para exibir textos e bitmaps (imagens).

#CRIANDO UMA INTERFACE GRÁFICA (GUI) NO PYTHON

from tkinter import Tk, Label, PhotoImage, TOP, BOTTOM

root = Tk() #cria uma janela principal em branco
photo = PhotoImage(file='ratinho-flores.gif') #imagem
image = Label(master=root, image=photo) #faz a união da janela com a imagem
image.pack(side=BOTTOM) #vai unir tudo para baixo
text = Label(master=root, font=("Calibri", 18), text='Meu primeiro programa com Interface Gráfica!')
text.pack(side=TOP) #vai unir tudo para cima
root.mainloop() #vai fazer funcionar

#tkinter é uma biblioteca GUI do Python que permite fazer Interface Gráfica. 
#Dentro dessa biblioteca, existem várias classes com uma função específica, por exemplo:
#Tk é a principal janela da uma aplicação, ou seja, ela é a janela que abriga todos os elementos. 
#Label serve para exibir textos e bitmaps (imagens).

#PhotoImage permite exibir imagens em formato PGM, PPM, GIF e PNG. 
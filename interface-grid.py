
from tkinter import Tk, Label, RAISED

root = Tk()
labels = [['1', '2', '3'], 
          ['4', '5', '6'], 
          ['7', '8', '9'], 
          ['*', '0', '#']]
for r in range(4): #linhas (row)
    for c in range(3): #colunas (column)
        label = Label(root, relief=RAISED, padx=15, text=labels[r][c])
        label.grid(row=r, column=c)
root.mainloop()

#O professor não explicou esse método, apenas deixou como exercício para rodar na IDE.
#Porém, descobri algumas coisas: padx está relacionado com a largura dos botões.

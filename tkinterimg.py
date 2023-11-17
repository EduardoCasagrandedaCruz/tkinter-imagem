from tkinter import *

from PIL import ImageTk, Image
import os

root = Tk()

arquivos = os.listdir('imagens')
imagens = []

for arquivo in arquivos:
    img= Image.open('imagens/' + arquivo)
    imagens.append(ImageTk.PhotoImage(img))

#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()






imglabel = Label(root, image=imagens[2])


imglabel.pack()












root.mainloop()
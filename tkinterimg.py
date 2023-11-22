from tkinter import *

from PIL import ImageTk, Image, ImageOps
import os

root = Tk()

arquivos = os.listdir('imagens')
imagens = []


controleimg=0

for arquivo in arquivos:
    img= Image.open('imagens/' + arquivo)
    img= ImageOps.contain(img,(400,400))
    imagens.append(ImageTk.PhotoImage(img))
#arquivos_label = Label(root, text=arquivos)
#arquivos_label.pack()



imglabel = Label(root, image=imagens[controleimg])
imglabel.grid(column=0,row=0,columnspan=3)


def prev_image():
    global controleimg
    global imglabel
    global imagens

    if controleimg == 0:
        controleimg=len(imagens)-1
    else:
        controleimg -= 1
    
    imglabel.grid_forget()
    
    imglabel=Label(root, image=imagens[controleimg])
    imglabel.grid(column=0,row=0, columnspan=3)

def next_image():
    global controleimg
    global imglabel
    global imagens

    if controleimg == len(imagens)-1:
        controleimg=0
    else:
        controleimg += 1
    
    imglabel.grid_forget()
    
    imglabel=Label(root, image=imagens[controleimg])
    imglabel.grid(column=0,row=0, columnspan=3)


a=Button(root, text='prev',command=prev_image)
a.grid(column=0,row=1)
b=Button(root, text='sair',command=root.quit)
b.grid(column=1,row=1)
c=Button(root, text='next',command=prev_image)
c.grid(column=2,row=1)













root.mainloop()
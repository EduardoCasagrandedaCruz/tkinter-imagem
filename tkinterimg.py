from tkinter import *

from PIL import ImageTk, Image

root = Tk()




img = Image.open('imagem.jpg')
img_tk = ImageTk.PhotoImage(img)


imglabel = Label(root, image=img_tk)


imglabel.pack()












root.mainloop()
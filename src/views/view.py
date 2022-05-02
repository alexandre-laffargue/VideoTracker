import tkinter as tk
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk
from tkinter import  CENTER, RIDGE, Frame, Menu, ttk, LabelFrame, Button, Canvas

 
class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.canvas = None
        self.parent = parent

        self.setmenu(parent)
        self.setbouton(parent)



    def setController(self, controller):
        self.controller = controller

    def setmenu(self, parent):
        self.controller = None
        parent.geometry('1400x700+200+100')
        bandeau = Frame(parent, borderwidth = 2, relief = RIDGE )
        bandeau.grid(row = 0, column = 0)

        menuBar = Menu(parent)
        parent['menu'] = menuBar

        Filesmenu = Menu(menuBar,tearoff=0)
        Viewmenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Files', menu=Filesmenu)
        menuBar.add_cascade(label='View', menu=Viewmenu)

        Filesmenu.add_command(label='Charger un fichier vidéo', command=self.lienvideo)
        Filesmenu.add_command(label='Lire une vidéo', command=self.lienlecture)
        Filesmenu.add_command(label='Quitter', command=exit)
        Filesmenu.add_separator()
        Filesmenu.add_command(label='Save', command=0)
        Filesmenu.add_command(label='Exporter (csv)', command=0)
        
        Viewmenu.add_command(label='Affichage graphique', command=0)
        
    def setbouton(self, parent):
        ZoneOptions = LabelFrame(parent, borderwidth = 2, text = 'Options', labelanchor = 'n', width = 200, height = 100)
        ZoneOptions.grid(row = 0, column = 0)

        Boustart = Button(ZoneOptions,text = 'start', command=self.lienlecture)
        Boustart.grid(row = 0, pady = 10, column = 2)
        Boupause = Button(ZoneOptions,text = 'Pause', command= self.linkpause)
        Boupause.grid(row = 0, pady = 10, column = 3)
        BouimageS = Button(ZoneOptions,text = '>|', command= self.linknextimage)
        BouimageS.grid(row = 0, pady = 10, column = 4)
        BouimageP = Button(ZoneOptions,text = '|<', command= 0 )
        BouimageP.grid(row = 0, pady = 10, column = 1)
        BouimageF = Button(ZoneOptions,text = '||<', command= self.linkreturnfirstimage)
        BouimageF.grid(row = 0, pady = 10, column = 0)
        BouimageL = Button(ZoneOptions,text = '>||', command= 0 )
        BouimageL.grid(row = 0, pady = 10, column = 5)


    def lienvideo(self):
        print("a")
        self.controller.afficher()

    def lienlecture(self):
        self.controller.lecture()

    def linkpause(self):
        self.controller.pause()

    def linknextimage(self):
        self.controller.next_image()

    def linkreturnfirstimage(self):
        self.controller.returnfirstimage()
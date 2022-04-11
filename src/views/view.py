import tkinter as tk
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk
from tkinter import RIDGE, Frame, Menu, ttk, LabelFrame, Button, Canvas

from controllers.Controller import Controller

 
class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        parent.geometry('1000x600+500+300')
        
        bandeau = Frame(parent, borderwidth = 2, relief = RIDGE)
        bandeau.grid(row = 0, column = 0)

        menuBar = Menu(parent)
        parent['menu'] = menuBar

        Filesmenu = Menu(menuBar,tearoff=0)
        Viewmenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Files', menu=Filesmenu)
        menuBar.add_cascade(label='View', menu=Viewmenu)
        
        ZoneOptions = LabelFrame(parent, borderwidth = 2, text = 'Options', labelanchor = 'n', width = 200, height = 100)
        ZoneOptions.grid(row = 0, column = 0)
        ZoneVideo = Frame(parent, borderwidth = 2, relief = RIDGE)
        ZoneVideo.grid(row = 1, column = 0)
        self.canvas = Canvas(ZoneVideo, bg = 'gray', width = 840, height = 850)
        self.canvas.pack()

        Filesmenu.add_command(label='Charger un fichier vidéo', command=0) #Controller.openfile(self)
        Filesmenu.add_command(label='Lire une vidéo', command=0)
        Filesmenu.add_command(label='Quitter', command=exit)
        Filesmenu.add_separator()
        Filesmenu.add_command(label='Save', command=0)
        Filesmenu.add_command(label='Exporter (csv)', command=0)
        
        Viewmenu.add_command(label='Affichage graphique', command=0)
        

        Boustart = Button(ZoneOptions,text = 'start', command=0)
        Boustart.grid(row = 0, pady = 10, column = 0)
        Boupause = Button(ZoneOptions,text = 'Pause', command= 0 )
        Boupause.grid(row = 0, pady = 10, column = 1)
        BouimageS = Button(ZoneOptions,text = '>|', command= 0 )
        BouimageS.grid(row = 0, pady = 10, column = 2)
        BouimageP = Button(ZoneOptions,text = '|<', command= 0 )
        BouimageP.grid(row = 0, pady = 10, column = 3)
        


    
    def setController(self, controller):
        self.controller = controller

    
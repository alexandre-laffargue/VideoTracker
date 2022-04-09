import tkinter as tk
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk
from tkinter import RIDGE, Frame, Menu, ttk, LabelFrame

from controllers import Controller
 
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


        Filesmenu.add_command(label='Charger un fichier vidéo', command=0)
        Filesmenu.add_command(label='Lire une vidéo', command=0)
        Filesmenu.add_command(label='Quitter', command=parent.destroy)
        Filesmenu.add_separator()
        Filesmenu.add_command(label='Save', command=0)
        Filesmenu.add_command(label='Exporter (csv)', command=0)
        
        Viewmenu.add_command(label='Affichage graphique', command=0)
        ZoneOptions = LabelFrame(parent, borderwidth = 2, text = 'Options', labelanchor = 'n', width = 200, height = 100)
        ZoneOptions.grid(row = 0, column = 0)
        ZoneVideo = Frame(parent, borderwidth = 2, relief = RIDGE)
        ZoneVideo.grid(row = 1, column = 0)


    
    def setController(self, controller):
        self.controller = controller

    
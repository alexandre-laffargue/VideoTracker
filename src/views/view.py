from fileinput import close
import tkinter as tk
from turtle import title
from typing import Text
import PIL.Image, PIL.ImageTk
from PIL import Image,ImageTk
from tkinter import  CENTER, RIDGE, Entry, Frame, Menu, StringVar, Toplevel, ttk, LabelFrame, Button, Canvas
from tkinter.messagebox import *
 
class View(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.parent = parent

        self.setmenu(parent)
        self.setbouton(parent)
        self.setbind()



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
        Editmenu = Menu(menuBar,tearoff=0)
        Viewmenu = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label='Files', menu=Filesmenu)
        menuBar.add_cascade(label='Edit', menu=Editmenu)
        menuBar.add_cascade(label='View', menu=Viewmenu)

        Filesmenu.add_command(label='Charger un fichier vidéo', command=self.lienvideo)
        Filesmenu.add_command(label='Lire une vidéo', command=self.lienlecture)
        Filesmenu.add_command(label='Quitter', command=exit)
        Filesmenu.add_separator()
        Filesmenu.add_command(label='Save', command=0)
        Filesmenu.add_command(label='Exporter (csv)', command=0)
        
        Editmenu.add_command(label='SetScale', command= self.linkechelle)
        Editmenu.add_command(label='ResetScale', command= self.linkresetechelle)

        Viewmenu.add_command(label='Affichage graphique', command=0)
        
    def setbouton(self, parent):
        ZoneBoutons = Frame(parent)
        ZoneBoutons.grid(row = 0, column = 0)
        ZoneOptions = LabelFrame(ZoneBoutons , borderwidth = 2, text = 'Options', labelanchor = 'n', width = 200, height = 100)
        ZoneOptions.grid(row = 0, column = 1)

        Boustart = Button(ZoneOptions,text = 'start', command=self.lienlecture)
        Boustart.grid(row = 0, pady = 10, column = 2)
        Boupause = Button(ZoneOptions,text = 'Pause', command= self.linkpause)
        Boupause.grid(row = 0, pady = 10, column = 3)
        BouimageS = Button(ZoneOptions,text = '>>|', command= self.linknextimage)
        BouimageS.grid(row = 0, pady = 10, column = 4)
        BouimageP = Button(ZoneOptions,text = '|<<', command= 0 )
        BouimageP.grid(row = 0, pady = 10, column = 1)
        BouimageF = Button(ZoneOptions,text = '|<', command= self.linkreturnfirstimage)
        BouimageF.grid(row = 0, pady = 10, column = 0)
        BouimageL = Button(ZoneOptions,text = '>|', command= 0 )
        BouimageL.grid(row = 0, pady = 10, column = 5)

        ZonePointage = LabelFrame(ZoneBoutons , borderwidth = 2, text = 'Pointage', labelanchor = 'n', width = 200, height = 100)
        ZonePointage.grid(row = 0,pady = 5, column = 0)
        self.Bourepere = Button(ZonePointage,text = '+',activebackground= "yellow", command= self.linkrepere )
        self.Bourepere.grid(row = 0, pady = 10, column = 0)
        BouPointer = Button(ZonePointage,text = 'x', command= self.linkpointage )
        BouPointer.grid(row = 0, pady = 10, column = 1)
        Bouechelle = Button(ZonePointage, text = 'scale', command = self.linkechelle)
        Bouechelle.grid(row = 0, pady = 10, column = 2 )
    
    def setbind(self):
        self.parent.bind('<Control-o>', self.lienvideobind)
        self.parent.bind('<Control-q>', exit)
        #self.parent.bind('<Control->', )

    def lienvideobind(self,event):
        self.controller.afficher()


    def lienvideo(self):
        self.controller.afficher()

    def lienlecture(self):
        self.controller.lecture()

    def linkpause(self):
        self.controller.pause()

    def linknextimage(self):
        self.controller.next_image()

    def linkreturnfirstimage(self):
        self.controller.returnfirstimage()

    def linkrepere(self):
        self.controller.repere()
    
    def changecolorred(self):
        self.Bourepere.configure( fg="red")

    def changecolorblack(self):
        self.Bourepere.configure( fg="black")

    def linkpointage(self):
        self.controller.pointage()
    
    def linkechelle(self):
        self.controller.echelle()
        
    def linkresetechelle(self):
        self.controller.resetscale()

    def createscale(self, x1, y1, x2, y2, canva):
        distancex = x1 - x2
        distancey = y1 - y2
        if distancex < 0:
            distancex = -distancex
        if distancey < 0:
            distancey = -distancey
        if distancex < distancey:
            canva.create_line(x1, y1, x1, y2, width= 2, fill='purple', tags='scale')
            canva.unbind('<Button-3>')
            return distancey
        if distancex > distancey:
            canva.create_line(x1, y1, x2, y1, width= 2, fill='purple', tags='scale')
            canva.unbind('<Button-3>')
            return distancex

    def createorigin(self,canva):
        (x,y) = self.controller.origindessin
        canva.create_line(x-10, y, x+10, y, width= 2, fill='purple', tags='scale')
        canva.create_line(x, y-10, x, y+10, width= 2, fill='purple', tags='scale')

    def createpoint(self, canva, x, y):
        canva.create_oval(x, y, x, y, width=5, fill="red")
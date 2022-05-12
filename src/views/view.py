from fileinput import close
import tkinter as tk
from turtle import title, width
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
        parent.geometry('1400x700+100+50')
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
        
        Editmenu.add_command(label='Afficher Valeurs', command= self.linktableau)
        Editmenu.add_command(label='SetScale', command= self.linkechelle)
        Editmenu.add_command(label='ResetScale', command= self.linkresetechelle)
        Editmenu.add_command(label='ResetPointage', command= self.linkresetpointage)

        Viewmenu.add_command(label='Affichage graphique y(x)', command= self.linkgraphy_x)
        Viewmenu.add_command(label='Affichage graphique x(t)', command= self.linkgraphx_t)
        Viewmenu.add_command(label='Affichage graphique y(t)', command= self.linkgraphy_t)
        
    def setbouton(self, parent):
        ZoneBoutons = Frame(parent)
        ZoneBoutons.grid(row = 0, column = 0)
        ZoneOptions = LabelFrame(ZoneBoutons , borderwidth = 2, text = 'Options', labelanchor = 'n', width = 200, height = 100)
        ZoneOptions.grid(row = 0, column = 1)

        Boustart = Button(ZoneOptions,text = 'start', command=self.lienlecture)
        Boustart.grid(row = 0, pady = 10, column = 2)
        Boupause = Button(ZoneOptions,text = 'Pause', command= self.linkpause)
        Boupause.grid(row = 0, pady = 10, column = 3)
        BouimageSuivante = Button(ZoneOptions,text = '>>|', command= self.linknextimage)
        BouimageSuivante.grid(row = 0, pady = 10, column = 4)
        BouimagePrecedante = Button(ZoneOptions,text = '|<<', command= 0 )
        BouimagePrecedante.grid(row = 0, pady = 10, column = 1)
        BouimageFirst = Button(ZoneOptions,text = '|<', command= self.linkreturnfirstimage)
        BouimageFirst.grid(row = 0, pady = 10, column = 0)
        BouimageLast = Button(ZoneOptions,text = '>|', command= 0)
        BouimageLast.grid(row = 0, pady = 10, column = 5)

        ZonePointage = LabelFrame(ZoneBoutons , borderwidth = 2, text = 'Pointage', labelanchor = 'n', width = 200, height = 100)
        ZonePointage.grid(row = 0,pady = 5, column = 0)
        self.Bourepere = Button(ZonePointage,text = '+',activebackground= "yellow", command= self.linkrepere )
        self.Bourepere.grid(row = 0, pady = 10, column = 0)
        self.BouPointer = Button(ZonePointage,text = 'x', command= self.linkpointage )
        self.BouPointer.grid(row = 0, pady = 10, column = 1)
        self.Bouechelle = Button(ZonePointage, text = 'scale', command = self.linkechelle)
        self.Bouechelle.grid(row = 0, pady = 10, column = 2 )
    
    def setbind(self):
        self.parent.bind('<Control-o>', self.lienvideobind)
        self.parent.bind('<Control-q>', exit)
        self.parent.bind('<Escape>', self.linkpointageoff )

    def lienvideobind(self,event):
        self.controller.afficher()

    def linkpointageoff(self, event):
        self.controller.putpointageoff()

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

    def linkgraphy_x(self):
        self.controller.creategraph('y_x')

    def linkgraphx_t(self):
        self.controller.creategraph('x_t')

    def linkgraphy_t(self):
        self.controller.creategraph('y_t')

    def linktableau(self):
        self.controller.createtableau()

    def linkrepere(self):
        self.controller.repere()

    def changecolorred(self, bouton):
        if bouton == "repere":
            self.Bourepere.configure( fg="red")
        elif bouton == "pointeur":
            self.BouPointer.configure( fg="red")
        elif bouton == "echelle":
            self.Bouechelle.configure( fg="red")

    def changecolorblack(self, bouton):
        if bouton == "tout":
            self.Bourepere.configure( fg="black")
            self.Bouechelle.configure( fg="black")
            self.BouPointer.configure( fg="black")
        elif bouton == "repere":
            self.Bourepere.configure( fg="black")
        elif bouton == "pointeur":
            self.BouPointer.configure( fg="black")
        elif bouton == "echelle":
            self.Bouechelle.configure( fg="black")

    def linkpointage(self):
        self.controller.pointage()
    
    def linkechelle(self):
        self.controller.echelle()
        
    def linkresetechelle(self):
        self.controller.resetscale()
    
    def linkresetpointage(self):
        self.controller.resetpointage()

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
            self.controller.scalesize = distancey
        if distancex > distancey:
            canva.create_line(x1, y1, x2, y1, width= 2, fill='purple', tags='scale')
            canva.unbind('<Button-3>')
            self.controller.scalesize = distancex

    def createorigin(self,canva):
        (x,y) = self.controller.origindessin
        canva.create_line(x-10, y, x+10, y, width= 2, fill='red', tags='origin')
        canva.create_line(x, y-10, x, y+10, width= 2, fill='red', tags='origin')

    def createpoint(self, canva, x, y):
        canva.create_oval(x, y, x, y, width=5, fill="red", tags='point'+str(self.controller.video.frame))

    def resizewindow(self, vwidth, vheight):
        if vwidth < 580:
            w = 600
        if vheight < 500:
            h = 600
        if vwidth >= 280:
            w= vwidth + 20
        if vheight >= 500:
            h = 90 + vheight
        self.parent.geometry( str(int(w)) + 'x' + str(int(h)))
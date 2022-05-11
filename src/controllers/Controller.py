import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
from tkinter import simpledialog;

class Controller:

    def __init__(self, video, view, point):
        
        self.video = video
        self.view = view
        self.point = point

        self.canvas = self.video.canvas
        self.origin = (0, 0)
        self.origindessin = (0, 0)
        self.takingrepere = False
        self.takingpoint = False
        self.takingscale = False
        self.scale1x = -1
        self.scale1y = -1
        self.scale2x = -1
        self.scale2y = -1
        self.scalesize = -1
        self.scalerealsize = -1


    def afficher(self):
        self.video.openfile()
        self.video.next_frame()

    def lecture(self):
        if self.video.capopen:
            if self.video.pause == True:
                self.video.nopause()
                self.video.play_video()

    def pause(self):
        self.video.putpause()

    def next_image(self):
        if self.video.capopen:
            self.video.next_frame()

    def returnfirstimage(self):
        if self.video.capopen:
            if self.video.pause == False:
                self.video.putpause()
                self.video.returnfirstframe()
                self.video.nopause()
            else:
                self.video.returnfirstframe()
                self.video.next_frame()

    def repere(self):
        if self.video.capopen:
            self.view.changecolorred()
            self.takerepere()

    def pointage(self):
        if self.video.capopen:
            self.view.changecolorblack()
            if self.takingpoint:
                self.takingpoint = False
            else:
                self.canvas.bind('<Button-1>', self.takecoord)
                self.takingpoint = True

    def echelle(self):
        if self.video.capopen:
            self.view.changecolorblack()
            self.takescale()

    def takerepere(self):
        if self.takingrepere:
            self.takingrepere = False
        else:
            self.canvas.bind('<Button-1>', self.takecoord)
            self.takingrepere = True

    def takecoord(self, event):
        xrep,yrep = self.origin
        x = int(self.canvas.winfo_pointerx() - self.canvas.winfo_rootx() )
        yi = int(self.video.canheight) - int(self.canvas.winfo_pointery()) - int(self.canvas.winfo_rooty())  #ordonné inversé du bas vers le haut
        y = int(self.canvas.winfo_pointery() - self.canvas.winfo_rooty() )
        if self.takingrepere:
            self.origin= (x,yi)
            self.origindessin=(x,y)
            self.takingrepere = False
            self.canvas.unbind('<Button-1>')
            self.view.createorigin(self.canvas)
            showinfo('Info', 'Repère placé au coordonnées (' + str(x) + ", "+ str(yi) + ")." )
        if self.takingpoint:
            print(self.video.frame,x-xrep,yi-yrep)
            self.video.next_frame()
            self.view.createpoint(self.canvas, x, y)
            self.trace()
        if self.takingscale:
            if self.scale1x == -1:
                self.scale1x = x
                self.scale1y = y
                print("premier point placé")
            elif self.scale1x != -1 and self.scale2x == -1:
                self.scale2x = x
                self.scale2y = y
                print("deuxieme point placé")
                self.scalesize = self.view.createscale(self.scale1x, self.scale1y, self.scale2x, self.scale2y, self.canvas)
                self.takingscale = False
                self.scalerealsize = int(simpledialog.askstring(title='Echelle', prompt="Veuiller entrer la distance réelle de l'échelle en cm :"))
                showinfo('Info', 'échelle placé : ' + str(self.scalesize) + 'pixels = ' + str(self.scalerealsize) + 'cm.' )



    def takescale(self):
        if self.scale2x != -1:
            showinfo('Info', 'échelle déjà placé : ' + str(self.scalesize) + 'pixels = ' + str(self.scalerealsize) + 'cm.' )
        else:
            if self.takingscale:
                self.takingscale = False
            else:
                self.takingscale = True
                self.canvas.bind('<Button-3>', self.takecoord)
                print("eoeooe")


    def resetscale(self):
        self.canvas.delete('scale')
        self.scale1x = -1
        self.scale1y = -1
        self.scale2x = -1
        self.scale2y = -1

    def trace(self):
        self.view.createorigin(self.canvas)
        self.view.createscale(self.scale1x, self.scale1y, self.scale2x, self.scale2y, self.canvas)
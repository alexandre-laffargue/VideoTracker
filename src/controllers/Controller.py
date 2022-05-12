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
        self.scaleplaced = False
        self.tableau = []


    def afficher(self):
        self.video.openfile()
        if self.video.capopen:
            self.view.resizewindow(self.video.canwidth, self.video.canheight)
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
            self.takingpoint = False
            self.takingscale = False
            self.view.changecolorblack("tout")
            self.view.changecolorred("repere")
            if self.takingrepere:
                self.takingrepere = False
                self.view.changecolorblack("repere")
            else:
                self.canvas.bind('<Button-1>', self.takecoord)
                self.takingrepere = True

    def pointage(self):
        if self.video.capopen:
            self.takingrepere = False
            self.takingscale = False
            self.view.changecolorblack("tout")
            self.view.changecolorred("pointeur")
            if self.takingpoint:
                self.takingpoint = False
                self.view.changecolorblack("pointeur")
            else:
                self.canvas.bind('<Button-1>', self.takecoord)
                self.takingpoint = True

    def echelle(self):
        if self.video.capopen:
            self.takingpoint = False
            self.takingrepere = False
            self.view.changecolorblack("tout")
            self.view.changecolorred("echelle")
            if self.scaleplaced:
                self.view.changecolorblack("echelle")
                showinfo('Info', 'échelle déjà placé : ' + str(self.scalesize) + 'pixels = ' + str(self.scalerealsize) + 'cm.' )
            else:
                if self.takingscale:
                    self.takingscale = False
                    self.view.changecolorblack("echelle")
                else:
                    self.takingscale = True
                    self.canvas.bind('<Button-3>', self.takecoord)


    def takecoord(self, event):
        self.xrep,self.yrep = self.origin
        x = int(self.canvas.winfo_pointerx() - self.canvas.winfo_rootx() )
        yi =  -( int(self.canvas.winfo_pointery()) - int(self.canvas.winfo_rooty()) - int(self.video.canheight))  #ordonné inversé du bas vers le haut
        y = int(self.canvas.winfo_pointery() - self.canvas.winfo_rooty() )
        if self.takingrepere:
            self.origin= (x,yi)
            self.origindessin=(x,y)
            self.takingrepere = False
            self.canvas.unbind('<Button-1>')
            self.view.changecolorblack('repere')
            self.canvas.delete('origin')
            self.view.createorigin(self.canvas)
            showinfo('Info', 'Repère placé au coordonnées (' + str(x) + ", " + str(yi) + ")." )
        if self.takingpoint:
            print("frame =",self.video.frame,"x=",x-self.xrep,"y=",yi-self.yrep)
            
            pt = self.point(self.video.frame, x-self.xrep, yi-self.yrep)
            print('(',pt.getT(), pt.getX(), pt.getY(),')')
            i = self.searchpoint(self.video.frame)
            if i == -1:
                self.tableau.append(pt)
                print('dans le tableau')
                print(self.tableau[0].getT(), self.tableau[0].getX(),self.tableau[0].getY() )
            else:
                self.tableau[i].setX(x-self.xrep)
                self.tableau[i].setY(yi-self.yrep)
                print('dans le tableau')
                print(self.tableau[i].getT(), self.tableau[i].getX(),self.tableau[i].getY() )
            self.video.next_frame()
            self.view.createpoint(self.canvas, x, y)
            self.trace()
        if self.takingscale:
            if self.scale1x == -1:
                self.scale1x = x
                self.scale1y = y
            elif self.scale1x != -1 and self.scale2x == -1:
                self.scale2x = x
                self.scale2y = y
                self.view.createscale(self.scale1x, self.scale1y, self.scale2x, self.scale2y, self.canvas)
                self.takingscale = False
                self.scaleplaced = True
                self.view.changecolorblack('echelle')
                self.scalerealsize = int(simpledialog.askstring(title='Echelle', prompt="Veuiller entrer la distance réelle de l'échelle en cm :"))
                showinfo('Info', 'échelle placé : ' + str(self.scalesize) + 'pixels = ' + str(self.scalerealsize) + 'cm.' )

    def searchpoint(self,frame):
        for i in range(len(self.tableau)):
            if self.tableau[i].getT() == frame:
                return i
        return -1

    def resetscale(self):
        if self.scaleplaced:
            self.canvas.delete('scale')
            self.scaleplaced = False
            self.scale1x = -1
            self.scale1y = -1
            self.scale2x = -1
            self.scale2y = -1

    def trace(self):
        self.view.createorigin(self.canvas)
        self.view.createscale(self.scale1x, self.scale1y, self.scale2x, self.scale2y, self.canvas)
        for i in range(len(self.tableau)):
            frame = self.tableau[i].getT()
            self.canvas.focus('point'+str(frame))
        for i in range(len(self.tableau)):
            x = self.tableau[i].getX() + self.xrep
            y = -(self.tableau[i].getY() + self.yrep) + int(self.video.canheight)
            self.view.createpoint(self.canvas, x, y)
        
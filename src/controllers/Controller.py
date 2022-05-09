import tkinter as tk
from tkinter import *



class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        self.canvas = self.view.canvas

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
            self.video.takerepere()
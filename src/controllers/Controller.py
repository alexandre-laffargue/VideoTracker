import tkinter as tk
from tkinter import *



class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view
        self.canvas = self.view.canvas

    def afficher(self):
        print('b')
        self.video.openfile()
        self.video.next_frame()

    def lecture(self):
        if self.video.pause == True:
            self.video.nopause()
            self.video.play_video()

    def pause(self):
        self.video.putpause()

    def next_image(self):
        self.video.next_frame()

    def returnfirstimage(self):
        if self.video.pause == False:
            self.video.putpause()
            self.video.returnfirstframe()
        else:
            self.video.returnfirstframe()
            self.video.next_frame()


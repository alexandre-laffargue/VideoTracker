import tkinter as tk
from tkinter import *



class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view


    def afficher(self):
        print('b')
        self.video.openfile(self.view)

    def lecture(self):
        self.video.nopause()
        self.video.play_video(self.view)

    def pause(self):
        self.video.pause()

    def next_image(self):
        self.video.next_frame(self.view)

            
            

        

        
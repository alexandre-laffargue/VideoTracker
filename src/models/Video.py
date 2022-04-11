from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL.Image, PIL.ImageTk
import cv2

class Video:

    def __init__(self):
        pass


    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            pass

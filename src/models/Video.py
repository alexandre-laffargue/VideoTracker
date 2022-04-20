from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL.Image, PIL.ImageTk
import cv2
from tkinter.filedialog import askopenfilename
import time

class Video:

    def __init__(self):
        self.cap = None
        self.delay = 0.015 #s
        self.pause = None

    def openfile(self, fen):
        print("c")
        listtypes = [("Fichier vidéo", ".mp4"),("Script python", ".py")]
        filename = askopenfilename(title="Sélectionner une vidéo", filetypes=listtypes) 
        print(filename)
        self.cap = cv2.VideoCapture(filename)
        video_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        video_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fen.canvas.config(width = video_width, height = video_height)
        fframe = self.get_first_frame()
        fframe = self.get_first_frame()
        fen.canvas.create_image(0, 0, image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(fframe)), anchor = NW)
        print('first image')

    def get_first_frame(self):   
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            return (cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        except:
            pass
    def nopause(self):
        self.pause = False

    def pause(self):
        self.pause = True

    def play_video(self, fen):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            fen.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            print("a")
            time.sleep(self.delay)
            print("c")
            self.play_video(fen)


    def next_frame(self, fen):
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            fen.canvas.create_image(0, 0, image = self.photo, anchor = NW)

    def _del(self):
        if self.cap.isOpened():
            self.cap.release()
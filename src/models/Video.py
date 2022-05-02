from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL.Image, PIL.ImageTk
import cv2
from tkinter.filedialog import askopenfilename
import time

class Video:

    def __init__(self, parent):
        self.cap = None
        self.delay = 15 #ms
        self.pause = True
        ZoneVideo = Frame(parent, borderwidth = 2, relief = RIDGE)
        ZoneVideo.grid(row = 1, column = 0)
        self.canvas = Canvas(ZoneVideo, bg = 'gray', width = 840, height = 450)
        self.canvas.pack()
        self.filename = None

    def openfile(self):
        print("c")
        listtypes = [("Fichier vidéo", ".mp4"),("Script python", ".py")]
        self.filename = askopenfilename(title="Sélectionner une vidéo", filetypes=listtypes) 
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        video_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        video_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = video_width, height = video_height)

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

    def putpause(self):
        self.pause = True

    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        try:
            ret, frame = self.get_frame()
            if ret:
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
            if not self.pause:
                self.canvas.after(self.delay, self.play_video)
        except:
            print("fin")
    
    def next_frame(self):
        ret, frame = self.get_frame()
        if ret and self.pause:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

    def returnfirstframe(self):
        self.cap = cv2.VideoCapture(self.filename)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
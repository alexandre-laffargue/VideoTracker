from tkinter import *
from tkinter import messagebox
from turtle import title
import PIL.Image, PIL.ImageTk
import cv2
from tkinter.filedialog import askopenfilename

class Video:

    def __init__(self):
        pass

    def openfile(self):
        listtypes = [("Fichier vidéo", ".mp4"),("Script python", ".py")]
        filename = askopenfilename(title="Sélectionner une vidéo", filetypes=listtypes) 
        print(filename)
        cap = cv2.VideoCapture(filename)
        video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = video_width, height = video_height)
        fframe = self.get_first_frame()
        self.canvas.create_image(0, 0, image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(fframe)), anchor = NW)

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

    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            print('ret')
            print(ret)
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
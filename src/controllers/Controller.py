import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import PIL.Image, PIL.ImageTk
import cv2

from models.Video import Video


class Controller:

    def __init__(self, video, view):
        
        self.video = video
        self.view = view

    def ChargerVideo(self):
        video = Entry(parent,bg="white")
        user = Label(root, text = "Mettre le lien de la vidéo")
        user.pack()
        user_Entry.pack()
        parent.mainloop()

    def openfile(self):
        listtypes = [("Fichier vidéo", ".mp4"),("Script python", ".py")]
        filename = askopenfilename(title="Sélectionner une vidéo", filetypes=listtypes) 
        print(filename)
        cap = cv2.VideoCapture(filename)
        video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = video_width, height = video_height)
        self.canvas.create_image(0, 0, image = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(Video.get_first_frame(self))), anchor = NW)
        

            
            

        

        
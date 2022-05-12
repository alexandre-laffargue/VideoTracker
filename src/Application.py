import tkinter as tk
from controllers.Controller import Controller
from models.Video import Video
from views.view import View
from models.Point import Point
from models.Graph import Graph
from models.Tableau import Tableau

class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title('Video Tracker')
        # create a video model
        video = Video(self)
    
        # create a view and place it on the root window
        view = View(self)
        # create a controller
        controller = Controller(video, view, Point, Graph, Tableau)

        # set the controller to view
        view.setController(controller)
        
if __name__ == '__main__':
    app = Application()
    app.mainloop()
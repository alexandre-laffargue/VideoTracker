from tkinter import *

class Graph:
    
    def __init__(self,parent):
        graph = Toplevel(parent)
        self.repere = (0, 0)
        self.canvas= Canvas(graph, width=800, height=800, bg="white")
        self.canvas.pack()
        self.draw_grid()
        self.draw_axes()
        
        graph.mainloop()
        
    
    def draw_grid(self):
        for i in range(50,800,50):
            self.canvas.create_line ((i, 0), (i, 800), 
                        fill="gray", width=2, dash=(8,4))
        for j in range(50, 800, 50):
            self.canvas.create_line ((0, j), (800, j), 
                        fill="gray", width=2, dash=(8,4))
    
    def draw_axes(self):
        self.canvas.create_line ((0, 0), (800, 800), 
                        fill="red", width=2,)
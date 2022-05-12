from tkinter import *
import matplotlib.pyplot as plt; plt.rcdefaults()

class Graph:

    def __init__(self,parent, data, coef, graphique):
        self.parent = parent
        self.data = data
        self.coef = coef
        self.graphique = graphique
        self.createtab()
        self.creategraph()


    def createtab(self):
        self.t = []
        self.x = []
        self.y = []
        
        for i in range(len(self.data)):
            self.t.append(self.data[i].getT())
            self.x.append(self.data[i].getX())
            self.y.append(self.data[i].getY())

    def creategraph(self):
        if self.graphique == 'y_t':
            plt.plot(self.t, self.y, 'ro')
            plt.title('Graph des positions Y en fonction du temps ')
            plt.ylabel('Position X')
            plt.xlabel('Temps')
        elif self.graphique == 'x_t':
            plt.plot(self.t, self.x, 'ro')
            plt.title('Graph des positions X en fonction du temps ')
            plt.ylabel('Position X')
            plt.xlabel('Temps')
        elif self.graphique == 'y_x':
            plt.plot(self.x, self.y, 'ro')
            plt.title('Graph des positions Y en fonction de X ')
            plt.ylabel('Position Y')
            plt.xlabel('Position X')

        plt.show()









'''        
        self.canvas= Canvas(graph, width=800, height=800, bg="white")
        self.canvas.pack()
        self.minmax()
        self.draw_grid()
        self.draw_timeaxe()
        graph.mainloop()
        
    def minmax(self):
        if self.data == []:
            return
        self.minY = self.data[0].getY()*self.coef
        self.maxY = self.data[0].getY()*self.coef
        self.minX = self.data[0].getX()*self.coef
        self.maxX = self.data[0].getX()*self.coef
        for i in range(len(self.data)):
            y = self.data[i].getY()*self.coef
            x = self.data[i].getX()*self.coef
            if self.minY > y:
                self.minY = y
            if self.maxY < y:
                self.maxY = y
            if self.minX > x:
                self.minX = x
            if self.maxX < x:
                self.maxX = x
        self.distance()        

    def distance(self):
        diffx =self.maxX-self.minX
        diffy = self.maxY-self.minY
        distanceaxex = diffx//16
        distanceaxey = diffy//16
        print(distanceaxex, distanceaxey)

    def draw_grid(self):
        for i in range(50,800,50):
            self.canvas.create_line ((i, 0), (i, 800), 
                        fill="gray", width=2, dash=(8,4))
        for j in range(50, 800, 50):
            self.canvas.create_line ((0, j), (800, j), 
                        fill="gray", width=2, dash=(8,4))
    
    def draw_timeaxe(self):
        self.canvas.create_line ((0, 750), (800, 750), 
                        fill="red", width=2,) '''
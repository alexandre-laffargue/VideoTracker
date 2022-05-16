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
            self.x.append(self.data[i].getX()*self.coef)
            self.y.append(self.data[i].getY()*self.coef)

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
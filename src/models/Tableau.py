from tkinter import *
from tkinter.ttk import Treeview

class Tableau:
    
    def __init__(self, parent, data):
        self.data = data
        self.tab = Toplevel(parent)
        self.table()
        self.entervalue()
        self.tab.mainloop()
        
    
    def table(self):
        self.tableau = Treeview(self.tab, columns=('temps', 'x', 'y'))

        self.tableau.heading('temps', text='Temps')
        self.tableau.heading('x', text='Position X')
        self.tableau.heading('y', text='Position Y')

        self.tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

        self.tableau.pack(padx = 10, pady = (0, 10))

    def entervalue(self):
        for i in range(len(self.data)):
            self.tableau.insert('', 'end', iid=self.data[i].getT(), values=(self.data[i].getT(), self.data[i].getX(),self.data[i].getY()))
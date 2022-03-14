import string
from Point import Point
import os

class FileRepo:

    def __init__(self,filename) -> None:
        self.filename = filename
        
    
    def export2CSV(self, data:list, filename:str):


        csv = self.TransformData2CSV(data)
        file = open( filename + ".csv", "w")
        try:
            file.write(csv)
        except:
            print("a")    
        file.close()

    def TransformData2CSV(self, data:list)->str: # > 1;5\n8;4\n1;5\n1;5\n

        csv = ""
        for i in data:
            csv += str(i.x)+";"+str(i.y)+ "\n"
        return csv

'''
f = FileRepo("filetest")

#data:list
P1 = Point(57987,3)
P2 = Point(55,34987)
P3 = Point(56,328)

data = [P1,P2,P3]

f.export2CSV(data,"test")

fil = open("test.csv", "r")
print(fil.read())

'''
"x1;y1\nx2;y2\nx3;y3\n....\nxn;yn\n"


'''

filename.csv -> _______
                |x1;y1|-- editeur de texte
                |x2;y2|                     |A | B|
                |x3;y3|                     |x1|y1|
                |xn;yn| ----> tableur ----> |x2|y2|
                                            |xn|yn|
'''

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
            print("fail")    
        file.close()

    def TransformData2CSV(self, data:list)->str: # > 1;5\n8;4\n1;5\n1;5\n

        csv = ""
        for i in data:
            csv += str(i.t) + ";" + str(i.x) + ";" + str(i.y) + "\n"
        return csv

'''
f = FileRepo("filetest")

#data:list
P1 = Point(3,57987,3)
P2 = Point(6,55,34987)
P3 = Point(9,56,328)

data = [P1,P2,P3]

f.export2CSV(data,"test")

fil = open("test.csv", "r")
print(fil.read())

'''
"t1;x1;y1\nt2;x2;y2\nt3;x3;y3\n....\ntn;xn;yn\n"


'''

filename.csv -> _______
                |t1;x1;y1|-- editeur de texte
                |t2;x2;y2|                     | A| B| C|
                |t3;x3;y3|                     |t1|x1|y1|
                |tn;xn;yn| ----> tableur ----> |t2|x2|y2|
                                               |tn|xn|yn|
'''

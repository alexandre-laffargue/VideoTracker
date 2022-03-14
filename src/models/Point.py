class Point:          # > programmation objet python  , pas d'heritage

    def __init__(self,x:float,y:float): # > (3,4)
        self.x = x               #   > self.__x = x  "__" montre que c privée
        self.y = y

    def getX(self)->float:
        return self.x

    def getY(self)->float:
        return self.y


    def setx(self,x):
        self.x = x

    def sety(self,y):
        self.y = y


pt = Point(5,9)          # pt -> référence l'objet de type Point possédant les valeurs (x,y), référence a la case mémoire
'''
print(pt.getX())
print(pt.getY())

print(id(pt))

pt.setx(99999999)
pt.sety(9)

print(id(pt))
#print(pt.getX)
#print(pt.getY)
'''
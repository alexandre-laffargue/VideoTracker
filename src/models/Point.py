class Point:          # > programmation objet python  , pas d'heritage

    def __init__(self,t:float,x:float,y:float): # > (1,3,4)
        self.x = x               #   > self.__x = x  "__" montre que c privée
        self.y = y
        self.t = t

    def getX(self)->float:
        return self.x

    def getY(self)->float:
        return self.y

    def getT(self)->float:
        return self.t


    def setX(self,x):
        self.x = x

    def setY(self,y):
        self.y = y

    def setT(self,t):
        self.t = t


pt = Point(1,5,9)          # pt -> référence l'objet de type Point possédant les valeurs (x,y), référence a la case mémoire
'''
print(pt.getX())
print(pt.getY())

print(id(pt))

pt.setX(99999999)
pt.setY(9)

print(id(pt))
#print(pt.getX)
#print(pt.getY)
'''
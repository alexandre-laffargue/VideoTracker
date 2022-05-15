import unittest
from src.models.Point import Point
from src.models.FileRepo import FileRepo

class Test_filerepo(unittest.TestCase):

    def setUp(self) -> None:
        
        self.p1 = Point(0,1,3)
        self.p2 = Point(1,4,6)
        self.p3 = Point(3,5,8)
        self.data = [self.p1,self.p2, self.p3]
        self.file = FileRepo(self.data, "filetest", 1)

    def tearDown(self):
        pass

    def test_transform2str(self):
        csv = self.file.TransformData2CSV(self.data)
        self.assertEqual(csv, "0;1;3\n1;4;6\n3;5;8\n")

    def test_export(self):
        self.file.export2CSV(self.data,"test")
        csv = open("test.csv", "r")
        self.assertEqual(csv.read() , "0;1;3\n1;4;6\n3;5;8\n")
        csv.close()

    def test_editpoint(self):
        self.p1.setX(2)
        self.p1.setY(4)
        self.assertTrue(self.p1.getX() == 2)
        self.assertTrue(self.p1.getY() == 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
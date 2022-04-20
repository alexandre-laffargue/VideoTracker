import unittest
import sys
sys.path.append("../src/models")
from Point import Point
from FileRepo import FileRepo



class Test_filerepo(unittest.TestCase):

    def setUp(self) -> None:
        self.file = FileRepo("filetest")
        self.p1 = Point(1,3)
        self.p2 = Point(4,6)
        self.p3 = Point(5,8)
        self.data = [self.p1,self.p2, self.p3]

    def tearDown(self):
        pass

    def test_transform2str(self):
        csv = self.file.TransformData2CSV(self.data)
        self.assertEqual(csv, "1;3\n4;6\n5;8\n")

    def test_export(self):
        self.file.export2CSV(self.data,"test")
        csv = open("test.csv", "r")
        self.assertEqual(csv.read() , "1;3\n4;6\n5;8\n")
        csv.close()

    def test_editpoint(self):
        self.p1.setx(2)
        self.p1.sety(4)
        self.assertTrue(self.p1.getX() == 2)
        self.assertTrue(self.p1.getY() == 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
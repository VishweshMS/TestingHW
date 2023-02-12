# -*- coding: utf-8 -*-
"""
Updated Feb 10, 2023
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Vishwesh Malur Somashekar

"""

import unittest

from Triangle import classifyTriangle,my_brand

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(33,33,33),'Equilateral','33,33,33 should be equilateral')
        
    def testEquilateralTriangleC(self): 
        self.assertEqual(classifyTriangle(6,6,6),'Equilateral','6,6,6 should be equilateral')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(8,10,10),'Isosceles','8,10,10 is a Isosceles Triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(12, 14, 14),'Isosceles','12, 14, 14 is a Isosceles Triangle')

    def testIsoscelesTriangleC(self): 
        self.assertEqual(classifyTriangle(9, 6, 9),'Isosceles','9, 6, 9 is a Isosceles Triangle')
        
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(12, 15, 20),'Scalene','12, 15, 20 should be Scalene Triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(25, 30, 35),'Scalene','25, 30, 35 should be Scalene Triangle')

    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle(40, 45, 55),'Scalene','40, 45, 55 is a Scalene Triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(9, 12, 15),'Right','9, 12, 15 is a Right triangle')
        
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 12, 13),'Right','5, 12, 13 should be Right Triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(8, 15, 17),'Right','8, 15, 17 should be Right Triangle')

    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(6,8,15),'NotATriangle','6,8,15 cannot form a Triangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(10,11,21),'NotATriangle','10,11,21 cannot form a Triangle')

    def testNotATriangleC(self): 
        self.assertEqual(classifyTriangle(9,13,22),'NotATriangle','9,13,22 cannot form a Triangle')

    def testInvalidDataA(self): 
        self.assertEqual(classifyTriangle(-1, 2, 3),'InvalidInput','-1, 2, 3 is a Invalid Data')
        
    def testInvalidDataB(self): 
        self.assertEqual(classifyTriangle(1.1, 2, 3),'InvalidInput','1.1, 2, 3 is a Invalid Data')

    def testInvalidDataC(self): 
        self.assertEqual(classifyTriangle(0, 0, 1),'InvalidInput','0, 0, 1 is a Invalid Data')


if __name__ == '__main__':
    my_brand("HW 02A")
    print('Running unit tests')
    unittest.main()
    my_brand("HW 02A")


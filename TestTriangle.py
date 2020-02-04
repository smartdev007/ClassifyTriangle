# -*- coding: utf-8 -*-
"""
Updated Feb 2, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Jenish Kevadia
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(4,3,5), ('Right'))
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle('1',3,5), ('InvalidInput'))
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle('',3,5), ('InvalidInput'))

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(5,3,4), ('Scalene'))
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(4,'a',0), ('InvalidInput'))
    def testScaleneTriangleC(self): 
        self.assertEqual(classifyTriangle('','a',1), ('InvalidInput'))

    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1), ('Equilateral'))
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle('1','a',1), ('InvalidInput'))
    def testEquilateralTriangleC(self): 
        self.assertEqual(classifyTriangle('',1,1), ('InvalidInput'))
    
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,1), ('Isoceles'))
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(1,'',1), ('InvalidInput'))
    def testIsoscelesTriangleC(self): 
        self.assertEqual(classifyTriangle(1,2,'1'), ('InvalidInput'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


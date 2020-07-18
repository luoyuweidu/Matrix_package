# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest
from matrix_manipulation import Matrix

class MatrixTest(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(2, 2)
        self.matrix[0] = [1,2]
        self.matrix[1] = [3,4]
     
    def test_initialization(self):
        mat = self.matrix
        self.assertEqual(mat.values, [[1,2],[3,4]], 'incorrect matrix')
        
    def test_transpose(self):
        mat = self.matrix 
        res = mat.getTranspose()
        self.assertEqual(res.values, [[1,3],[2,4]], 'Transposed matrix not as expected')
    
    def test_getShape(self):
        mat = self.matrix 
        size = mat.getShape()
        self.assertEqual(size, (2,2), 'Size not as expected')
    
    def test_matrixAdd(self):
        mat_1 = self.matrix
        mat_2 = Matrix(2, 2)
        mat_sum = mat_1 + mat_2 
        
        self.assertEqual(mat_sum.values, [[1,2],[3,4]])
        
    def test_matrixSub(self):
        mat_1 = self.matrix
        mat_2 = Matrix(2, 2)
        mat_sub = mat_1 + mat_2 
        
        self.assertEqual(mat_sub.values, [[1,2],[3,4]])
        
    def test_matrixMul(self):
        mat_1 = self.matrix
        mat_2 = Matrix(2, 2)
        mat_mul = mat_1 * mat_2 
        print(mat_mul)
        self.assertEqual(mat_mul.values, [[0,0],[0,0]])
        
        
if __name__ == '__main__':
    unittest.main()
        
class Matrix():
    
    def __init__(self, m, n):
        """Matrix class to perform simple algrbra such as 
        addition, substraction, multiplication, matrix inversion

        Attributes:
            values (matrix) representing matrix values 
            m representing the number of rows of the matrix
            n representing the number of columns of the matrix
        """
        
        self.values = [[0]*n for x in range(m)]
        self.m = m
        self.n = n
    
    def __getitem__(self, idx):
        """
        Method to get value from a matrix by index. Index can be in [i] or [i][j] format

        Args:
            idx: index of the matrix

        Return:
            value of the corresponding index 
        """
        return self.values[idx]
    
    def __setitem__(self, idx, item):
        """method to set value in matrix by calling the index

        Args:
            idx: index of the matrix
        """
        self.values[idx] = item
        
    def getTranspose(self):
        """Return a transpose of matrix"""
    
        ret = Matrix(self.n, self.m)
        ret.values = [list(item) for item in zip(*self.values)]
        return ret
    
    def getShape(self):
        """method to get the shape of the matrix
        """
        return (self.m, self.n)
    
    def __add__(self, mat):
        """method to add two matrices together 

        Args:
            mat (matrix) the matrix to add to the original matric

        Returns:
            A new matrix that is the sum of two matrices
        """
        if self.getShape() != mat.getShape():
            raise "Trying to add matrixes of varying size!"
        else:
            ret = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    ret[i][j] = self[i][j] + mat[i][j]
        
        return ret
    
    def __substract__(self, mat):
        """method to substract a matrix from the original matrix

        Args:
            mat(matrix) the matrix to substract from the original matrix

        Return:
            A new matrix which is th result of substraction
        """
        if self.getShape() != mat.getShape():
            raise "Trying to substract matrixes of varying size!"
        else:
            ret = Matrix(self.m, self.n)
            for i in range(self.m):
                for j in range(self.n):
                    ret[i][j] = self[i][j] - mat[i][j]
        
        return ret
    
    def __mul__(self, mat):
        
        """method to calculate multipliction of two matrics
    
           Args:
           mat(matrix) the matrix to multiply with the original matrix 
    
           Return:
           A new matrix which is th result of multipliction 
        """
        if self.n != mat.m:
            raise "Two matrics are not multiplicable"
        else:
            mat_t = mat.getTranspose()
            ret = Matrix(self.m, mat.n)
            for i in range(self.m):
                for j in range(mat.n):
                    ret[i][j] = sum([item[0]*item[1] for item in zip(self.values[i], mat_t.values[j])])
         
        return ret
        
        
import numpy as np
a=np.array(input('Enter any array:'))
b=np.array(input('Enter another array:'))
c=np.linalg.det(a) 
print('Det of a matrix a',c)
d=np.linalg.matrix_rank(a)
print('Rank of a matrix a',d)
e=np.trace(a)
print('Trace of a matrix a',e)
f=np.linalg.inv(a)
print('Inverse of a matrix a',f)
g=np.linalg.eigvals(a)
print('Eigen values of a matrix a',g)
h=np.linalg.matrix_power(a,4) 
print('Matrix Power of a matrix a',h)
j=np.add(a,b)
print('Addition of two matrices',j)
i=np.subtract(a,b) 
print('Subtraction of two matrices',i)
k=np.multiply(a,b)
print('Element by element multiplication of two matrices',k)
l=np.dot(a,b)
print('Multiplication of two matrices',l)
m=np.divide(a,b) 
print('Element by element division of two matrices',m)
n=np.linalg.solve(a,b)
print('Solution of linear equations',n)
o=np.linalg.qr(a) 
print('qr decomposition of matrix',o)

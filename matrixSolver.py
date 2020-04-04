""""
This solution  uses python numpy package for data science to solve matrix determinants.
Python Numpy package enables operations on arrays with number elements. You can either read these elements from a csv file
using pandas or collect it as input from users.
Here, we collected the matrix elements as input from users. Then, we use a function called linalg.det from numpy to solve the
determinants
"""

import numpy as np

def tBYt():
    x1 = int(input('X1: '))
    x2 = int(input('X2: '))
    y1 = int(input('Y1: '))
    y2 = int(input('Y2: '))

    matrix = np.array([[x1, x2], [y1, y2]])
    print('The determinant of your matrix is: ' + str(np.linalg.det(matrix)))

def trBYtr():
    x1 = int(input('X1: '))
    x2 = int(input('X2: '))
    x3 = int(input('X3: '))
    y1 = int(input('Y1: '))
    y2 = int(input('Y2: '))
    y3 = int(input('Y3: '))
    z1 = int(input('Z1: '))
    z2 = int(input('Z2: '))
    z3 = int(input('Z3: '))

    matrix = np.array([[x1, x2, x3], [y1, y2, y3], [z1, z2, z3]])
    print('The determinant of your matrix is: ' + str(np.linalg.det(matrix)))


def fBYf():
    a1 = int(input('a1: '))
    b1 = int(input('b1: '))
    c1 = int(input('c1: '))
    V1 = int(input('V1: '))
    a2= int(input('a2: '))
    b2 = int(input('b2: '))
    c2 = int(input('c2: '))
    V2 = int(input('V2: '))
    a3 = int(input('a3: '))
    b3 = int(input('b3: '))
    c3 = int(input('c3: '))
    V3 = int(input('V3: '))
    a4 = int(input('a4: '))
    b4 = int(input('b4: '))
    c4 = int(input('c4: '))
    V4 = int(input('V4: '))


    matrix = np.array([[a1, b1, c1, V1], [a2, b2, c2, V2], [a3, b3, c3, V3], [a4, b4, c4, V4]])
    print('The determinant of your matrix is: ' + str(np.linalg.det(matrix)))

def fvBYfv():
    a1 = int(input('a1: '))
    b1 = int(input('b1: '))
    c1 = int(input('c1: '))
    d1 = int(input('d1: '))
    V1 = int(input('V1: '))
    a2= int(input('a2: '))
    b2 = int(input('b2: '))
    c2 = int(input('c2: '))
    d2 = int(input('d2: '))
    V2 = int(input('V2: '))
    a3 = int(input('a3: '))
    b3 = int(input('b3: '))
    c3 = int(input('c3: '))
    d3 = int(input('d3: '))
    V3 = int(input('V3: '))
    a4 = int(input('a4: '))
    b4 = int(input('b4: '))
    c4 = int(input('c4: '))
    d4 = int(input('d4: '))
    V4 = int(input('V4: '))
    a5 = int(input('a5: '))
    b5 = int(input('b5: '))
    c5 = int(input('c5: '))
    d5 = int(input('d5: '))
    V5 = int(input('V5: '))


    matrix = np.array([[a1, b1, c1, d1, V1], [a2, b2, c2, d2, V2], [a3, b3, c3, d3, V3], [a4, b4, c4, d4, V4], [a5, b5, c5, d5, V5]])
    print('The determinant of your matrix is: ' + str(np.linalg.det(matrix)))


matrix_type = input("Enter matrix type. e.g. 2 by 2, 3 by 3, 4 by 4 or 5 by 5: ")
if matrix_type == "2 by 2":
    tBYt()
elif matrix_type == "3 by 3":
    trBYtr()
elif matrix_type == "4 by 4":
    fBYf()
elif matrix_type == "5 by 5":
    fvBYfv()
else:
    print('Matrix type not recognised')


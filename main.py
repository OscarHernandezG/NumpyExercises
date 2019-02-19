import numpy as np



if __name__ == '__main__':

    floatVector = np.zeros(shape=10)

#    print(floatVector)

    floatVector[4] = 1

 #   print(floatVector)


    intVector = np.arange(10, 50)

#    print(intVector)

    matrix = np.array(np.arange(1, 10)).reshape(3, 3)

    matrix = np.flip(matrix, 0)

    print(matrix)


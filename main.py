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

#   print(matrix)

    identity = np.eye(3)

#    print(identity)

    randomMat = np.random.random((3, 3))

#    print(randomMat)

    randomVec = np.random.randint(0, 10, 10)
    average = randomVec.mean()

#    print(randomVec)
#    print(average)

    mat01 = np.zeros((10, 10))

    mat01[0, :] = 1
    mat01[9, :] = 1
    mat01[:, 9] = 1
    mat01[:, 0] = 1

#    print(mat01)

    mat55 = np.zeros((5, 5))
    mat55[:] = np.matrix(np.arange(1, 6))

#    print(mat55)

    randomArray = np.float64(np.random.randint(0, 10, 9).reshape(3, 3))

#    print(randomArray)

    randomArray2 = np.random.randint(0, 100, 25).reshape(5, 5)

    randomArray2 = np.subtract(randomArray2, np.mean(randomArray2))

#    print(randomArray2)

    randomArray3 = np.random.randint(0, 100, 25).reshape(5, 5)

    for i in range(0, 5):
        randomArray3[i, :] = np.subtract(randomArray3[i, :], np.mean(randomArray3[i, :]))

    print(randomArray3)



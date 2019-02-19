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

    print(randomVec)
    print(average)



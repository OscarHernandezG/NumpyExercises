import numpy as np
import cv2


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

#    print(randomArray3)

    randomMat2 = np.random.random((5, 5))

    idx = (np.abs(randomMat2 - 0.5)).argmin()
    x = int(idx / 5)
    y = int(idx % 5)
    closestValue = randomMat2[x, y]

#    print(closestValue)

    randomMat3 = np.random.randint(0, 10, 9).reshape(3, 3)

    greater = randomMat3[randomMat3 > 5]

#    print(np.size(greater))


    image = np.zeros((64, 64), np.uint8)

    line = np.arange(0, 255, 256/64, np.uint8)

    image[:] = line

    cv2.imshow("image", image)
    cv2.waitKey(0)


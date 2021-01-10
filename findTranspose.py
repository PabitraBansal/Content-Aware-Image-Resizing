import numpy as np
import energy
import findSeam
import reduceImage

def findTranspose(image, shapeReduction):
    '''
        Compute the bitmask which gives the order in which the seams must be removed.
        Parameters:
            image: Image to be reduced.
            shapeReduction: Tuple with 2 elements reduction in rows and columns.
        Returns:
            T: The matrix for dynamic programing.
            bitMask: Order in which the rows/columns need to be removed.
    '''
    T = np.zeros((shapeReduction[0]+1, shapeReduction[1]+1), dtype='double')
    bitMask = np.ones_like(T) * -1

    # Removing horizontal seams
    imageNoRow = image
    for i in range(1, T.shape[0]):
        e = energy.energyRGB(imageNoRow)
        optSeamMask, seamEnergyRow = findSeam.findSeam(e.T)
        imageNoRow = reduceImage.reduceImageByMask(imageNoRow, optSeamMask, 0)
        bitMask[i, 0] = 0

        T[i, 0] = T[i - 1, 0] + seamEnergyRow

    # Removing veertical seams
    imageNoColumn = image
    for j in range(1, T.shape[1]):
        e = energy.energyRGB(imageNoColumn)
        optSeamMask, seamEnergyColumn = findSeam.findSeam(e)
        imageNoColumn = reduceImage.reduceImageByMask(imageNoColumn, optSeamMask, 1)
        bitMask[0, j] = 1

        T[0, j] = T[0, j - 1] + seamEnergyColumn

    # Computing the T matrix using dynamic programming
    for i in range(1, T.shape[0]):
        imageWithoutRow = image
        for j in range (1, T.shape[1]):
            e = energy.energyRGB(imageWithoutRow)

            # Finding seam and seamEnergy in horizontal dierction
            optSeamMaskRow, seamEnergyRow = findSeam.findSeam(e.T)
            imageNoRow = reduceImage.reduceImageByMask(imageWithoutRow, optSeamMaskRow, 0)

            # Finding seam and seamEnergy in verticlal direction
            optSeamMaskColumn, seamEnergyColumm = findSeam.findSeam(e)
            imageNoColumn = reduceImage.reduceImageByMask(imageWithoutRow, optSeamMaskColumn, 1)

            # Choosing the minimum cost option
            neighbors = [(T[i - 1, j] + seamEnergyRow), (T[i, j - 1] + seamEnergyColumn)]
            val = np.min(neighbors)
            ind = np.argmin(neighbors)

            T[i, j] = val                   # Updating T
            bitMask[i, j] = ind             # Updating bitMask

            imageWithoutRow = imageNoColumn

        e = energy.energyRGB(image)
        [optSeamMaskRow, seamEnergyRow] = findSeam.findSeam(e.T)
        image = reduceImage.reduceImageByMask(image, optSeamMaskRow, 0)

    return T, bitMask
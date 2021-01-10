import numpy as np
import energy
import matplotlib.image as mpimg

def findSeam(e):
    '''
        The function finds a seam with least energy using dynamic programing.
        Parameter:
            e: Energy of the current image
        
        Returns:
            optSeamMask: Optimal seam.
            seamEnergy: Energy of the optimal seam.
    '''

    # Traverse the image from the second row to the last row
    # and compute the cumulative minimum energy M for all possible
    # connected seams for each entry (i, j):
    # M(i, j) = e(i, j)+ min(M(i−1, j −1),M(i−1, j),M(i−1, j +1))

    M = np.copy(e)
    for i in range(1, M.shape[0]):
        for j in range(M.shape[1]):
            if j-1 < 0:
                M[i, j] += np.min([M[i-1, j], M[i-1, j+1]])
            elif j+1 >= M.shape[1]:
                M[i, j] += np.min([M[i-1, j-1], M[i-1, j]])
            else:
                 M[i, j] += np.min([M[i-1, j-1], M[i-1, j], M[i-1, j+1]])
 
    print(M.shape, e.shape)
    val = np.min(M[-1])         # Finding the minimum value in the last column
    ind = np.argmin(M[-1])      # Finding the index of the minimum value

    seamEnergy = val
    optSeamMask = np.zeros_like(e, dtype=np.uint8)

    # Backtracing to get the optimal Seam mask
    for i in reversed(range(1, M.shape[0])):
        optSeamMask[i, ind] = 1
        if ind-1 < 0:
            neighbors = min([M[i-1, ind], M[i-1, ind+1]])
            val = np.min(neighbors)
            indInc = np.argmin(neighbors)
            ind += indInc
        elif ind+1 >= e.shape[1]:
            neighbors = min([M[i-1, ind-1], M[i-1, ind]])
            val = np.min(neighbors)
            indInc = np.argmin(neighbors)
            ind += indInc - 1
        else:
            neighbors = [M[i - 1, ind - 1], M[i - 1, ind], M[i - 1, ind + 1]]
            val = np.min(neighbors)
            indInc = np.argmin(neighbors)
            ind += indInc - 1
        seamEnergy = seamEnergy + val

    optSeamMask[0, ind] = 1

    # Converting mask to boolean for making deleting of seam easy
    optSeamMask = ~(optSeamMask.astype(np.bool))

    return optSeamMask, seamEnergy

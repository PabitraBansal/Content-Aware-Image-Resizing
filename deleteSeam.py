import numpy as np
import energy
import findSeam

def deleteSeam(bitMask, shapeReduction, image, func):
    '''
        Function finds the seam in the direction (horizontal / verticle) as specified by the bit mask 
        and removes it from the image.

        Paramteres:
            bitMask: bit mask tells thee direction from which seam must be deleted.
            shapeReduction: Difference in shape of the input and output image.
            image: Input image
            func: The function to be used for removing seams.
    '''
    i = bitMask.shape[0]        # Difference in number of rows
    j = bitMask.shape[1]        # Difference in number of columns

    # Looping and removing seams 
    for k in range(shapeReduction[0] + shapeReduction[1]):

        # Calculating energy of current image
        e = energy.energyRGB(image)

        if (bitMask[i-1, j-1] == 0):
            # Removing horizontal seam
            optSeamMask, seamEnergy = findSeam.findSeam(e.T)    # Finding optimal seam
            image = func(image, optSeamMask, 0)                 # Removing the seam
            i -= 1
        else:
            # Removing vertical seam
            optSeamMask, seamEnergy = findSeam.findSeam(e)      # Finding optimal seam
            image = func(image, optSeamMask, 1)                 # Removing the seam
            j -= 1

    return image, optSeamMask, e
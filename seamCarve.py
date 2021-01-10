import numpy as np
import findTranspose
import deleteSeam
import reduceImage

def seamCarve(image, newShape):
    '''
        Parameters:
            image:  Input image
            newShape: Tuple with 2 elements containing the shape of the output image

        Returns:
            The seam, energy of output image and the output image
    '''
    shapeX = image.shape[0] - newShape[0] # Change in number of rows/height
    shapeY = image.shape[1] - newShape[1] # Change in number of columns/width

    return seamCarveReduce(image , (np.max([0,shapeX]), np.max([0,shapeY])))

def seamCarveReduce(image, shapeReduction):
    '''
        Parameters:
            image:  Input image
            shapeReduction: Tuple with 2 elements containing the change in shape

        Returns:
            The seam, energy of output image and the output image
    '''
    # If no change in shape return
    if shapeReduction[0] == 0 and shapeReduction[1] == 0:
        return
    T, bitMask = findTranspose.findTranspose(image, shapeReduction) # Find the optimal transformation steps
    return deleteSeam.deleteSeam(bitMask, shapeReduction, image, reduceImage.reduceImageByMask) 
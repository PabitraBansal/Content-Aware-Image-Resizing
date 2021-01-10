import numpy as np

def reduceImageByMask(image, seamMask, isVerticle):
    '''
        Function choose calls the reduce vertiacally / horizontally depending on the isVectricle 
        parameter.
        Parameters:
            image: Image from which seam must be removed.
            seamMask: Seam to be removed as a boolean matrix.
            isVerticle: 1 - If seam to be removed is Verticle
                        0 - If seam to be removed is Horrizontal
        Return:
            Reduced Image
    '''
    if isVerticle == 1:
        imageReduced = reduceImageByMaskVertical(image, seamMask)
    else:
        imageReduced = reduceImageByMaskHorizontal(image, seamMask.T)

    return imageReduced

def reduceImageByMaskVertical(image, seamMask):
    '''
        Function removes the verticle mask
        Parameters:
            image: Image from which seam must be removed.
            seamMask: Seam to be removed as a boolean matrix.
        Return:
            Reduced Image
    '''
    imageReduced = np.zeros((image.shape[0], image.shape[1]-1, image.shape[2]))
    for i in range(seamMask.shape[0]):
        imageReduced[i, :, 0] = image[i, seamMask[i, :], 0]
        imageReduced[i, :, 1] = image[i, seamMask[i, :], 1]
        imageReduced[i, :, 2] = image[i, seamMask[i, :], 2]

    return imageReduced

def reduceImageByMaskHorizontal(image, seamMask):
    '''
        Function removes the horizontal mask
        Parameters:
            image: Image from which seam must be removed.
            seamMask: Seam to be removed as a boolean matrix.
        Return:
            Reduced Image
    '''
    imageReduced = np.zeros((image.shape[0]-1, image.shape[1], image.shape[2]))
    for j in range(seamMask.shape[1]):
        imageReduced[:, j, 0] = image[seamMask[:, j], j, 0]
        imageReduced[:, j, 1] = image[seamMask[:, j], j, 1]
        imageReduced[:, j, 2] = image[seamMask[:, j], j, 2]

    return imageReduced
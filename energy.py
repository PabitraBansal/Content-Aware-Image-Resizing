import numpy as np
from scipy.ndimage.filters import convolve

def energyRGB(image):
    '''
        Function calculates the energy of an RGB image
        Parameters:
            image: RGB image
        Returns:
            res: Energy of the image
    '''
    res = energyGrey(image[:,:,0]) + energyGrey(image[:,:,1]) + energyGrey(image[:,:,2])
    return res

def energyGrey(image):
    '''
        Function calculates the energy of an image with single colour channel using 1st derivative 
        gradient filters in both x and y direction.
        Parameters:
            image: Single channel image
        Returns:
            res: Energy of the image
    '''
    gx = np.array([[-1,0,1]]).astype(np.float)              # Gradient filter in x dirrection
    gy = np.array([[-1],[0],[1]]).astype(np.float)          # Gradient filter in y dirrection
    
    # Energy = |derivative in x| + |derivative in y|
    res = np.abs(convolve(image, gx, mode='nearest')) + np.abs(convolve(image, gy, mode='nearest'))
    return res

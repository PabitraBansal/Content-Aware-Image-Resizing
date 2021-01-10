import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import seamCarve

# Load image
image = mpimg.imread('./sea.jpg')
imShape = image.shape

# # Resize the image so that the code runs faster
image = np.array(Image.fromarray(image).resize((imShape[1]//3, imShape[0]//3)))
imShape = image.shape

# Size of the output image after seam carving
newImage, Mask, e = seamCarve.seamCarve(image.astype(np.float), (imShape[0], imShape[1]//2))
ImageMask = np.copy(image)

# Highlighting the seam in the original image
for i in range(Mask.shape[0]):
    for j in range(Mask.shape[1]):
        if Mask[i, j] == 0:
            ImageMask[i,j,0], ImageMask[i,j,1], ImageMask[i,j,2] = 0,0,0

# Ploting the seam, energy of the outout image and the output image
figure, axis = plt.subplots(nrows=1, ncols=3)
axis[0].imshow(ImageMask)
axis[1].imshow(newImage.astype(np.int))
axis[2].imshow(e.astype(np.int), cmap='gray')
plt.show()
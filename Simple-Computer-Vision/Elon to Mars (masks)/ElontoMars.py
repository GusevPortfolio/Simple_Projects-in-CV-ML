import matplotlib.image as mplimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

#Read the photo of Elon
init_photo = "E3.png"
image = cv2.imread(init_photo)

#Change BGR to RGB
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)

#Setup the gap for the treshold
lower = np.array([250,250,250]) 
upper = np.array([255,255,255])

# Define the masked area
mask = cv2.inRange(image_copy, lower, upper)
plt.imshow(mask, cmap='gray')

#Apply the mask
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]

#Read the background image of Mars
background_image = cv2.imread('M1.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

# Crop it to the right size (842x1132)
crop_background = background_image[0:842, 0:1132]

# Mask the cropped background
crop_background[mask == 0] = [0, 0, 0]

# Display the background
plt.imshow(crop_background)

# Add the two images together to create a complete image
complete_image = masked_image + crop_background

# Display the result
plt.imshow(complete_image)
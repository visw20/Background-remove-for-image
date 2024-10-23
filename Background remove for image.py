from rembg import remove
import numpy as np
import cv2

# Load the image
input_path = 'C:/Brackground remove for image/pexels-james-lee-932763-6054896.jpg'
output_path = 'C:\Brackground remove for image\output_image3_no_bg.png'

# Read the image
input_image = cv2.imread(input_path)

# Remove the background
output_image = remove(input_image)

# Save the image with the background removed
cv2.imwrite(output_path, output_image)

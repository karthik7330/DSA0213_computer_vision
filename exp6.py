import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Get image dimensions
(h, w) = img.shape[:2]

# Define translation values
tx = 100   # move right by 100 pixels
ty = 50    # move down by 50 pixels

# Create translation matrix
translation_matrix = np.float32([[1, 0, tx],
                                 [0, 1, ty]])

# Apply translation
moved_image = cv2.warpAffine(img, translation_matrix, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
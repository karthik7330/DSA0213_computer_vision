import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define Laplacian mask with diagonal neighbors
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply Laplacian filter
laplacian = cv2.filter2D(gray, cv2.CV_64F, kernel)

# Convert to absolute values
laplacian = cv2.convertScaleAbs(laplacian)

# Sharpen the image (Original - Laplacian)
sharpened = cv2.subtract(gray, laplacian)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Laplacian (8-neighbour)", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define Laplacian mask with positive center coefficient
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply sharpening filter
sharpened = cv2.filter2D(gray, -1, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image (Positive Center)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
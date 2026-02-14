import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Boost factor
A = 1.5   # A >= 1

# Create High-Boost kernel (4-neighbour)
kernel = np.array([[0, -1, 0],
                   [-1, A + 4, -1],
                   [0, -1, 0]])

# Apply High-Boost filter
high_boost = cv2.filter2D(gray, -1, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("High-Boost Sharpened Image", high_boost)

cv2.waitKey(0)
cv2.destroyAllWindows()
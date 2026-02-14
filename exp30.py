import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Black-Hat transformation
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Black-Hat Transformation", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
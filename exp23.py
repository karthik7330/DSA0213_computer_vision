import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define boundary detection kernel
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

# Apply convolution
boundary = cv2.filter2D(gray, cv2.CV_64F, kernel)

# Convert to absolute values
boundary = cv2.convertScaleAbs(boundary)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Boundary Image", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
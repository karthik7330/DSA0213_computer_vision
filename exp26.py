import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Opening (Erosion followed by Dilation)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Result", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
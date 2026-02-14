import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
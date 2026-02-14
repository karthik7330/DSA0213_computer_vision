import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 1: Blur the image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 2: Create mask (Original - Blurred)
mask = cv2.subtract(gray, blur)

# Step 3: Add mask to original image
sharpened = cv2.add(gray, mask)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Unsharp Mask", mask)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
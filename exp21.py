import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define Sobel gradient masks
Gx_kernel = np.array([[-1, -2, -1],
                      [ 0,  0,  0],
                      [ 1,  2,  1]])

Gy_kernel = np.array([[-1,  0,  1],
                      [-2,  0,  2],
                      [-1,  0,  1]])

# Apply filters
Gx = cv2.filter2D(gray, cv2.CV_64F, Gx_kernel)
Gy = cv2.filter2D(gray, cv2.CV_64F, Gy_kernel)

# Compute gradient magnitude
gradient = cv2.magnitude(Gx, Gy)
gradient = cv2.convertScaleAbs(gradient)

# Sharpen image (Original + Gradient)
sharpened = cv2.add(gray, gradient)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Magnitude", gradient)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
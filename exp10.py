import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path
(h, w) = img.shape[:2]

# Define source points (from original image)
src_points = np.float32([[100, 100],
                          [400, 100],
                          [100, 400],
                          [400, 400]])

# Define destination points
dst_points = np.float32([[80, 150],
                          [420, 120],
                          [120, 450],
                          [450, 430]])

# Compute Homography matrix
H, status = cv2.findHomography(src_points, dst_points)

# Apply homography transformation
homography_image = cv2.warpPerspective(img, H, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
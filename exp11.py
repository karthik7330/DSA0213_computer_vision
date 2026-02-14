import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path
(h, w) = img.shape[:2]

# Define source points (minimum 4)
src_pts = np.float32([[100, 100],
                      [400, 100],
                      [100, 400],
                      [400, 400]])

# Define destination points
dst_pts = np.float32([[80, 150],
                      [420, 120],
                      [120, 450],
                      [450, 430]])

# Compute Homography using Direct Linear Transformation (DLT)
H, status = cv2.findHomography(src_pts, dst_pts, method=0)

# Apply transformation
dlt_transformed = cv2.warpPerspective(img, H, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", dlt_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
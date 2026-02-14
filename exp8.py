import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path
(h, w) = img.shape[:2]

# Define four points in the original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Define four corresponding points in the transformed image
pts2 = np.float32([[10, 100],
                   [280, 50],
                   [100, 320],
                   [300, 300]])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_image = cv2.warpPerspective(img, matrix, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
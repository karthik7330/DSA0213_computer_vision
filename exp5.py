import cv2

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Get image dimensions
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# Rotate image clockwise (45 degrees)
matrix_clockwise = cv2.getRotationMatrix2D(center, -45, 1.0)
clockwise = cv2.warpAffine(img, matrix_clockwise, (w, h))

# Rotate image counter-clockwise (45 degrees)
matrix_counter = cv2.getRotationMatrix2D(center, 45, 1.0)
counter_clockwise = cv2.warpAffine(img, matrix_counter, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator along Y-axis
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y (Horizontal Edges)", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
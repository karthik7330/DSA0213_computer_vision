import cv2

# Read the image
img = cv2.imread("1.jpg")   # Replace with your image path

# Scale image to smaller size
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Scale image to bigger size
bigger = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Smaller Image", smaller)
cv2.imshow("Bigger Image", bigger)

cv2.waitKey(0)
cv2.destroyAllWindows()
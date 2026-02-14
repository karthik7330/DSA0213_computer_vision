import cv2
# Read image
img = cv2.imread("image.jpg")   # Replace with your image path
blur = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("Gaussian Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
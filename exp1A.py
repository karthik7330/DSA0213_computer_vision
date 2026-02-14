import cv2
# Read image
img = cv2.imread("1200685.jpg")   # Replace with your image path
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
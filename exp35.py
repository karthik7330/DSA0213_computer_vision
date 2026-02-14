import cv2

# Read the image
img = cv2.imread("players.png")   # Replace with your image path

# Coordinates for rectangle (adjust as needed)
x, y, w, h = 100, 50, 250, 350

# Draw rectangle
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Extract object using ROI
roi = img[y:y+h, x:x+w]

# Display images
cv2.imshow("Image with Rectangle", img)
cv2.imshow("Extracted Object", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
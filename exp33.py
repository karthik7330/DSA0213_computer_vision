import cv2

# Load Haar cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
img = cv2.imread("face.jpg")   # Replace with your image path

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display result
cv2.imshow("Face Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Print result
print("Number of faces detected:", len(faces))
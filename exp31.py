import cv2
import numpy as np

# Read template (watch) image
template = cv2.imread("watch.jpg")   # Template image of watch

# Read test image
test_img = cv2.imread("test.jpg")    # Image containing watch

# Convert to grayscale
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
gray_test = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# Initialize ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(gray_template, None)
kp2, des2 = orb.detectAndCompute(gray_test, None)

# Create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw first 20 matches
result = cv2.drawMatches(template, kp1, test_img, kp2, matches[:20], None, flags=2)

# Display result
cv2.imshow("Watch Recognition", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Recognition condition
if len(matches) > 15:
    print("Watch Detected Successfully!")
else:
    print("Watch Not Detected!")
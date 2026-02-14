import cv2
import numpy as np

# Read the video
cap = cv2.VideoCapture("video.mp4")  # Replace with your video file

# Read first frame to get frame size
ret, frame = cap.read()
(h, w) = frame.shape[:2]

# Define four points from the original frame
pts1 = np.float32([[100, 100],
                   [400, 100],
                   [100, 400],
                   [400, 400]])

# Define destination points
pts2 = np.float32([[50, 150],
                   [450, 100],
                   [100, 450],
                   [400, 450]])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transformation
    transformed_frame = cv2.warpPerspective(frame, matrix, (w, h))

    # Display video
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")   # Replace with your video file

frames = []

# Read all frames and store them
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play video in reverse
for frame in reversed(frames):
    cv2.imshow("Reverse Video Playback", frame)
    
    # Adjust delay for speed control
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
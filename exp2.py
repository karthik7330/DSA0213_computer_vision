import cv2

# Read captured video file
cap = cv2.VideoCapture("input.mp4")  # Replace with your video file name

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    # Change delay value to control speed
    # 100 -> Slow motion
    # 25  -> Normal speed
    # 5   -> Fast motion
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
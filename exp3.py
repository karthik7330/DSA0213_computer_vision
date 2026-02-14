import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam Video", frame)

    # Change delay to control speed
    # 100 -> Slow motion
    # 25  -> Normal speed
    # 5   -> Fast motion
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
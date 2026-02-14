import cv2

# Read the image
img = cv2.imread("image.jpg")   # Replace with your image path

# Define watermark text
text = "© My Watermark"

# Set position (bottom-right corner)
position = (50, 450)

# Add watermark
cv2.putText(img, text, position,
            cv2.FONT_HERSHEY_SIMPLEX,
            1,              # Font size
            (255, 255, 255), # White color
            2,              # Thickness
            cv2.LINE_AA)

# Display result
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
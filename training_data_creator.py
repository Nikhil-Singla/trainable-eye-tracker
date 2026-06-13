import cv2

# Initialize the default Mac camera (0 is usually the built-in FaceTime HD camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'q' to close the camera window.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab a frame.")
        break

    # Display the resulting video frame
    cv2.imshow('Mac Camera Feed', frame)

    # Stop the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera hardware resource and destroy all active windows
cap.release()
cv2.destroyAllWindows()

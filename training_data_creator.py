import cv2
import pyautogui

# Get current coordinates

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

    # Read a single keypress per loop iteration
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    if key == ord('s'):
        # Save the current frame as an image file
        x, y = pyautogui.position()
        print(f"X: {x}, Y: {y}")
        filename = f'captured_frame-{x}-{y}.jpg'

        cv2.imwrite(filename, frame)
        print(f"Frame captured and saved as '{filename}'.")

# Release the camera hardware resource and destroy all active windows
cap.release()
cv2.destroyAllWindows()

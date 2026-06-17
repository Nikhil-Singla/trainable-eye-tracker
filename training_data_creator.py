import cv2
import pyautogui
import random

# Get current coordinates
# Initialize the default camera (0 is usually the built-in FaceTime HD camera for Mac)
available = False

for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        available = True
        break
    
if not available:
    raise ValueError("Error: Could not open the camera.")

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
        # Quit app
        break

    if key == ord('c'):
        # Save the current frame as an image file
        x, y = pyautogui.position()
        
        seed = random.randint(10**9)

        print(f"X: {x}, Y: {y}")
        filename = f'{seed}-{x}-{y}.jpg'

        cv2.imwrite(filename, frame)
        print(f"Frame captured and saved as '{filename}'.")

    if key == ord('b'):
        # Save samples when not looking at the screen.
        seed = random.randint(10**9)
        filename = f'{seed}-OUTSIDE.jpg'

        cv2.imwrite(filename, frame)
        print(f"Frame captured and saved as '{filename}'.")

# Release the camera hardware resource and destroy all active windows
cap.release()
cv2.destroyAllWindows()

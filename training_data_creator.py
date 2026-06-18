import cv2
import pyautogui
import random
import glob
import os
import mediapipe as mp

# TODO: Implement Path functionality to save images in separate folder.
# If implemented, must add testcase to ensure no other images are selected/deleted.
from pathlib import Path 

# Initialize the default camera (0 is usually the built-in FaceTime HD camera for Mac)
available = False

for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        available = True
        break
    
if not available:
    raise ValueError("Error: Could not open the camera.")

# Settings to use SSD MobileNetV2 model from OpenCV. The SSD MobileNetV2 model uses a MobileNetV2 backbone with a 256x256 input size 
cap.set(3, 256)    # width
cap.set(4, 256)    # height
cap.set(10, 100)   # brightness

print("Press 'q' to close the camera window.")

def saveFrame(input_frame, x=None, y=None):
    seed = random.randint(0, 10**9)
    if not y:
        filename = f'{seed}--OUTSIDE.jpg'
    else:
        print(f"X: {x}, Y: {y}")
        filename = f'{seed}--{x}--{y}.jpg'

    cv2.imwrite(filename, input_frame)
    print(f'Frame captured and saved as "{filename}".')

def getImages():
    current_working_directory = Path(__file__).parent.resolve()
    extension = '*.jpg'

    filepath = current_working_directory.joinpath(extension)
    # print(filepath)

    files = glob.glob(str(filepath))
    return files

def deleteImages():
    # Remove all the saved images.
    files = getImages()
    for f in files:
        os.remove(f)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab a frame.")
        break

    # Display the resulting video frame
    cv2.imshow('Camera Feed', frame)

    # Read a single keypress per loop iteration
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        # Quit app
        break

    if key == ord('c'):
        # Get current coordinates
        x, y = pyautogui.position()
        saveFrame(frame, x, y)

    if key == ord('b'):
        # Save samples when not looking at the screen.
        saveFrame(frame)

# Release the camera hardware resource and destroy all active windows
cap.release()
cv2.destroyAllWindows()

deleteImages()
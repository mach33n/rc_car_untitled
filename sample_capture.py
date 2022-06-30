import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot openCamera")
    exit()

# Loop camera feed processing
while True:
    # Capture frame
    ret, frame = cap.read()

    # Check if ret value is false and handle processing issue
    if not ret:
        print("Can't recieve frame (stream end?). Exiting...")
        break

    # Operate on frame
    pic = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    
    # Display frame
    cv.imshow('frame', pic)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

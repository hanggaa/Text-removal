import cv2 as cv
import numpy as np

cap = cv.VideoCapture('WM.mp4')
n = 0

# Get the video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

# Define the codec using VideoWriter_fourcc and create a VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
out = cv.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if the frame is not okay

    mask = cv.imread('saved.jpg', 0)
    framee = cv.inpaint(frame, mask, 3, cv.INPAINT_TELEA)

    # Write the frame into the file 'output.mp4'
    out.write(framee)

    n += 1
    if n == 1000:
        break
    else:
        cv.imshow('frames', framee)
        if cv.waitKey(1) == 27:
            break

cap.release()
out.release()  # Release the VideoWriter
cv.destroyAllWindows()
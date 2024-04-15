import cv2 as cv
import numpy as np

cap=cv.VideoCapture('WM.mp4')
n=0

while(1):
    ret, frame = cap.read()
    mask=cv.imread('saved.jpg', 0)

    framee = cv.inpaint(frame, mask, 3, cv.INPAINT_TELEA)

    n+=1
    if n==1000:
        break
    else:
        cv.imshow('frames', framee)
        if cv.waitKey(1)==27:
            break


cap.release()
cv.destroyAllWindows()
import cv2 as cv

cap=cv.VideoCapture('WM.mp4')
n=0

while(1):
    ret, frame = cap.read()
    n+=1

    if n==150:
        cv.imwrite('frame saved.jpg', frame)
        break

cap.release()
cv.destroyAllWindows()
import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('WM.mp4')

# Get the video's width, height, and frames per second (fps)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Define the text region
        # You'll need to adjust these values based on where the text is in your video
        x, y, w, h = 50, 50, 100, 100  # top-left corner (x, y) and width and height of the rectangle
        sub_img = frame[y:y+h, x:x+w]
        white_rect = np.ones(sub_img.shape, dtype=np.uint8) * 255

        # Perform the masking operation
        res = cv2.addWeighted(sub_img, 0.7, white_rect, 0.3, 1.0)

        # Replace the region with the result
        frame[y:y+h, x:x+w] = res

        # Write the frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
cap.release()
out.release()
cv2.destroyAllWindows()

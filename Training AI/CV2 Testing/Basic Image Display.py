import cv2

vid = cv2.VideoCapture(0)    # Capturing the video
vid.set(3,200)    # setting the frame height and width to 200x200
vid.set(4,200)

while True:
    # inside infinity loop
    rect, frame = vid.read()    # Getting the frame and capturing it in 'frame'
    cv2.imshow('frame', frame)    # Showing the frame using 'cv2.imshow'

    if cv2.waitKey(1) & 0xFF == ord('q'):    # If q is pressed, close
        break

vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
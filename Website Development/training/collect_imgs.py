import os
import cv2

DATA_DIR = './training data'    # Directory for storage of the training data

number_of_classes = 26  # Number of different classes (letters)
dataset_size = 100  # Number of entrances for each

cap = cv2.VideoCapture(0)   # Capturing the default camera

for j in range(number_of_classes):

    if not os.path.exists(os.path.join(DATA_DIR, str(j))):  # If the path doesn't exist create it
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))
    done = False

    while True: # Loop to keep the camera open until the letter 'Q' is pressed
        ret, frame = cap.read()

        # Putting the text on screen 'Press "Q"'
        cv2.putText(frame, 'Press "Q"', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:   # Capturing the amount of frames as specified in 'dataset_size'
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)    # Saving the frame as a .jpg with the name being which frame it is
        
        counter += 1

cap.release()
cv2.destroyAllWindows()

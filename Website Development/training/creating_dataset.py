import os
import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

# objects for detecting and drawing landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

DATA_DIR = './training data'

data = []
labels = []

for dir_ in os.listdir(DATA_DIR):   # every directory in training data folder
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:   # every frame within the directory
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the image for mediapipe and matplotlib

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: # for every result
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x    # Storing x and y co ordinates
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)  # Appending x and y co ordinates
                    data_aux.append(y)
    
            data.append(data_aux)
            labels.append(dir_)

f = open('data.pickle', 'wb')   # writing the data as bytes
pickle.dump({'data': data, 'labels': labels}, f)
f.close()

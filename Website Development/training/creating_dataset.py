import os
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

# objects for detecting and drawing landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

DATA_DIR = './training data'

for dir_ in os.listdir(DATA_DIR):   # every directory in training data folder
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:   # every frame within the directory
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting the image for mediapipe and matplotlib

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks: # for every result
                mp_drawing.draw_landmarks(
                    img_rgb,    # image being drawn
                    hand_landmarks, # the model being output
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        plt.figure()
        plt.imshow(img_rgb)

plt.show()

import cv2
import mediapipe as mp
import pickle
import numpy as np

# loading the model
model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

# objects for detecting and drawing landmarks
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Function to be sent to app.py
def video_stream():
    cap = cv2.VideoCapture(0)  # Capture video feed moved to inside the function

    labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 
                   10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 
                   19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

    while True:
        ret, frame = cap.read()

        H, W, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame for mediapipe

        results = hands.process(frame_rgb)
        data_aux = []
        x_ = []
        y_ = []

        if results.multi_hand_landmarks:
            # Processing and extracting landmarks for both hands
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)
                    x_.append(x)
                    y_.append(y)

            # If one hand is detected 'C' is predicted
            if len(data_aux) == 42:
                predicted_character = 'C'

                x1 = int(x_[0] * W)
                y1 = int(y_[0] * H)
                cv2.putText(frame, predicted_character, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2, cv2.LINE_AA)

            elif len(data_aux) == 84: # When Two hands being detected

                x1 = int(min(x_) * W)
                y1 = int(min(y_) * H)

                x2 = int(max(x_) * W)
                y2 = int(max(y_) * H)

                # Predicting the letter
                prediction = model.predict([np.asarray(data_aux)])
                predicted_character = labels_dict[int(prediction[0])]

                # Drawing rectangle and rediction on webcam footage
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)
                cv2.putText(frame, predicted_character, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 2, cv2.LINE_AA)

        # Convert frame to JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')  

    cap.release()

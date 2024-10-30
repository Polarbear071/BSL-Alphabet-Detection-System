from cvzone.HandTrackingModule import HandDetector
import cv2

capture = cv2.VideoCapture(0) # Capturing the camera 0 = built-in camera
detector = HandDetector(staticMode = False, maxHands = 2, modelComplexity = 1, detectionCon = 0.5, minTrackCon = 0.5)

while True:
    success, img = capture.read() # Capturing each webcam frame
    hands, img = detector.findHands(img, draw = True, flipType = True) # Finds the hands, draws landmarks and outlines, flips the image for easier detections

    if hands:
        hand_1 = hands[0] # The first detected hand
        landmark_list_1 = hand_1['lmList'] # Lists the landmarks on the hand
        bounding_box_1 = hand_1['bbox'] # Creates the box boudary
        centre_1 = hand_1['center'] # Stores the centre co-ordinates
        hand_type_1 = hand_1['type'] # Stores which hand it is

        fingers_1 = detector.fingersUp(hand_1) # Counting the number of fingers up for the first hand
        print(f'Hand 1 = {fingers_1.count(1)}', end = ' \n') # Outputting the number of fingers that are currently up

        # Calculating distance between landmarks and drawing them in pink
        length, info, img, = detector.findDistance(landmark_list_1[8][0:2], landmark_list_1[12][0:2], img, color = (255, 0, 255), scale = 10)

        if len(hands) == 2:
            hand_2 = hands[1]   # Lines 24 - 31 are the same but for the second hand
            landmark_list_2 = hand_2['lmList']
            bounding_box_2 = hand_2['bbox']
            centre_2 = hand_2['center']
            hand_type_2 = hand_2['type']
            
            fingers_2 = detector.fingersUp(hand_2)
            print(f'Hand 2 = {fingers_2.count(1)}', end = ' \n')

            # Calculate the distance between the index fingers of the hands and drawing it in red
            length, info, img = detector.findDistance(landmark_list_1[8][0:2], landmark_list_2[8][0:2], img, color = (255, 0, 0), scale = 10)
    
        print() # Makes the terminal more legible
    cv2.imshow('Image', img)
    cv2.waitKey(1) # Keep the window open and update each frame (checking every 1 millisecond between each frame)
# import HandTrackingModule as htm
# import cv2
# import os
#
# # Set the dimensions for the camera
# wCam, hCam = 640, 480
#
# # Start capturing video from the camera
# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)  # Width
# cap.set(4, hCam)  # Height
#
# # Load images of fingers from the specified folder
# folderPath = 'fingers'
# mylist = os.listdir(folderPath)
# overlayList = [cv2.imread(f'{folderPath}/{i}') for i in mylist]
#
# # Initialize hand detector with confidence threshold
# detector = htm.handDetector(detectionCon=0.75)
# tipIds = [4, 8, 12, 16, 20]  # Indices for the fingertips of the thumb, index, middle, ring, and pinky
#
# while True:
#     success, img = cap.read()  # Read frames from the webcam
#     img = detector.findHands(img)  # Detect hands
#     lmList = detector.findPosition(img, draw=False)  # Get landmark positions
#
#     if len(lmList) != 0:  # Ensure landmarks are detected
#         fingers = []
#
#         # Hand type detection based on landmark 17 (pinky base) and 5 (index base)
#         hand_type = "Right" if lmList[17][1] < lmList[5][1] else "Left"
#
#         # Thumb detection
#         if hand_type == "Right":
#             thumb_open = lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]  # Thumb tip to base comparison
#         else:  # Left hand
#             thumb_open = lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]
#
#         fingers.append(1 if thumb_open else 0)  # Append thumb status (1 for open, 0 for closed)
#
#         # Other four fingers: check if the tip is higher (y-axis) than the joint
#         for id in range(1, 5):
#             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:  # Fingertip is above joint
#                 fingers.append(1)  # Finger is open
#             else:
#                 fingers.append(0)  # Finger is closed
#
#         totalFingers = fingers.count(1)  # Count how many fingers are up
#         print(f"Hand: {hand_type}, Fingers up: {totalFingers}")
#
#         # Display the corresponding finger image
#         if totalFingers > 0 and totalFingers <= len(overlayList):
#             h, w, c = overlayList[totalFingers - 1].shape
#             img[0:h, 0:w] = overlayList[totalFingers - 1]
#
#         # Draw a rectangle with the total number of fingers
#         cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
#         cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
#
#     # Show the result image
#     cv2.imshow('Hand Detection', img)
#     cv2.waitKey(1)  # Small delay for smoother video feed
##################################################################################################################

# import HandTrackingModule as htm
# import cv2
# import os
#
# # Set the dimensions for the camera
# wCam, hCam = 640, 480
#
# # Start capturing video from the camera
# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)  # Width
# cap.set(4, hCam)  # Height
#
# # Load images of fingers from the specified folder
# folderPath = 'fingers'
# mylist = os.listdir(folderPath)
# overlayList = [cv2.imread(f'{folderPath}/{i}') for i in mylist]
#
# # Initialize hand detector with confidence threshold
# detector = htm.handDetector(detectionCon=0.75)
# tipIds = [4, 8, 12, 16, 20]  # Indices for the fingertips of the thumb, index, middle, ring, and pinky
#
# while True:
#     success, img = cap.read()  # Read frames from the webcam
#     img = detector.findHands(img)  # Detect hands
#     lmList = detector.findPosition(img, draw=False)  # Get landmark positions
#
#     if len(lmList) != 0:  # Ensure landmarks are detected
#         fingers = []
#
#         # Hand type detection based on landmark 17 (pinky base) and 5 (index base)
#         hand_type = "Right" if lmList[17][1] < lmList[5][1] else "Left"
#
#         # Thumb detection
#         if hand_type == "Right":
#             thumb_open = lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]  # Thumb tip to base comparison
#         else:  # Left hand
#             thumb_open = lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]
#
#         fingers.append(1 if thumb_open else 0)  # Append thumb status (1 for open, 0 for closed)
#
#         # Other four fingers: check if the tip is higher (y-axis) than the joint
#         for id in range(1, 5):
#             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:  # Fingertip is above joint
#                 fingers.append(1)  # Finger is open
#             else:
#                 fingers.append(0)  # Finger is closed
#
#         totalFingers = fingers.count(1)  # Count how many fingers are up
#         print(f"Hand: {hand_type}, Fingers up: {totalFingers}")
#
#         # Display the corresponding finger image
#         if totalFingers > 0 and totalFingers <= len(overlayList):
#             h, w, c = overlayList[totalFingers - 1].shape
#             img[0:h, 0:w] = overlayList[totalFingers - 1]
#
#         # Draw a rectangle with the total number of fingers
#         cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
#         cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)
#
#         # Display the detected hand type on the screen (Right or Left)
#         cv2.putText(img, f"Hand: {hand_type}", (350, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
#
#     # Show the result image
#     cv2.imshow('Hand Detection', img)
#     cv2.waitKey(1)  # Small delay for smoother video feed

#########################################################################################################################################

import HandTrackingModule as htm
import cv2
import os

# Set the dimensions for the camera
camera_width, camera_height = 640, 480

# Start capturing video from the camera
video_capture = cv2.VideoCapture(0)
video_capture.set(3, camera_width)  # Width
video_capture.set(4, camera_height)  # Height

# Load images of fingers from the specified folder
images_folder = 'fingers'
image_files = os.listdir(images_folder)
finger_images = [cv2.imread(f'{images_folder}/{img}') for img in image_files]

# Initialize hand detector with confidence threshold
hand_detector = htm.handDetector(detectionCon=0.75)
finger_tip_ids = [4, 8, 12, 16, 20]  # Indices for the fingertips of the thumb, index, middle, ring, and pinky

while True:
    success, frame = video_capture.read()  # Read frames from the webcam
    frame = hand_detector.findHands(frame)  # Detect hands
    landmarks_list = hand_detector.findPosition(frame, draw=False)  # Get landmark positions

    if len(landmarks_list) != 0:  # Ensure landmarks are detected
        finger_states = []

        # Hand type detection based on landmark 17 (pinky base) and 5 (index base)
        detected_hand_type = "Right" if landmarks_list[17][1] < landmarks_list[5][1] else "Left"

        # Thumb detection
        if detected_hand_type == "Right":
            thumb_status = landmarks_list[finger_tip_ids[0]][1] > landmarks_list[finger_tip_ids[0] - 1][1]  # Thumb tip to base comparison
        else:  # Left hand
            thumb_status = landmarks_list[finger_tip_ids[0]][1] < landmarks_list[finger_tip_ids[0] - 1][1]

        finger_states.append(1 if thumb_status else 0)  # Append thumb status (1 for open, 0 for closed)

        # Other four fingers: check if the tip is higher (y-axis) than the joint
        for index in range(1, 5):
            if landmarks_list[finger_tip_ids[index]][2] < landmarks_list[finger_tip_ids[index] - 2][2]:  # Fingertip is above joint
                finger_states.append(1)  # Finger is open
            else:
                finger_states.append(0)  # Finger is closed

        total_fingers_up = finger_states.count(1)  # Count how many fingers are up
        print(f"Hand: {detected_hand_type}, Fingers up: {total_fingers_up}")

        # Display the corresponding finger image
        if total_fingers_up > 0 and total_fingers_up <= len(finger_images):
            height, width, channels = finger_images[total_fingers_up - 1].shape
            frame[0:height, 0:width] = finger_images[total_fingers_up - 1]

        # Draw a rectangle with the total number of fingers
        cv2.rectangle(frame, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(frame, str(total_fingers_up), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

        # Display the detected hand type on the screen (Right or Left)
        cv2.putText(frame, f"Hand: {detected_hand_type}", (300, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    # Show the result image
    cv2.imshow('Hand Detection', frame)
    cv2.waitKey(1)  # Small delay for smoother video feed

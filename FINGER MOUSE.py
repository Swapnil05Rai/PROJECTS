import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drwing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
ind_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drwing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y),
                               radius=15, color=(0, 255, 255))
                    ind_x = screen_width/frame_width*x
                    ind_y = screen_height/frame_height*y
                    pyautogui.moveTo(ind_x, ind_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y),
                               radius=15, color=(0, 255, 255))
                    thu_x = screen_width/frame_width*x
                    thu_y = screen_height/frame_height*y
                    if abs(ind_y-thu_y) < 45:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow("FINGERMOUSE", frame)
    cv2.waitKey(1)

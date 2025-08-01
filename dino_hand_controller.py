import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)
                                
def is_fist(hand_landmarks):
    # Check if finger tips are below pip joints (y increases downward)
    tips_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]
    for tip, pip in zip(tips_ids, pip_ids):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            return False  # Finger is extended
    return True  # All fingers are curled → fist

prev_state = "open"

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_fist(hand_landmarks):
                if prev_state != "fist":
                    pyautogui.press('space')  # Trigger jump
                    print("✊ Fist detected – Jump!")
                    prev_state = "fist"
            else:
                prev_state = "open"

    cv2.imshow("Dino Hand Controller", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()

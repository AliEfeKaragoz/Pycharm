import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import keyboard as kb

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

hand_detector = HandDetector(maxHands=2,detectionCon=0.4,minTrackCon=0.4)

def ControlSteering(img,hand1,hand2,draw=True):
    center_point1 = hand1["center"]
    center_point2 = hand2["center"]
    dx = center_point2[0] - center_point1[0]
    dy = center_point2[1] - center_point1[1]
    degree = np.degrees(np.arctan2(dy,dx))
    degree = degree * -1
    if degree > 90:
        degree -= 180
    elif degree < -90:
        degree += 180
    if 15 < degree <= 60:
        kb.press("d")
        kb.release("a")
    elif -15 > degree >= -60:
        kb.press("a")
        kb.release("d")
    else:
        kb.release("d")
        kb.release("a")
    if draw:
        cv2.line(img,center_point1,center_point2,(0,255,0),3)
        cv2.putText(img,f"Steering Degree: {int(degree)}",(25,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    else: print(f"Steering Degree: {degree}")

def ControlPedals(img,hand1,hand2,draw=True):
    x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
    y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    A,B,C = np.polyfit(x, y, 2) # y = Ax^2 + Bx + C
    h1_x1,h1_y1 = hand1["lmList"][5][:2]
    h1_x2,h1_y2 = hand1["lmList"][17][:2]
    h2_x1,h2_y1 = hand2["lmList"][5][:2]
    h2_x2,h2_y2 = hand2["lmList"][17][:2]
    hand1_distance = math.sqrt((h1_y2 - h1_y1) ** 2 + (h1_x2 - h1_x1) ** 2)
    hand2_distance = math.sqrt((h2_y2 - h2_y1) ** 2 + (h2_x2 - h2_x1) ** 2)
    hand1_distance_cm = A * hand1_distance ** 2 + B * hand1_distance + C
    hand2_distance_cm = A * hand2_distance ** 2 + B * hand2_distance + C
    average_distance_cm = (hand1_distance_cm + hand2_distance_cm) / 2
    if 20 < average_distance_cm < 50:
        kb.press("w")
        kb.release("s")
    elif 70 < average_distance_cm < 100:
        kb.press("s")
        kb.release("w")
    else:
        kb.release("w")
        kb.release("s")
    if draw:
        bbox1 = hand1["bbox"]
        bbox2 = hand2["bbox"]
        cv2.rectangle(img,(bbox1[0],bbox1[1]),(bbox1[0] + bbox1[2],bbox1[1] + bbox1[3]),(0,255,0),3)
        cv2.rectangle(img,(bbox2[0],bbox2[1]),(bbox2[0] + bbox2[2],bbox2[1] + bbox2[3]),(0,255,0),3)
        cv2.putText(img,f"Average Distance: {int(average_distance_cm)} cm",(25,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    else: print(f"Average Distance: {average_distance_cm} cm")

while True:
    success,Original_img = cap.read()
    Original_img = cv2.resize(Original_img,(width_c,height_c))
    if not success:
        break
    else:
        hands,Original_img = hand_detector.findHands(Original_img,draw=False)
        if hands:
            if len(hands) == 2:
                hand1 = hands[0]
                hand2 = hands[1]
                ControlSteering(Original_img,hand1,hand2,True)
                ControlPedals(Original_img,hand1,hand2,True)
        cv2.imshow("Original Img",Original_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

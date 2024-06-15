import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

hand_detector = HandDetector(maxHands=2,detectionCon=0.8)

def MeasureDistance(img,hand,draw=True):
    # x is the raw distance, y is the value in cm
    x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
    y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C
    x1,y1 = hand["lmList"][5][:2]
    x2,y2 = hand["lmList"][17][:2]
    distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
    A,B,C = coff
    distance_cm = A * distance ** 2 + B * distance + C
    if draw:
        (x,y,w,h) = hand["bbox"]
        cv2.rectangle(img,(x,y),(x + w,y + h),(0,255,0),3)
        cvzone.putTextRect(img,f"{int(distance_cm)} cm",(x + 5,y - 10),colorR=(0,255,0))
    else: print(f"Distance: {(distance_cm)} cm")

while True:
    success,Original_img = cap.read()
    Original_img = cv2.resize(Original_img,(width_c,height_c))
    if not success:
        break
    else:
        hands,Original_img = hand_detector.findHands(Original_img,draw=False)
        if hands:
            hand = hands[0]
            MeasureDistance(Original_img,hand)
            if len(hands) == 2:
                hand2 = hands[1]
                MeasureDistance(Original_img,hand2)
        cv2.imshow("Original Img",Original_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

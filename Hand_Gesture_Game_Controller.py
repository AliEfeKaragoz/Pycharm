import cv2
import keyboard as kb
from cvzone import HandTrackingModule

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

hand_detector = HandTrackingModule.HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success,Original_img = cap.read()
    Original_img = cv2.resize(Original_img,(width_c,height_c))
    if not success:
        break
    else:
        hands,Original_img= hand_detector.findHands(Original_img,draw=True)
        if hands:
            hand = hands[0]
            """
            lm_list = hand["lmList"] # list of 21 landmarks points
            bbox = hand["bbox"] # bounding box info x,y,w,h
            center_point = hand["center"] # center of the hand cx,cy
            hand_type = hand["type"] # hand type left or right
            """
            fingers = hand_detector.fingersUp(hand)
            print(fingers)
            if fingers == [0,1,0,0,0]:
                kb.press("w")
                kb.release("a")
                kb.release("d")
                kb.release("s")
                kb.release("space")
            elif fingers == [0,1,1,0,0]:
                kb.press("a")
                kb.release("w")
                kb.release("d")
                kb.release("s")
                kb.release("space")
            elif fingers == [0,1,1,1,0]:
                kb.press("d")
                kb.release("w")
                kb.release("a")
                kb.release("s")
                kb.release("space")
            elif fingers == [0,1,1,1,1]:
                kb.press("s")
                kb.release("a")
                kb.release("w")
                kb.release("d")
                kb.release("space")
            elif fingers == [1,1,1,1,1]:
                kb.press("space")
                kb.release("a")
                kb.release("w")
                kb.release("d")
                kb.release("s")
            elif fingers == [0,0,0,0,0]:
                kb.release("a")
                kb.release("w")
                kb.release("d")
                kb.release("s")
                kb.release("space")
            elif fingers == [1,1,1,0,1]:
                kb.release("a")
                kb.release("w")
                kb.release("d")
                kb.release("s")
                kb.release("space")
                break
            else:
                continue
            cv2.putText(Original_img,f"Fingers: {fingers}",(25,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow("Original Img",Original_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

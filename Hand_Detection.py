import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

width_c = 700
height_c = 500

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

def FindLandmarks(mark):
    x = int(hand_landmark.landmark[mark].x * width_s)
    y = int(hand_landmark.landmark[mark].y * height_s)
    return x,y

def Palm(img,color):
    pts = np.array([[x0,y0],[x5,y5],[x9,y9],[x13,y13],[x17,y17]],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.fillPoly(img,[pts],color)
    cv2.polylines(img,[pts],True,color,5)

def Fingers(img,marks,color):
    pts = np.array(marks,np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],False,color,5)

def Landmarks(img,radius,color):
    cv2.circle(img,(x0,y0),radius,color,-1)
    cv2.circle(img,(x1,y1),radius,color,-1)
    cv2.circle(img,(x2,y2),radius,color,-1)
    cv2.circle(img,(x3,y3),radius,color,-1)
    cv2.circle(img,(x4,y4),radius,color,-1)
    cv2.circle(img,(x5,y5),radius,color,-1)
    cv2.circle(img,(x6,y6),radius,color,-1)
    cv2.circle(img,(x7,y7),radius,color,-1)
    cv2.circle(img,(x8,y8),radius,color,-1)
    cv2.circle(img,(x9,y9),radius,color,-1)
    cv2.circle(img,(x10,y10),radius,color,-1)
    cv2.circle(img,(x11,y11),radius,color,-1)
    cv2.circle(img,(x12,y12),radius,color,-1)
    cv2.circle(img,(x13,y13),radius,color,-1)
    cv2.circle(img,(x13,y13),radius,color,-1)
    cv2.circle(img,(x14,y14),radius,color,-1)
    cv2.circle(img,(x15,y15),radius,color,-1)
    cv2.circle(img,(x16,y16),radius,color,-1)
    cv2.circle(img,(x17,y17),radius,color,-1)
    cv2.circle(img,(x18,y18),radius,color,-1)
    cv2.circle(img,(x19,y19),radius,color,-1)
    cv2.circle(img,(x20,y20),radius,color,-1)

with mp_hands.Hands(static_image_mode=False) as hands:
    while True:
        success,Original_frame = cap.read()
        Original_frame = cv2.resize(Original_frame,(width_c,height_c))
        height_s,width_s,channel_s = Original_frame.shape
        Black_board = np.zeros_like(Original_frame)
        if not success:
            break
        else:
            Blurred_frame = cv2.blur(Original_frame,(5,5))
            HSV_frame = cv2.cvtColor(Blurred_frame,cv2.COLOR_BGR2HSV)
            RGB_frame = cv2.cvtColor(Original_frame,cv2.COLOR_BGR2RGB)

            hands_process = hands.process(RGB_frame)
            if hands_process.multi_hand_landmarks:
                for hand_landmark in hands_process.multi_hand_landmarks:
                    x0,y0 = FindLandmarks(0)
                    x1,y1 = FindLandmarks(1)
                    x2,y2 = FindLandmarks(2)
                    x3,y3 = FindLandmarks(3)
                    x4,y4 = FindLandmarks(4)
                    x5,y5 = FindLandmarks(5)
                    x6,y6 = FindLandmarks(6)
                    x7,y7 = FindLandmarks(7)
                    x8,y8 = FindLandmarks(8)
                    x9,y9 = FindLandmarks(9)
                    x10,y10 = FindLandmarks(10)
                    x11,y11 = FindLandmarks(11)
                    x12,y12 = FindLandmarks(12)
                    x13,y13 = FindLandmarks(13)
                    x14,y14 = FindLandmarks(14)
                    x15,y15 = FindLandmarks(15)
                    x16,y16 = FindLandmarks(16)
                    x17,y17 = FindLandmarks(17)
                    x18,y18 = FindLandmarks(18)
                    x19,y19 = FindLandmarks(19)
                    x20,y20 = FindLandmarks(20)

                    Palm(Black_board,(255,255,255))
                    Fingers(Black_board,[[x0,y0],[x1,y1],[x2,y2],[x3,y3],[x4,y4]],(255,255,255))
                    Fingers(Black_board,[[x5,y5],[x6,y6],[x7,y7],[x8,y8]],(255,255,255))
                    Fingers(Black_board,[[x9,y9],[x10,y10],[x11,y11],[x12,y12]],(255,255,255))
                    Fingers(Black_board,[[x13,y13],[x14,y14],[x15,y15],[x16,y16]],(255,255,255))
                    Fingers(Black_board,[[x17,y17],[x18,y18],[x19,y19],[x20,y20]],(255,255,255))
                    Landmarks(Black_board,7,(0,0,255))

            cv2.imshow("Original Frame",Original_frame)
            cv2.imshow("Black Board",Black_board)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()

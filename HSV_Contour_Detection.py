import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,800)
cap.set(4,600)

while True:
    success,Original_frame = cap.read()
    Original_frame = cv2.resize(Original_frame,(800,600))
    if not success:
        break
    else:
        Blurred_frame = cv2.GaussianBlur(Original_frame,(5,5),0)
        HSV_frame = cv2.cvtColor(Blurred_frame,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])

        Mask = cv2.inRange(HSV_frame, lower_blue, upper_blue)

        kernel_ero = np.ones((10, 10), np.uint8)
        kernel_dil = np.ones((10, 10), np.uint8)

        erosion = cv2.erode(Mask, kernel_ero)
        dilation = cv2.dilate(erosion, kernel_dil)

        contours, _ = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(Original_frame,contours,-1,(0,0,255),2)

        cv2.imshow("HSV Contour",Original_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,600)
cap.set(4,450)

while True:
    success,Original_frame = cap.read()
    Original_frame = np.flip(Original_frame,1)
    Original_frame = cv2.resize(Original_frame,(600,450))
    if success:
        Blurred_frame = cv2.GaussianBlur(Original_frame,ksize=(5,5),sigmaX=0)
        HSV_frame = cv2.cvtColor(Blurred_frame,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100, 50, 50])
        upper_blue = np.array([130, 255, 255])

        Mask = cv2.inRange(HSV_frame,lower_blue,upper_blue)

        kernel_ero = np.ones((10, 10), np.uint8)
        kernel_dil = np.ones((10, 10), np.uint8)

        erosion = cv2.erode(Mask,kernel_ero)
        dilation = cv2.dilate(erosion,kernel_dil)

        Result = cv2.bitwise_and(Original_frame,Original_frame,mask=dilation)

        Combine = cv2.addWeighted(Original_frame,1,Result,1.25,0)

        cv2.imshow("Result",Result)
        cv2.imshow("Combine",Combine)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

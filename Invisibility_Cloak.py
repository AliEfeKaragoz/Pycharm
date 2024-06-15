import cv2
import numpy as np
import time

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

time.sleep(3)
for i in range(60):
    success,Img_BG = cap.read()
    Img_BG = cv2.resize(Img_BG,(width_c,height_c))
    if not success:
        break

while True:
    success,Original_img = cap.read()
    Original_img = cv2.resize(Original_img,(width_c,height_c))
    if not success:
        break
    else:
        HSV_img = cv2.cvtColor(Original_img,cv2.COLOR_BGR2HSV)
        Blurred_img = cv2.GaussianBlur(HSV_img,(35,35),0)

        lower_blue = np.array([84,98,0])
        upper_blue = np.array([179,255,255])
        Mask = cv2.inRange(HSV_img,lower_blue,upper_blue)

        Mask = cv2.erode(Mask,None,iterations=2)
        Mask = cv2.dilate(Mask,None,iterations=2)

        Original_img[np.where(Mask==255)] = Img_BG[np.where(Mask==255)]
        cv2.imshow("Original Img",Original_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

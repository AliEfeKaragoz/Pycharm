import cv2
resim = cv2.imread("orman.jpg")
resim_2 = cv2.cvtColor(resim,cv2.COLOR_BGR2HLS)
resim_3 = cv2.cvtColor(resim,cv2.COLOR_BGR2Lab)
resim_4 = cv2.cvtColor(resim,cv2.COLOR_RGB2HSV)

cv2.imshow("resim",resim)
cv2.imshow("resim_2",resim_2)
cv2.imshow("resim_3",resim_3)
cv2.imshow("resim_4",resim_4)

cv2.waitKey(0)
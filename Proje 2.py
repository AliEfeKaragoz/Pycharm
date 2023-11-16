import cv2
cam = cv2.VideoCapture(0)

while True:
    control,webcam = cam.read()
    cv2.imshow("KAMERA",webcam)
    if cv2.waitKey(15) == 27:
        break
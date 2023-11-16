import cv2
import mediapipe as mp

face_detection = mp.solutions.face_detection

video = cv2.VideoCapture(0)

with face_detection.FaceDetection(min_detection_confidence=0.5) as Face:
    while True:
        control,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        result = Face.process(rgb)
        if result.detections:
            for detection in result.detections:
                bounding_box = detection.location_data.relative_bounding_box
                x,y = int(bounding_box.xmin * webcam.shape[1]),int(bounding_box.ymin* webcam.shape[0])
                w,h = int(bounding_box.width * webcam.shape[1]),int(bounding_box.height * webcam.shape[0])
                cv2.rectangle(webcam,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("",webcam)
        if cv2.waitKey(15) == 27:
            break
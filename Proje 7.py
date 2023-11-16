import cv2
import mediapipe as mp
face_detection = mp.solutions.face_detection

background = cv2.imread("background.jpg")

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,800)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

with face_detection.FaceDetection(min_detection_confidence=0.5,model_selection=0) as Face:
    while True:
        control,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        results = Face.process(rgb)
        if results.detections:
            for detection in results.detections:
                bounding_box = detection.location_data.relative_bounding_box
                x,y = int(bounding_box.xmin * webcam.shape[1]),int(bounding_box.ymin * webcam.shape[0])
                w,h = int(bounding_box.width * webcam.shape[1]),int(bounding_box.height * webcam.shape[0])
                face = webcam[y:y+h,x:x+w]
                result = background.copy()
                result[y:y+h,x:x+w] = face
        else:
            result = webcam
        cv2.imshow("Camera & Surface",result)
        if cv2.waitKey(15) == 27:
            break
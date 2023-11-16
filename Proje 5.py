import cv2
import mediapipe as mp
face_model = mp.solutions.face_mesh

surface = cv2.imread("surface.jpg")

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,800)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

with face_model.FaceMesh(max_num_faces=4,min_detection_confidence=0.5,min_tracking_confidence=0.5) as Face:
    while True:
        control,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        surface_copy = surface.copy()
        result = Face.process(rgb)
        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                for face_landmark in face_landmarks.landmark:
                    face_model_x,face_model_y = int(face_landmark.x * webcam.shape[1]),int(face_landmark.y * webcam.shape[0])
                    cv2.circle(surface_copy,(face_model_x,face_model_y),1,(0,255,0),-1)
        cv2.imshow("Surface Screen",surface_copy)
        cv2.imshow("Camera Screen",webcam)
        if cv2.waitKey(15) == 27:
            break
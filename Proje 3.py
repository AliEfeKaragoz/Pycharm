import cv2
import mediapipe as mp
mp_yuz_tanima = mp.solutions.face_mesh

video = cv2.VideoCapture(0)

with mp_yuz_tanima.FaceMesh(min_tracking_confidence=0.5,min_detection_confidence=0.5) as yuz:
    while True:
        kontrol,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        sonuc = yuz.process(rgb)
        if sonuc.multi_face_landmarks:
            for landmarks in sonuc.multi_face_landmarks:
                for landmark in landmarks.landmark:
                    x,y = int(landmark.x * webcam.shape[1]),int(landmark.y * webcam.shape[0])
                    cv2.circle(webcam,(x,y),2,(0,0,255),-1)
                    print(f"x:{x} y:{y}")
        cv2.imshow("Yuz Belirleme",webcam)
        if cv2.waitKey(15) == 27:
            print("Program başarıyla kapatıldı.")
            break
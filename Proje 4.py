import cv2
import mediapipe as mp
import random
el_model = mp.solutions.hands

video = cv2.VideoCapture(0)

with el_model.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as el:
    while True:
        kontrol,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        sonuc = el.process(rgb)
        if sonuc.multi_hand_landmarks:
            for hand_landmarks in sonuc.multi_hand_landmarks:
                # Baş parmak

                bas_parmak_bas_x = int(hand_landmarks.landmark[4].x * webcam.shape[1])
                bas_parmak_bas_y = int(hand_landmarks.landmark[4].y * webcam.shape[0])

                # İşaret parmak

                isaret_parmak_bas_x = int(hand_landmarks.landmark[8].x * webcam.shape[1])
                isaret_parmak_bas_y = int(hand_landmarks.landmark[8].y * webcam.shape[0])

                # Orta parmak

                orta_parmak_bas_x = int(hand_landmarks.landmark[12].x * webcam.shape[1])
                orta_parmak_bas_y = int(hand_landmarks.landmark[12].y * webcam.shape[0])

                # Yüzük parmak

                yuzuk_parmak_bas_x = int(hand_landmarks.landmark[16].x * webcam.shape[1])
                yuzuk_parmak_bas_y = int(hand_landmarks.landmark[16].y * webcam.shape[0])

                # Serçe parmak

                serce_parmak_bas_x = int(hand_landmarks.landmark[20].x * webcam.shape[1])
                serce_parmak_bas_y = int(hand_landmarks.landmark[20].y * webcam.shape[0])

                # KORDİNATLAR
                # Baş parmak ihtimalleri

                bas_ve_isaret = cv2.line(webcam,(bas_parmak_bas_x,bas_parmak_bas_y),(isaret_parmak_bas_x,isaret_parmak_bas_y),(255,0,0),4)
                bas_ve_orta = cv2.line(webcam,(bas_parmak_bas_x,bas_parmak_bas_y),(orta_parmak_bas_x,orta_parmak_bas_y),(255,0,0),4)
                bas_ve_yuzuk = cv2.line(webcam,(bas_parmak_bas_x,bas_parmak_bas_y),(yuzuk_parmak_bas_x,yuzuk_parmak_bas_y),(255,0,0),4)
                bas_ve_serce = cv2.line(webcam,(bas_parmak_bas_x,bas_parmak_bas_y),(serce_parmak_bas_x,serce_parmak_bas_y),(255,0,0),4)

                # İşaret parmak ihtimalleri

                isaret_ve_orta = cv2.line(webcam,(isaret_parmak_bas_x,isaret_parmak_bas_y),(orta_parmak_bas_x,orta_parmak_bas_y),(0,255,0),4)
                isaret_ve_yuzuk = cv2.line(webcam,(isaret_parmak_bas_x,isaret_parmak_bas_y),(yuzuk_parmak_bas_x,yuzuk_parmak_bas_y),(0,255,0),4)
                isaret_ve_serce = cv2.line(webcam,(isaret_parmak_bas_x,isaret_parmak_bas_y),(serce_parmak_bas_x,serce_parmak_bas_y),(0,255,0),4)

                # Orta parmak ihtimalleri

                orta_ve_yuzuk = cv2.line(webcam,(orta_parmak_bas_x,orta_parmak_bas_y),(yuzuk_parmak_bas_x,yuzuk_parmak_bas_y),(0,0,255),4)
                orta_ve_serce = cv2.line(webcam,(orta_parmak_bas_x,orta_parmak_bas_y),(serce_parmak_bas_x,serce_parmak_bas_y),(0,0,255),4)

                # Yüzük parmak ihtimalleri

                yuzuk_ve_serce = cv2.line(webcam,(yuzuk_parmak_bas_x,yuzuk_parmak_bas_y),(serce_parmak_bas_x,serce_parmak_bas_y),(0,255,255),4)

        cv2.imshow("Parmak Arasi Mesafe Belirleme",webcam)
        if cv2.waitKey(15) == 27:
            print("Program başarıyla kapatıldı.")
            break
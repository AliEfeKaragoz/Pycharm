import cv2
import mediapipe as mp

hand_model = mp.solutions.hands
hand_draw = mp.solutions.drawing_utils

surface = cv2.imread("img.png")

video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH,800)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,600)

with hand_model.Hands(max_num_hands=8,min_detection_confidence=0.5,min_tracking_confidence=0.5) as Hands:
    while True:
        control,webcam = video.read()
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        surface_copy = surface.copy()
        result = Hands.process(rgb)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for hand_landmark in hand_landmarks.landmark:
                    hand_model_x,hand_model_y = int(hand_landmark.x * webcam.shape[1]),int(hand_landmark.y * webcam.shape[0])
                    cv2.circle(surface_copy,(hand_model_x,hand_model_y),6,(255,255,255),-1)
        cv2.imshow("Surface Screen",surface_copy)
        cv2.imshow("Camera Screen",webcam)
        if cv2.waitKey(15) == 27:
            break
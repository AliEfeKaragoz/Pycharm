import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose.Pose(
    min_tracking_confidence=0.7,
    min_detection_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

while True:
    success,Original_frame = cap.read()
    Original_frame = cv2.resize(Original_frame,(width_c,height_c))
    height_s,width_s,channel_s = Original_frame.shape
    if not success:
        break
    else:
        RGB_frame = cv2.cvtColor(Original_frame,cv2.COLOR_BGR2RGB)
        mp_pose_process = mp_pose.process(RGB_frame)
        if mp_pose_process.pose_landmarks:
            mp_drawing.draw_landmarks(
                image=Original_frame,
                landmark_list=mp_pose_process.pose_landmarks,
                connections=mp.solutions.pose.POSE_CONNECTIONS
            )
        cv2.imshow("Original Frame",Original_frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

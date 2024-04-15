import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=False,
                                               max_num_faces=1,
                                               refine_landmarks=True,
                                               min_detection_confidence=0.7,
                                               min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

(width_c,height_c) = 700,500

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

while True:
    success,Original_frame = cap.read()
    Original_frame = cv2.resize(Original_frame,(width_c,height_c))
    height_s,width_s,channel_s = Original_frame.shape
    Black_board = np.zeros_like(Original_frame)
    if not success:
        break
    else:
        RGB_frame = cv2.cvtColor(Original_frame,cv2.COLOR_BGR2RGB)

        face_mesh_process = mp_face_mesh.process(RGB_frame)
        if face_mesh_process.multi_face_landmarks:
            for face_landmark in face_mesh_process.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=Black_board,
                    landmark_list=face_landmark,
                    connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(200,0,0),thickness=1,circle_radius=1),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(255,0,0),thickness=1,circle_radius=0)
                )
        cv2.imshow("Original Frame",Original_frame)
        cv2.imshow("Black Board",Black_board)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

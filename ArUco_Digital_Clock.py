import cv2
import numpy as np
import datetime
import pytz

marker_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
param_markers = cv2.aruco.DetectorParameters()

timezones = {
    0:"Europe/Istanbul",
    1:"Europe/Berlin",
    2:"Europe/Paris",
    3:"Asia/Tokyo",
    4:"Europe/Moscow",
    5:"Us/Eastern"
}

def GetCurrentTime(timezone):
    tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz).strftime("%H:%M:%S")

def DrawTime(dest_img,corners,timezone=None,here=False):
    center_x = int((corners[0][0][0] + corners[0][2][0]) / 2)
    center_y = int((corners[0][0][1] + corners[0][2][1]) / 2)
    if here == False:
        current_time = GetCurrentTime(timezone)
        current_zone = timezones[ids]
        cv2.putText(dest_img,current_zone,(center_x - 50,center_y - 10),cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,(0,255,0),2)
        cv2.putText(dest_img,current_time,(center_x - 50,center_y + 20),cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,(0,255,0),2)
    else:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        current_zone = "Current Time"
        cv2.putText(dest_img, current_zone, (center_x - 50, center_y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2)
        cv2.putText(dest_img, current_time, (center_x - 50, center_y + 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2)

(width_c,height_c) = 1000,750

cap = cv2.VideoCapture(0)
cap.set(3,width_c)
cap.set(4,height_c)

while True:
    success,Original_img = cap.read()
    Original_img = cv2.resize(Original_img,(width_c,height_c))
    if not success:
        break
    else:
        Gray_img = cv2.cvtColor(Original_img,cv2.COLOR_BGR2GRAY)
        marker_corners,marker_ids,reject = cv2.aruco.detectMarkers(Gray_img,marker_dict,parameters=param_markers)
        if marker_ids is not None:
            for ids,corners in zip(marker_ids.flatten(),marker_corners):
                corners = corners.reshape(-1,4,2).astype(np.int32)
                cv2.fillConvexPoly(Original_img,corners,0)
                if ids in timezones:
                    DrawTime(Original_img,corners,timezones[ids],False)
                else:
                    DrawTime(Original_img,corners,None,True)
        cv2.imshow("Original Img",Original_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

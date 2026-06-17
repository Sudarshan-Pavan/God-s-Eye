import cv2
import numpy as np
cap = cv2.VideoCapture(0)

pts = []
while (1):

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([155, 75, 255])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
   
    moments = cv2.moments(contour)
    cX = int(moments["m10"] / moments["m00"])
    cY = int(moments["m01"] / moments["m00"])

    cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)

    print(f"Laser detected at ({cX}, {cY})")
    
    cv2.imshow('Track Laser', frame)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

cap.release()
cv2.destroyAllWindows()
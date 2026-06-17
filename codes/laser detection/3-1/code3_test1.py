import cv2
import numpy as np
cap = cv2.VideoCapture(0)

pts = []
while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_red = np.array([100, 200, 255])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 10:
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])

            cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)

            print(f"Laser detected at ({cX}, {cY})")

    cv2.imshow("Laser Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

cap.release()
cv2.destroyAllWindows()
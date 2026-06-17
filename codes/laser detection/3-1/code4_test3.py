import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)  

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(gray, 5, 20, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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

video_capture.release()
cv2.destroyAllWindows()
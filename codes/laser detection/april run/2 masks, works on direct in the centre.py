import cv2
import numpy as np
from cvzone.SerialModule import SerialObject

#arduino = SerialObject()
video_capture = cv2.VideoCapture(0)
# frame dimensions = 640H/480V

#cX = int
#cY = int

frame_count = 0  # Initialize frame count

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture frame")
        break

    frame_count += 1
    if frame_count % 2 == 0:  # Process every second frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define a more specific red color range for the red laser
        lower_red = np.array([0, 150, 255])
        upper_red = np.array([50, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red2 = np.array([160, 100, 255])
        upper_red2 = np.array([180, 255, 255])

        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        mask = cv2.bitwise_or(mask1, mask2)

        result = cv2.bitwise_and(frame, frame, mask=mask)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 10:
                moments = cv2.moments(contour)
                if moments["m00"] != 0:  # Prevent division by zero
                    cX = int(moments["m10"] / moments["m00"])
                    cY = int(moments["m01"] / moments["m00"])

                    cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)
                    print(f"Laser detected at ({cX}, {cY})")

        cv2.imshow("Laser Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

video_capture.release()
cv2.destroyAllWindows()

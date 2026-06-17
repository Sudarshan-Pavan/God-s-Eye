#laser shape and size included
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0) 

while True:
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_laser = np.array([155, 160, 255])  # lower range of the laser red 
    upper_laser = np.array([255, 255, 255])  # upper range of the laser red

    mask = cv2.inRange(hsv, lower_laser, upper_laser)  # combining the 2 layers ranges

    result = cv2.bitwise_and(frame, frame, mask=mask)  # taking in mask as a result frame

    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)  # converting the color layer to black and white for threshold 
    _, threshold = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY)  # creating threshold for recognition

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # recognizing the white contours in the threshold 

    for contour in contours:
        area = cv2.contourArea(contour)

        # Additional filters based on shape and size
        #epsilon = 0.02 * cv2.arcLength(contour, True)
        #approx = cv2.approxPolyDP(contour, epsilon, True)

        #if area > 10 and len(approx) > 6:
        if area > 10:
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])

            cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)
            print(f"Laser detected at ({cX}, {cY})")

    cv2.imshow("Laser Detection", frame)  # showing the camera recording
    cv2.imshow("Laser Detection", threshold)  # showing the camera recording

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
    # closing the camera ("laser detection") window

video_capture.release()
cv2.destroyAllWindows()

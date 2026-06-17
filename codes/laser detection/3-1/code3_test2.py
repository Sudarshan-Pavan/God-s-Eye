import cv2
import numpy as np
cap = cv2.VideoCapture(0)

pts = []
while (1):

    # Take each frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold = cv2.threshold(hsv, 200, 255, cv2.THRESH_BINARY)[1]
    contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    lower_red = np.array([100, 200, 255])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

    # Process the contours
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        # Ignore small contours
        if area < 50:
            # Find the centroid of the contour
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])


    cv2.circle(frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Track Laser', frame)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

    moments = cv2.moments(hsv[:, :, 2])
x = int(moments['m10'] / moments['m00'])
y = int(moments['m01'] / moments['m00'])

cap.release()
cv2.destroyAllWindows()
# NEED SHIT TON OF EDITING
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0) 

while True:
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_laser = np.array([120, 160, 255])  # Lower range of the laser red 
    upper_laser = np.array([255, 255, 255])  # Upper range of the laser red

    mask = cv2.inRange(hsv, lower_laser, upper_laser)  # Combining the 2 layers ranges
 
    result = cv2.bitwise_and(frame, frame, mask=mask)  # Taking in the mask as a result frame

    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)  # Converting the color layer to black and white for threshold 
    _, threshold = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY)  # Creating threshold for recognition

    # Apply morphological operations
    kernel = np.ones((3, 3), np.uint8)
    #erosion = cv2.erode(threshold, kernel, iterations=1)
    dilation = cv2.dilate(threshold, kernel, iterations=1)

    # Use the processed image for contour detection
    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        # Recognizing the laser and finding the co-ordinates
        if area > 10:
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])

            cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)  # Creating circle at the laser recognized

            print(f"Laser detected at ({cX}, {cY})")  # Printing detected co-ordinates

    cv2.imshow("Laser Detection", frame)  # Showing the camera recording

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
    # Closing the camera ("laser detection") window
 
video_capture.release()
cv2.destroyAllWindows()

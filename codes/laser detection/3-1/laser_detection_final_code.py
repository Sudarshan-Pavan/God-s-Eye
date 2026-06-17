import cv2
import numpy as np

video_capture = cv2.VideoCapture(0) 

while True:
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_laser = np.array([155, 160, 255]) #lower range of the laser red 
    upper_laser = np.array([255, 255, 255]) #upper range of the laser red

    mask = cv2.inRange(hsv, lower_laser, upper_laser) #combining the 2 layers ranges
 
    result = cv2.bitwise_and(frame, frame, mask=mask) #taking in the mask as a result frame

    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY) #converting the color layer to black and white for threshold 
    _, threshold = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY) #creating threshold for recognition

    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #recognising the white contours in the threshold 

    for contour in contours:
        area = cv2.contourArea(contour)
#recognising the laser and finding the co-ordinates
        if area > 10:
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])

            cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1) #creating circle at the laser recognised

            print(f"Laser detected at ({cX}, {cY})") #printing detected co-ordinates

    #cv2.flip(frame, 0)
    cv2.imshow("Laser Detection", frame) #showing the camera recording

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
    #closing the camera ("laser detection") window
 
video_capture.release()
cv2.destroyAllWindows() 
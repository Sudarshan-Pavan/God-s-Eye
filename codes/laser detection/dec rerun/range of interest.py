#WASTE !!!!!!!!!!!!!!!!!!!!!!!
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

# Define ROI coordinates (adjust as needed)
roi_x, roi_y, roi_w, roi_h = 300, 200, 50, 50

while True:
    ret, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define ROI
    roi = hsv[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]

    # Calculate average color in ROI
    avg_color = np.mean(roi, axis=(0, 1))

    # Dynamically adjust lower color range based on average color
    lower_laser = np.clip(avg_color - 20, 0, 255).astype(np.uint8)

    upper_laser = np.array([255, 255, 255], dtype=np.uint8)  # Specify dtype

    mask = cv2.inRange(hsv, lower_laser, upper_laser)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(result, 1, 255, cv2.THRESH_BINARY)

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

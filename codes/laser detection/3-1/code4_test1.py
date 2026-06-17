import cv2
import numpy as np

# Set up the video capture
video_capture = cv2.VideoCapture(0)  # Change the parameter to the appropriate video source

while True:
    # Read the current frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([100, 100, 255])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

    # Apply a threshold to create a binary image
    _, threshold = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Process the contours
    for contour in contours:
        # Calculate the contour area
        area = cv2.contourArea(contour)

        if area > 10:
            # Find the centroid of the contour
            moments = cv2.moments(contour)
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])

            # Draw a circle at the centroid
            cv2.circle(frame, (cX, cY), 4, (0, 255, 0), -1)

            # Print the coordinates
            print(f"Laser detected at ({cX}, {cY})")

    # Display the resulting frame
    cv2.imshow("Laser Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('m'):
        break

# Release the video capture and close the windows
video_capture.release()
cv2.destroyAllWindows()

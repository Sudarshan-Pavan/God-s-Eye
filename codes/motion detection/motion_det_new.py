import cv2
import winsound
import threading
import imutils

# Initialize the webcam
video_capture = cv2.VideoCapture(0)  # 0 represents the default camera

# Initialize variables
previous_frame = None
motion_detected = False

# Function to play the alarm sound
def play_alarm():
    winsound.Beep(1000, 500)  # You can customize the frequency and duration

def detect_motion(frame):
    global motion_detected
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if previous_frame is None:
        previous_frame = gray_frame
        return
    
    frame_diff = cv2.absdiff(previous_frame, gray_frame)
    _, thresholded_diff = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresholded_diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        
        motion_detected = True
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Start the alarm thread
        alarm_thread = threading.Thread(target=play_alarm)
        alarm_thread.start()

def main():
    global previous_frame
    
    while True:
        ret, frame = video_capture.read()
        
        frame = imutils.resize(frame, width=600)
        motion_detected = False
        
        detect_motion(frame)
        
        cv2.imshow('Motion Detection', frame)
        
        if motion_detected:
            print("Motion detected!")
        
        previous_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()


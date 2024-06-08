import cv2
import serial

# Initialize serial communication with ESP8266
ser = serial.Serial('COM4', 9600)  # Replace 'COMX' with the appropriate COM port

# Load pre-trained HOG + SVM model for human detection
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Global variables for ROI selection
roi_defined = False
roi_x, roi_y, roi_w, roi_h = 0, 0, 0, 0

# Mouse callback function for ROI selection
def select_roi(event, x, y, flags, param):
    global roi_defined, roi_x, roi_y, roi_w, roi_h

    if event == cv2.EVENT_LBUTTONDOWN:
        roi_defined = False
        roi_x, roi_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        roi_defined = True
        roi_w, roi_h = x - roi_x, y - roi_y

# Create a video capture object
cap = cv2.VideoCapture(0)

# Set up the window and callback
cv2.namedWindow('Webcam Feed')
cv2.setMouseCallback('Webcam Feed', select_roi)

# Initialize buzzer state and last detection status
buzzer_active = False
last_detection_status = False

while True:
    ret, frame = cap.read()

    # Draw the ROI if defined
    if roi_defined:
        cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_w, roi_y + roi_h), (0, 255, 0), 2)

        # Extract the selected ROI
        roi = frame[roi_y:roi_y + roi_h, roi_x:roi_x + roi_w]

        # Detect humans in the ROI
        (rects, weights) = hog.detectMultiScale(roi, winStride=(4, 4), padding=(8, 8), scale=1.05)

        # Update detection status
        detection_status = len(rects) > 0

        # Activate the buzzer if human detected and it wasn't active before
        if detection_status and not buzzer_active:
            ser.write(b'b')
            buzzer_active = True
            print("Human detected! Buzzer activated!")

        # Deactivate the buzzer if no human detected and it was active before
        elif not detection_status and buzzer_active:
            ser.write(b's')
            buzzer_active = False
            print("")

    # Update last detection status
    last_detection_status = detection_status if roi_defined else False

    # Display the frames
    cv2.imshow('Webcam Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
import cv2

# Define a function to be called when the trackbar is moved
def on_trackbar(val):
    pass

# Create a window to display the video and trackbar
cv2.namedWindow('video3.mp4')
cv2.createTrackbar('Threshold', 'video3.mp4', 0, 255, on_trackbar)

# Open the video file
cap = cv2.VideoCapture('video3.mp4')

# Loop until the end of the video file is reached
while cap.isOpened():
    # Read a frame from the video file
    ret, frame = cap.read()

    # If the frame was read successfully
    if ret:
        # Get the current value of the trackbar
        threshold = cv2.getTrackbarPos('Threshold', 'video3.mp4')

        # Process the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        result = cv2.bitwise_and(frame, frame, mask=binary)

        # Display the result
        cv2.imshow('video3.mp4', result)

        # Check if the 'q' key was pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

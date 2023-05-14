import cv2 as cv
cap = cv.VideoCapture('tom.mp4')

fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('out_video.mp4', fourcc, 25, (180, 144))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame_resized = cv.resize(frame, (180, 144), interpolation = cv.INTER_LINEAR)
        out.write(frame_resized)
    else:
        break


cap.release()
out.release()


import cv2
import imutils

cam = cv2.VideoCapture("d:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\Test_Open_CV\\img\\DLTTAD.mp4")

while True:
    ret, frame = cam.read()
    
    if ret:
        if cv2.waitKey(1) == ord('a'):
            frame = imutils.rotate(frame,-90)
        elif cv2.waitKey(1) == ord('d'):
            frame = imutils.rotate(frame,90)
        elif cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow("video",frame)

cam.release()
cv2.destroyWindow()
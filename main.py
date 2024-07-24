import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cam.release()
cv2.destroyWindow()
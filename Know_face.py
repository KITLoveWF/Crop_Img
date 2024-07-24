import cv2

face = cv2.CascadeClassifier("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\Crop_Img\\Crop_Img\\haar.xml")
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if ret:
        # nhận diện khuôn mặt
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(img_gray,scaleFactor=1.05,minNeighbors=5,minSize=(30,30))
        for (x,y,w,h) in faces:
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('a'):
        print(1)
        # lưu ảnh
        count = 0
        for(x,y,w,h) in faces:
            img_crop = frame[y:y+h,x:x+w]
            if count == 0:
                cv2.imwrite("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\faces\\{}.jpg".format(count),img_crop)
            count = count+1
    #print("Số khuôn mặt" , len(faces))
    cv2.imshow("webcam",frame)

cam.release()
cv2.destroyAllWindows()

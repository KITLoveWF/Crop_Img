import cv2

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if ret:
        # tinh diem trung tam
        # (h,w)
        width = frame.shape[1]
        height = frame.shape[0]
        center_x = width//2 # lay phan nguyen
        center_y = height//2
        # tinh kich thuoc can lay
        width_need = int(width*0.2)
        height_need = int(height*0.2)
        # point first
        x_fi = center_x - width_need//2
        y_fi = center_y - height_need//2
        # point second 
        x_se = center_x + width_need//2
        y_se = center_y + height_need//2
        # cat canh
        crop_img = frame[y_fi:y_se,x_fi:x_se]

        #crop_img =frame[100:200,150:350] (150,100) -> (350,200)
        cv2.imshow("Video", crop_img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cam.release()
cv2.destroyWindow()
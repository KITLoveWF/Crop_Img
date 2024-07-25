import cv2
import numpy as np


# định nghĩa ngưỡng lọc màu 
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])
lower_green = np.array([40,50,50])
upper_green = np.array([90,255,255])
lower_yellow = np.array([15,150,150])
upper_yellow = np.array([35,255,255])

img = cv2.imread("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\Crop_Img\\Crop_Img\\t_light_all.jpeg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask_red = cv2.inRange(hsv,lower_red,upper_red)
cv2.imshow("img",img)
cv2.imshow("",mask_red)

contour_red,_ = cv2.findContours(mask_red,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

if(len(contour_red)>0): print("xanh")
cv2.waitKey()
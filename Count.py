import cv2

img = cv2.imread("D:\\Football_Analistic_System\\Week_1\\Test_OpenCv\\Crop_Img\\Crop_Img\\balloon.png")

# tạo ảnh xám
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# tạo ngưỡng
ret, near_max = cv2.threshold(img_gray,230,255,cv2.THRESH_BINARY)

# đếm số đường bao (coutour) > 1 giá trị do ta ước lượng
contour, _ = cv2.findContours(near_max,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
Min_area = (img.shape[1]*img.shape[0]) / 150
count = 0
for cnt in contour[:-1]:
    if cv2.contourArea(cnt) >= Min_area:
        count = count + 1
        cv2.drawContours(img,[cnt],-1,(0,255,0),2,cv2.LINE_AA)

print("Số bóng", count)
cv2.imshow("nguong", near_max)

cv2.imshow("img",img)

cv2.waitKey()
cv2.destroyWindow()
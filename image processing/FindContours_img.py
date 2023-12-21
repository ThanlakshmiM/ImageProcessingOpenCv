import cv2  # library cv2
import imutils

img = cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshImg=cv2.threshold(grayImg,180,225,cv2.THRESH_BINARY)[1]
dst = cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(dst)
area = 500
for c in cnts:
    if cv2.contourArea(c)<area:
        continue
    (x,y,w,h)=cv2.boundingRect(c)
    pt1 = (x, y)  # Top-left corner
    pt2 = (x+w, y+h)  # Bottom-right corner
    color = (0, 255, 0)  # Rectangle color in BGR format (green in this case)
    thickness = 2  # Line thickness

rect=cv2.rectangle(img, pt1, pt2, color, thickness)
#rect=cv2.rectangle(img,(x,y),(x+w,y+h,(0,255,0),2))
cv2.imwrite("image5.jpg",rect)
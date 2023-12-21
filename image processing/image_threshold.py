import cv2   #  library cv2

img=cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")   # image read
greyImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          # block on while convert
threshImg=cv2.threshold(greyImg,180,255,cv2.THRESH_BINARY) [1]  # only block and white compleate threshold
cv2.imwrite("image2.jpg",threshImg)   # image save
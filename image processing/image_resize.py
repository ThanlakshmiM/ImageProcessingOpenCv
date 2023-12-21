import cv2  # library cv2
import imutils  # library imutils

img=cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")  # image read
resizeImg=imutils.resize(img,width=100)  # image resize
cv2.imwrite("image.jpg",resizeImg) # image save
import cv2  # lbrary cv2

img=cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")  # image read
gaussianBlur=cv2.GaussianBlur(img,(21,21),0)  # image smoothing format using gaussian
cv2.imwrite("image1.jpg",gaussianBlur)   # image save
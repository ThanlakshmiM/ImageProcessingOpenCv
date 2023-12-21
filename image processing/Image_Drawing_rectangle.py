import cv2  # library cv2

img=cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")

rectangleImg=cv2.rectangle(img,(5,5),(220,220),(255,0,0),2)  # image detect rectange shape-img,startPoint,EndPoint,color,thickness

cv2.imwrite("image3.jpg",rectangleImg)

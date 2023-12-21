import cv2 # library cv2

img = cv2.imread(r"C:\Users\user\Desktop\python\final_project\invesment sucusss.png")
Text=cv2.putText(img,"Hi..Guys",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,10,0,255,2) # img,text,position,font,fontsize,color,thickness
cv2.imwrite("image4.jpg",Text)
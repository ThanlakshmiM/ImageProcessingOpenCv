import cv2
from matplotlib import pyplot as plt
car_cascade= cv2.CascadeClassifier(r'C:\Users\user\Desktop\python\image processing\cars.xml')
cap = cv2.VideoCapture(r'C:\Users\user\Desktop\python\image processing\cars.mp4')

import cv2
print(cv2.__version__)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    if cv2.waitKey(33) == 27:
        break
    plt.imshow(gray)
    plt.axis('off')  # Turn off axis labels

cv2.destroyAllWindows()
plt.show()
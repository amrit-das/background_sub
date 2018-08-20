import cv2
import numpy as np
from PIL import Image, ImageDraw



height = 478
width = 639
step_size = int(width / 71)
img=cv2.imread("white.jpg")
for x in range(0, width, step_size):
    for y in range (0,height,step_size):
        cv2.rectangle(img,(x,y),(x+step_size,y+step_size),(0,0,0),3)
cv2.imshow("",img)

'''cap=cv2.VideoCapture(0)
ret=True
loop=0
while ret:
    loop+=1
    if (loop%100)==0:
        ret,cam=cap.read()
        cv2.namedWindow('image',)
        cv2.resizeWindow('image', 639,478)
        gray = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
        h = np.size(gray, 1)
        w = np.size(gray, 0)
        count=0
        black_square=0
        for i in range (0,h-9,9):
            for j in range (0,w-9,9):
                for k in range (i,i+9):
                    for l in range (j,j+9):
                        if gray[k,l]<127:
                            count+=1
                            if count>10:
                                draw.rectangle(((i, j), (i+step_size,j+step_size)), fill="#000000")
                                black_square+=1
        #image.show()
        print black_square*100/(478*639),"%"
        cv2.imshow("image",gray)
        if cv2.waitKey(5)==27:
            break
cap.release()'''

#FOR ONLY IMAGE 
cam=cv2.imread('panda.png')
gray = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
h = np.size(gray, 1)
w = np.size(gray, 0)
count=0
for i in range (0,h-9,9):
    for j in range (0,w-9,9):
        for k in range (i,i+9):
            for l in range (j,j+9):
                if gray[k,l]<127:
                    count+=1
                    if count>10:
                        cv2.rectangle(img,(x,y),(x+step_size,y+step_size),(0,0,0),-1)    
cv2.imshow("image",gray)



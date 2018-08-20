import cv2
import numpy as np

def mouse_click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        for i in range (1,height-1):
            for j in range (1,width-1):
                if (i==x and j==y):
                    [b,g,r]= image3[i,j]
                    print b,g,r
                    #arr=np.uint8([[[b,g,r]]])
                    #print cv2.cvtColor(arr,cv2.COLOR_BGR2YUV)
                    break

image1 = cv2.imread("img0.jpg")
image2 = cv2.imread("img2.jpg")
image3 = cv2.absdiff(image1,image2)
height = np.size(image3, 0)
width = np.size(image3, 1)


cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_click)
cv2.imshow('image',image3)
cv2.waitKey(0)

    
        

import cv2
import numpy as np

global pixel,pixel1

pixel=np.uint8([[[0,0,0]]])
global con
con=False
def mouse_click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        con=True
        #print "***"
        for i in range (1,height-1):
            for j in range (1,width-1):
                if (i==x and j==y):
                    _, frame1 = cap.read()
                    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
                    print "**"
                    #pixel= np.array(frame[i,j])
                    pixel=np.uint8([[frame[i,j]]])

                    print pixel
                    pixel1 = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
                    lower = np.array([50,50,pixel1[0][0][2]-10])
                    upper = np.array([255,255,pixel1[0][0][2]+10])
                    #lower_lab = np.array([45,128,123])
                    #upper_lab = np.array([93,209,27])
                    #lower_lab = np.array([0,109,200])
                    #upper_lab = np.array([255,150,255])

                    
                    mask = cv2.inRange(hsv, lower, upper)
                    #mask_lab=cv2.inRange(lab,lower_lab, upper_lab)

                    
                    res = cv2.bitwise_and(frame,frame, mask= mask)
                    _,contour,hier=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
                    cv2.drawContours(mask,contour,-1,(127),3)
                    cv2.imshow('mask',mask)
                    cv2.imshow('res',res)
                #cv2.imshow('frame',frame)
                
                #cv2.imshow('mask_lab',mask_lab)
                    

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lab=cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    img=cv2.imread('color.png',1)
    height = np.size(frame, 0)
    width = np.size(frame, 1)
    cv2.namedWindow('image')
    cv2.imshow('image',frame)
    cv2.setMouseCallback('image',mouse_click)
    '''
    print con,"**"
    if con:
        print pixel
        pixel1 = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
        lower = np.array([50,50,pixel1[0][0][2]-10])
        upper = np.array([255,255,pixel1[0][0][2]+10])
        #lower_lab = np.array([45,128,123])
        #upper_lab = np.array([93,209,27])
        #lower_lab = np.array([0,109,200])
        #upper_lab = np.array([255,150,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower, upper)
        #mask_lab=cv2.inRange(lab,lower_lab, upper_lab)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
        contour,hier=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(mask,contour,-1,(127),3)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)'''
    #cv2.imshow('frame',frame)
    
    #cv2.imshow('mask_lab',mask_lab)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
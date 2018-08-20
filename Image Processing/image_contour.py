import cv2
import numpy as np
img = cv2.imread('panda.png',0)
ret,thresh = cv2.threshold(img,127,255,0)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(127),3)
cv2.imshow("",img)
cnt = contours[0]
M = cv2.moments(cnt)
print( M )
print "CONTOURS",contours
print "HIER",hierarchy
cv2.waitKey(0)
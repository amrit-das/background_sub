import cv2
import numpy as np


cam=cv2.imread('rings.jpg')
gray = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),3)
edge=cv2.Canny(blur,50,200)
_,contour,hier=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(cam,contour,-1,(0,0,255),3)
print contour
cv2.imshow("df",edge)
cv2.imshow("",cam)

cv2.waitKey(0)

cv2.destroyAllWindows()

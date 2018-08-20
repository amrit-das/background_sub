import cv2
import numpy as np
from math import pi
f=cv2.imread('fan.jpg')   
img_yuv = cv2.cvtColor(f, cv2.COLOR_BGR2YUV)
refPt = []
cropping = False
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        cropping = True
    elif cropping==True:
        refPt.append((x+5, y+5))
        cropping = False
clone = img_yuv.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
while True:
    cv2.imshow("image", img_yuv)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("r"):
        image = clone.copy()
 
    elif key == ord("c"):
        break
if len(refPt) == 2:
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    #cv2.imshow("ROI", roi)
    count=0
    sum=np.array([0,0,0])
    for i in range (0,np.size(roi,0)):
        for j in range(0,np.size(roi,1)):
            count+=1
            sum+=roi[i,j]
    [y,u,v]=np.array(sum/count)
    drag_area=np.size(roi,0)*np.size(roi,1)
    print "drag area",drag_area
    print [y,u,v]
q=15
mask = cv2.inRange(img_yuv, (np.array([y-q,u-q,v-q])), (np.array([y+q,u+q,v+q])))
cv2.imshow("Masking_yuv_board",mask)
erode = cv2.erode(mask,None,iterations = 1)
dilate = cv2.dilate(erode,None,iterations = 1)
image,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_yuv, contours, -1, (0,255,0), 2)
cv2.imshow("contour_yuv_board", img_yuv)
cv2.waitKey(0)
cv2.destroyAllWindows()
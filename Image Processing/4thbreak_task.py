import cv2
import numpy as np
from PIL import Image,ImageFilter,ImageDraw
import random

img1 = Image.open('embr.png').convert('1')
'''gaus=img1.filter(ImageFilter.GaussianBlur(radius=7))
box=gaus.filter(ImageFilter.BoxBlur(radius=7))
min1=img1.filter(ImageFilter.MaxFilter(size=3))
min1=min1.convert('1')'''
med=img1.filter(ImageFilter.MedianFilter(size=3))
mode=med.filter(ImageFilter.ModeFilter(size=3))
mode1=mode.filter(ImageFilter.FIND_EDGES)
#mode.save("mode.png")
image=cv2.imread("mode.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(thresh_img,kernel,iterations =1)
dilation = cv2.dilate(erosion,kernel,iterations = 1)

_,contours,hierarchy = cv2.findContours(dilation,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 2)

'''circles = cv2.HoughCircles(thresh_img,cv2.HOUGH_GRADIENT, 1.2, 100)
print circles
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	print "done"
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(image, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)'''
 

#mask1=img1.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=1))


cv2.imshow("",image)
print len(contours)-1

cv2.waitKey(0)




#newTry

import cv2
import numpy as np


def average(refPt,x,y):
	roi = frame[refPt[0][1]:refPt[1][1],refPt[0][0]:refPt[1][0]]
	cv2.rectangle(frame,(x,y),(x+30,y+30),(255,0,0),1)
	cv2.imshow("frame",frame)
	count = 0
	sum = np.array([0,0,0])
	for i in range (0,np.size(roi,0)):
		for j in range(0,np.size(roi,1)):
			count+=1
			sum += roi[i,j]
	[b,g,r] = np.array(sum/count)
	return [b,g,r]


def click_and_return(event, x, y, flags, param):
	global refPt,frame,click,y1,u,v

	if event == cv2.EVENT_LBUTTONDOWN:
		click = True
		refPt.append((x, y))
		refPt.append((x+30,y+30))
	
	elif event == cv2.EVENT_LBUTTONUP:
		print x,y
		[b,g,r]= average(refPt,x,y)
		#[b,g,r] = frame[y,x]
		arr =  np.uint8([[[b,g,r]]])
		[[[y1,u,v]]] = cv2.cvtColor(arr,cv2.COLOR_BGR2YUV)
		#print frame[x,y]

		'''y = int(0.299*r + 0.587*g + 0.114*b)
		u = int(0.492*(b-y))
		v = int(0.877*(r-y))'''
		print b,g,r, "BGR"
		print y1,u,v, "YUV"
		print click

	else:
		pass


try:
	index = 1
except:
	index = 0

cap = cv2.VideoCapture(index)

kernel = np.ones((5,5),np.uint8)

width,height = cap.get(3),cap.get(4)
ret,click = True,False
refPt = []
y1,u,v = 0,0,0

cv2.namedWindow("Image")


while ret:
	
	ret,frame = cap.read()

	if click:

		blur1 = cv2.GaussianBlur(frame,(5,5),0)
		blur2 = cv2.bilateralFilter(blur1,9,75,75)
		
		img_yuv = cv2.cvtColor(blur2,cv2.COLOR_BGR2YUV)
		
		mask = cv2.inRange(img_yuv, (np.array([0,u-17,v-17])), (np.array([255,u+17,v+17])))
		erode = cv2.erode(mask,kernel,iterations = 1)
		dilate = cv2.dilate(erode,kernel,iterations = 1)

		print u,v
		#mask = cv2.inRange(dilate, (np.array([0,u-12,v-12])), (np.array([255,u+12,v+12])))

		erode = cv2.erode(dilate,kernel,iterations = 1)
		dilate = cv2.dilate(erode,kernel,iterations = 1)

		image,contour,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		#cv2.rectangle(frame,(x,y),(x+10,y+10),(255,0,0),3)
		#cv2.drawContours(frame,contour,(0,0,255),2)
		#cnt = max(contour, key = cv2.contourArea)



		cv2.imshow("Image",frame)
		cv2.imshow("",dilate)
	

	else:
		cv2.imshow("Image", frame)
		cv2.setMouseCallback("Image", click_and_return)

	if cv2.waitKey(1) == 27:
		ret = False

cv2.destroyAllWindows()
cap.release()


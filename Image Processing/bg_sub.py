import numpy as np
import cv2
import math
from skimage.measure import compare_ssim

image1 = cv2.imread("fan0.jpg")
image2 = cv2.imread("fan1.jpg")
grayA = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayA.jpg",grayA)
cv2.imwrite("grayB.jpg",grayB)
(score, diff) = compare_ssim(grayB, grayA, full=True)
diff = (diff * 255).astype("uint8")
thresh = cv2.threshold(diff, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
blur = cv2.GaussianBlur(diff,(5,5),1)
kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(thresh,kernel,iterations = 1)
dilate = cv2.dilate(erode,kernel,iterations = 1)
cv2.imwrite("diff.jpg",diff)
cv2.imwrite("dilate.jpg",dilate)
img1,contours,hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for c in contours:
	if cv2.contourArea(c)>1000:
		x,y,w,h=cv2.boundingRect(c)
		cv2.rectangle(image2,(x,y),(x+w,y+h),[255,0,0],1)
		cv2.drawContours(image2, c, -1, (0,255,0), 2)
		if max(w,h)==w:
			roi1 = dilate[y:(y+h), x:(x+(w/2))]
			roi2 = dilate[y:(y+h),(x+(w/2)):(x+w)]
			cv2.imwrite("ROI1.jpg",roi1)
			cv2.imwrite("ROI2.jpg",roi2)
			im1 = np.asarray(roi1, dtype=np.float)
			im2 = np.asarray(roi2, dtype=np.float)
			sum1= im1.sum()
			sum2=im2.sum()
			if sum1>sum2:
				top1=tuple(c[c[:, :, 0].argmin()][0])
				bottom1=tuple(c[c[:, :, 0].argmax()][0])
				cv2.circle(image2, top1, 3, (255, 0, 0), -1)
				cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
				print "Top: ",top1
				print "Bottom: ",bottom1
			else:
				top1=tuple(c[c[:, :, 0].argmax()][0])
				bottom1=tuple(c[c[:, :, 0].argmin()][0])
				cv2.circle(image2, top1, 3, (255, 0, 0), -1)
				cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
				print "Top: ",top1
				print "Bottom: ",bottom1

			print "hori"
		else:
			roi1=dilate[y:(y+(h/2)),x:x+w]
			roi2=dilate[(y+(h/2)):y+h,x:x+w]
			cv2.imwrite("ROI1.jpg",roi1)
			cv2.imwrite("ROI2.jpg",roi2)
			im1 = np.asarray(roi1, dtype=np.float)
			im2 = np.asarray(roi2, dtype=np.float)
			sum1= im1.sum()
			sum2=im2.sum()
			if sum1>sum2:
				top1=tuple(c[c[:, :, 1].argmin()][0])
				bottom1=tuple(c[c[:, :, 1].argmax()][0])
				cv2.circle(image2, top1, 3, (255, 0, 0), -1)
				cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
				print "Top: ",top1
				print "Bottom: ",bottom1
			else:
				top1=tuple(c[c[:, :, 1].argmax()][0])
				bottom1=tuple(c[c[:, :, 1].argmin()][0])
				cv2.circle(image2, top1, 3, (255, 0, 0), -1)
				cv2.circle(image2, bottom1, 3, (0, 0, 255), -1)
				print "Top: ",top1
				print "Bottom: ",bottom1
			print "vert"

cv2.imwrite("final.jpg",image2)

cv2.waitKey(0)

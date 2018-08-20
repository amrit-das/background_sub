import cv2
import numpy as np

cam = cv2.VideoCapture(3)

while True:
	ret,frame = cam.read()
	cv2.imshow("hgfh",frame)
	if cv2.waitKey(5) == 27:
		break

cap.release()
cv2.destroyAllWindows()
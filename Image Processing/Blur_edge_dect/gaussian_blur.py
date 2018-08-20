import numpy as np
from math import exp
import cv2

def ker(n,m):
	Y=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
	X=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
	num=exp(-(X[n,m]**2+Y[n,m]**2)/2*dev**2)
	return num

img=cv2.imread('bike.jpg',1)

img2=cv2.imread('bike.jpg',1)

height = np.size(img2, 0)

width = np.size(img2, 1)
dev=0.5
k=1.0/(2*3.14*dev*dev)
kernel_mat=1.7*k*(np.array([[ker(0,0),ker(0,1),ker(0,2)],[ker(1,0),ker(1,1),ker(1,2)],[ker(2,0),ker(2,1),ker(2,2)]]))

for g in range (0,6):
	for i in range (1,height-1):
		for j in range (1,width-1):
			img2[i,j]=(img[i-1,j-1]*kernel_mat[0,0]+img[i-1,j]*kernel_mat[0,1]+img[i-1,j+1]*kernel_mat[0,2]+img[i,j-1]*kernel_mat[1,0]+img[i,j]*kernel_mat[1,1]+img[i,j+1]*kernel_mat[1,2]+img[i+1,j-1]*kernel_mat[2,0]+img[i+1,j]*kernel_mat[2,1]+img[i+1,j+1]*kernel_mat[2,2])/8
	for i in range (1,height-1):
		for j in range (1,width-1):
			img[i,j]=img2[i,j]    

cv2.imshow('frame',img2)

cv2.waitKey(0)

cv2.destroyAllWindows()



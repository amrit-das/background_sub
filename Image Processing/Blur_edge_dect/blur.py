import numpy as np

import cv2

img=cv2.imread('bike.jpg',1)

img2=cv2.imread('bike.jpg',1)

height = np.size(img, 0)

width = np.size(img, 1)

kernel_mat=(0.65)*np.array([[1,2,1],[2,4,2],[1,2,1]])

for i in range (1,height-1):

    for j in range (1,width-1):

        img2[i,j]=(0.125)*(img[i-1,j-1]*kernel_mat[0,0]+img[i-1,j]*kernel_mat[0,1]+img[i-1,j+1]*kernel_mat[0,2]+img[i,j-1]*kernel_mat[1,0]+img[i,j+1]*kernel_mat[1,2]+img[i+1,j-1]*kernel_mat[2,0]+img[i+1,j]*kernel_mat[2,1]+img[i+1,j+1]*kernel_mat[2,2])

        

cv2.imshow('frame',img2)

cv2.waitKey(0)

cv2.destroyAllWindows()

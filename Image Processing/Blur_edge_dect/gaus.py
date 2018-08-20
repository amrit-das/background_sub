import cv2
import numpy as np
img = cv2.imread('bike.jpg')
gausBlur = cv2.GaussianBlur(img, (5,5),0)

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
capture = cv.CaptureFromCAM(0)

def repeat():

    frame = cv.QueryFrame(capture)
    cv.ShowImage("w1", frame)


while True:
    repeat()

'''img2 = cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )
img3=cv2.cvtColor( img, cv2.COLOR_RGB2GRAY )

height = np.size(img, 0)

width = np.size(img, 1)

kernel_mat=(np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))

for i in range (1,height-1):

    for j in range (1,width-1):

        x=img2[i+1,j-1]*kernel_mat[2,0]+img2[i+1,j]*kernel_mat[2,1]+img2[i+1,j+1]*kernel_mat[2,2]+(img2[i-1,j-1]*kernel_mat[0,0]+img2[i-1,j]*kernel_mat[0,1]+img2[i-1,j+1]*kernel_mat[0,2])

        y=(img2[i-1,j+1]*kernel_mat[0,2]+img2[i,j+1]*kernel_mat[1,2]+img2[i+1,j+1]*kernel_mat[2,2])+(img2[i-1,j-1]*kernel_mat[0,0]+img2[i,j-1]*kernel_mat[1,0]+img2[i+1,j-1]*kernel_mat[2,0])

        img3[i-1,j-1]=sqrt(x**2+y**2)'''
img2=cv2.Canny(gausBlur,150,200)


cv2.imshow("gray",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

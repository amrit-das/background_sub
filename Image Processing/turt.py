import cv2
import numpy as np
from PIL import Image, ImageDraw


if __name__ == '__main__':
    height = 478
    width = 639
    image = Image.new(mode='L', size=(width, height), color=255)


    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 71)

    for x in range(0, image.width, step_size):
    	for y in range (0,image.height,step_size):
    	#line = ((x, y_start), (x, y_end))
    	#draw.line(line, fill=128
    		draw.rectangle(((x,y ), (x+step_size, y+step_size)), outline="#000000")
    '''x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)
    draw.rectangle(((0, 0), (60,60)), fill="#ff8888")'''
    '''
    cap=cv2.VideoCapture(0)
    ret=True
    loop=0
    while ret:
    	ret,cam=cap.read()
    	gray = cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
    	h = np.size(gray, 1)
    	w = np.size(gray, 0)
    	if cv2.waitKey(1)==32:
    		black_square=0
    		for i in range (0,w-9,9):
    			for j in range (0,h-9,9):
    				count=0
    				for k in range (i,i+9):
    					for l in range (j,j+9):
    						if gray[k,l]<127:
    							count+=1
    							if count>5:
    								draw.rectangle(((j, i), (j+step_size,i+step_size)), fill="#000000")
    								black_square+=1
    							else:
    								draw.rectangle(((j, i), (j+step_size,i+step_size)), fill="#ffffff",outline="#000000")
    		image.show()
    		print black_square*100/(478*639),"%"
    		continue
    	cv2.imshow('',gray)
    	if cv2.waitKey(1)==27:
    		break
    cap.release()'''

    #FOR ONLY IMAGE 
    
    cam1=cv2.imread('panda.png')
    gray1 = cv2.cvtColor(cam1,cv2.COLOR_BGR2GRAY)
    h = np.size(gray1, 1)
    w = np.size(gray1, 0)
    count=0
    for i in range (0,w-9,9):
    	for j in range (0,h-9,9):
    		for k in range (i,i+9):
    			for l in range (j,j+9):
    				if gray1[k,l]<127:
    					count+=1
    					if count>10:
    						draw.rectangle(((j, i), (j+step_size,i+step_size)), fill="#000000")
    image.show()
    cv2.imshow("image",gray1)
    cv2.destroyAllWindows()
    del draw

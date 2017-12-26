#!/usr/bin/env python
import cv2
import numpy as np


def region_of_interest(img,vertices,color3=(255,255,255),color1=255):
	mask = np.zeros_like(img)

	if len(img.shape) >2:
		color = color3
	else:
		color = color1

	cv2.fillPoly(mask,vertices,color)

	ROI_image = cv2.bitwise_and(img,mask)
	return ROI_image

def mark_img(img,blue_threshold=200,green_threshold=200,red_threshold=200):
	bgr_threshold = [blue_threshold,green_threshold,red_threshold]

	thresholds=(image[:,:,0]<bgr_threshold[0])|(image[:,:,1]<bgr_threshold[1])|(image[:,:,2]<bgr_threshold[2])

	mark[thresholds]=[0,0,0]

	return mark


image = cv2.imread('solidWhiteCurve.jpg')
height,width = image.shape[:2]
print(str(height)+","+str(width))

vertices = np.array([[(50,height),(width/2-45,height/2+60),(width/2+45,height/2+60),(width-50,height)]],dtype=np.int32)

roi_img = region_of_interest(image,vertices,(0,0,255))

mark = np.copy(roi_img)
mark = mark_img(roi_img)

cv2.imshow('roi_white',mark)
cv2.imshow('result',image)



cv2.waitKey(0)

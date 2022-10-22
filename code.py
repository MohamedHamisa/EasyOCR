# Install pytorch
#https://pytorch.org/get-started/locally/
# Install easyocr 
!pip install easyocr

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

 #Read in images or video
IMAGE_PATH = 'sign.png'
#IMAGE_PATH = 'surf.jpeg'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)
result

#Draw Results
top_left = tuple(result[0][0][0])#we take the first result # because open cv expects to get tuple as an arguement
bottom_right = tuple(result[0][0][2]) #the third
text = result[0][1] #the word
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
img = cv2.putText(img,text,top_left, font, 0.5,(255,255,255),2,cv2.LINE_AA) #where we want to position the text in white , cv2.LINE_AA) line style
plt.imshow(img)
plt.show()

#Handling Multiple Lines
img = cv2.imread(IMAGE_PATH)
spacer = 100
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
    img = cv2.putText(img,text,(20,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
    spacer+=15
    
plt.imshow(img)
plt.show()

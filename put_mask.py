import cv2
import numpy as np

img1 = cv2.imread('face.jpg')          #name of the image of the person's face
img2 = cv2.imread('mask.png')       #.png image of the mask with black background.


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(img1,1.1,3)

lowerFace = [[face[0][0] , face[0][1] + (face[0][3])//2, face[0][2], (face[0][3])//2 ]]

a,b,c,d = (lowerFace[0][0])+10, (lowerFace[0][1]), (lowerFace[0][2])-20, (lowerFace[0][3])+20    

img2 = cv2.resize(img2,(c,d))
    
# I want to put mask on lower-half of the face, So I create a Region of Interest (ROI)

croped_img1 = img1[b:b+d, a:a+c]

rows,cols,channels = img2.shape
roi = croped_img1[0:rows, 0:cols ]


# Now create a mask of the Mask and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)


# Now black-out the area of Mask in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of Mask from mask image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put mask in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
croped_img1[0:rows, 0:cols] = dst

cv2.imshow('Image',img1)
cv2.waitKey(0)

cv2.destroyAllWindows()


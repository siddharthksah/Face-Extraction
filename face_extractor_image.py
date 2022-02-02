# this code extracts faces in an image and saves it in a folder
# an image can have multiple faces and this code will still work

# importing libraries
from PIL import Image
import numpy as np
import cv2

# the haarcascase file, please download it from here https://github.com/avelino/python-opencv-detect/blob/master/haarcascade_frontalface_alt.xml
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print ("Found {0} faces!".format(len(faces)))

d=0

# padding essentials makes the extracted images look better
padding = 50

# Draw a rectangle around the faces and crop face
for (x, y, w, h) in faces:

    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 25), 2)
    cropped = img[y-padding:y+h+padding,x-padding:x+w+padding]
    dim = (400, 400)
    # resize image
    cropped = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
    filename = "cropped_%d.jpg"%d
    cv2.imwrite(filename,cropped)
    d+=1

#cv2.imshow("Faces found" ,img)
#cv2.waitKey(0)
# this code extracts faces in images inside a folder and saves it in a folder
# an image can have multiple faces and this code will still work

# importing libraries
from PIL import Image
import numpy as np
import cv2, os

# the haarcascase file, please download it from here https://github.com/avelino/python-opencv-detect/blob/master/haarcascade_frontalface_alt.xml
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


#input directory
directory = "/home/siddharth/Desktop/face_extractor/images/"

# output directory where the image will be saved
output_directory = "./output/"


if not os.path.exists('output'):
    os.makedirs('output')
for files in os.listdir(directory):
    try:
        #print(files.split(".")[0])
        img = cv2.imread(directory + files)
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
        padding = 50
        # Draw a rectangle around the faces and crop face
        for (x, y, w, h) in faces:
            #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 25), 2)
            cropped = img[y-padding:y+h+padding,x-padding:x+w+padding]
            dim = (400, 400)
            # resize image
            cropped = cv2.resize(cropped, dim, interpolation = cv2.INTER_AREA)
            filename = files.split(".")[0] + "_cropped_%d.png"%d
            cv2.imwrite(output_directory + filename,cropped)
            d+=1

        #cv2.imshow("Faces found" ,img)
        #cv2.waitKey(0)
    except:
        pass

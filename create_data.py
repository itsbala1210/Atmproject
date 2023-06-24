#creating database
import cv2, sys, numpy, os
import urllib.request
import numpy as np
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'  #All the faces data will be present this folder
sub_data = input("enter the name of the person :")
password = input("enter four digit pin ")
mail = input("enter outlook id")
amount = int(input("enter the amount(min 2000 deposit)"))
while(amount<2000):
    amount =int(input("minimum 2000 deposit required..."))
        
####sub_data = 'hai'  #These are sub data sets of folder, for my faces I've used my name
file_path = os.path.join("users", sub_data + ".txt")
with open(file_path, "w") as f:
    f.write(password + " " + mail+" "+str(amount))
path = os.path.join(datasets, sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
(width, height) = (130, 100)    # defining the size of images 


face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0) #'0' is use for my webcam, if you've any other camera attached use '1' like this
##url="http://192.168.43.1:8080/shot.jpg"
# The program loops until it has 30 images of the face.
count = 1
while count < 101: 
    (_, im) = webcam.read()
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    im=cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path,count), face_resize)
    count += 1
	
    cv2.imshow('OpenCV', im)
    print(str(count)+"Capturing....")
    key = cv2.waitKey(10)
    if key == 27:
        break

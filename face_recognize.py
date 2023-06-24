# facerec.py
import cv2, sys, numpy, os
import urllib
import numpy as np
import time
import os
from subprocess import call
import time
import os
import glob
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import random
#DO THE CHANGES HERE
gmail_user = "balarengasamy12102001@outlook.com"
gmail_pwd = "bala1210"
FROM = 'balarengasamy12102001@outlook.com'
TO = ['balarengasamy12102001@outlook.com'] #must be a list
otp_=random.randint(10000,100000)
pins=1234
def save(a):
    f = open("users/"+n+".txt","w")
    f.write(str(pins)+" "+TO[0]+" "+str(a))
    f.close()
    
def mail1(amount):
    
    msg = MIMEMultipart()
    time.sleep(1)
    msg['Subject'] ="SECURITY"

    #BODY with 2 argument
    
    #body=sys.argv[1]+sys.argv[2]
    #DO THE CHANGES HERE
    body="Your Balance amount is :"+str(amount)
    
    #otp_text="your otp for logging in :"+str(otp_)
    msg.attach(MIMEText(body,'plain'))
    #msg.attach(MIMEText(otp_text,'plain'))
    time.sleep(1)


    ###IMAGE
    fp = open("1.jpg", 'rb')   		
    time.sleep(1)
    img = MIMEImage(fp.read())
    time.sleep(1)
    fp.close()
    time.sleep(1)
    msg.attach(img)
    time.sleep(1)


    try:
            server = smtplib.SMTP("smtp.office365.com", 587) #or port 465 doesn't seem to work!
            print ("smtp.gmail")
            server.ehlo()
            print ("ehlo")
            server.starttls()
            print ("starttls")
            server.login(gmail_user, gmail_pwd)
            print ("reading mail & password")
            server.sendmail(FROM, TO, msg.as_string())
            print ("from")
            server.close()
            print ('successfully sent the mail')
            print('You have been Updated successfully via mail check your mail.....')
    except:
            print ("failed to send mail")
def proceed(option,amount):
    if(option =="1"):
        a = int(input("Enter the amount to be withdrawed...."))
        if(amount<=a):
            print("sry amount cannot be withdrawed.....Excess amount...")
            print("Your balance is"+str(amount))
            return proceed(option,amount)
        else:
            amount = amount-a
            mail1(amount)
            return amount
    elif(option =="2"):
        a = int(input("Enter the amount to be credited...."))
        amount = amount+a
        mail1(amount)
        return amount
    else:
        mail1(amount)
        return amount

        
def mail():
    
    msg = MIMEMultipart()
    time.sleep(1)
    msg['Subject'] ="SECURITY"

    #BODY with 2 argument
    
    #body=sys.argv[1]+sys.argv[2]
    #DO THE CHANGES HERE
    body="Authenthication ..... your otp for logging in :"+str(otp_)
    
    #otp_text="your otp for logging in :"+str(otp_)
    msg.attach(MIMEText(body,'plain'))
    #msg.attach(MIMEText(otp_text,'plain'))
    time.sleep(1)


    ###IMAGE
    fp = open("1.jpg", 'rb')   		
    time.sleep(1)
    img = MIMEImage(fp.read())
    time.sleep(1)
    fp.close()
    time.sleep(1)
    msg.attach(img)
    time.sleep(1)


    try:
            server = smtplib.SMTP("smtp.office365.com", 587) #or port 465 doesn't seem to work!
            print ("smtp.gmail")
            server.ehlo()
            print ("ehlo")
            server.starttls()
            print ("starttls")
            server.login(gmail_user, gmail_pwd)
            print ("reading mail & password")
            server.sendmail(FROM, TO, msg.as_string())
            print ("from")
            server.close()
            print ('successfully sent the mail')
    except:
            print ("failed to send mail")

size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'
n=input("enter your name : ")
print('Training...')
f = open("users/"+n+".txt","r")
a = f.read()
a = a.split(" ")
pins = int(a[0])
TO[0] = a[1]
amount = int(a[2])
f.close()
# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face'
model = cv2.face.FisherFaceRecognizer_create()
model.train(images, labels)

# Part 2: Use fisherRecognizer on camera stream
face_cascade = cv2.CascadeClassifier(haar_file)
##with open("1.txt", mode='a') as file:
webcam = cv2.VideoCapture(0)

##url="http://192.168.43.1:8080/shot.jpg"
while True:

    (_, im) = webcam.read()
##    imgPath=urllib.urlopen(url)
##    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
##    im=cv2.imdecode(imgNp,-1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,255,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        #Try to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)

        if prediction[1]<500:
            #port.write('B')
           # print (names[prediction[0]])
            cv2.putText(im,names[prediction[0]],(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            print('The accessing person is ',str(n))
            
            if names[prediction[0]]==n:
                
                print("The detected face person is : ",names[prediction[0]])  
                print('you can proceed your transaction')
                pin=int(input('enter your pin: '))
                if pin ==pins:#both face and pin matches
                    print("You can continue further")
                    print("Click '1' For withdrawl")
                    print("\nClick '2' For Deposit")
                    print("\nClick '3' For Display")
                    option = input("Enter the above option")
                    amount = proceed(option,amount)
                    save(amount)
                    exit()
                
        
                else:# face matches but pin wrong
                    mail()
                    check_otp=int(input("Enter the otp :"))
                    if check_otp==otp_:
                        print("You can continue further")
                        print("You can continue further")
                        print("Click '1' For withdrawl")
                        print("\nClick '2' For Deposit")
                        print("\nClick '3' For Display")
                        option = input("Enter the above option")
                        amount = proceed(option,amount)
                        save(amount)
                        exit()
                    else :
                        print("Incorrect pin ... exiting the portal")
                
                
            else: # both face and pin not matches
                im2=im
                cv2.putText(im2,'unknown ',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 0, 255))
                print("The detected person is unknown ")
                cv2.imwrite('1.jpg',im2)
                mail()
                check_otp=int(input("enter the otp : "))
                if check_otp==otp_:
                    pin=int(input('enter your pin:'))
                    if pin == pins:
                        print("You can continue further")
                        print("Click '1' For withdrawl")
                        print("\nClick '2' For Deposit")
                        print("\nClick '3' For Display")
                        option = input("\nEnter the above option")
                        amount = proceed(option,amount)
                        save(amount)
                        exit()
                    else:
                        save(amount)
                        print("Incorrect pin ... exiting the portal")
                        exit()

      
        else:
            cv2.putText(im,'Scanning',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    
       

import cv2
import pyautogui
from playsound import playsound

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


kin = input("Enter the Video File Name:")
cap = cv2.VideoCapture("C:\\Users\\K.VISHWA\\Documents\\clinics\\"+kin+".mp4")
j=1;
r=0;
rr=0;
while True:   
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    anyFace = faces;
    if type(anyFace) == tuple:
        print("No face detected");
        r=0;
        rr=0;
    else :
        print("Face detected");
        r=r+1;
        rr=rr+1;
        if r > 7:
                
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\K.VISHWA\Documents\clinics\offline\sample'+str(j)+'.jpg');
                j=j+1;
                if rr > 7:
                    playsound("C:\\Users\\K.VISHWA\\Documents\\clinics\\audio1.mp3")

        

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)


    if cv2.waitKey(30) & 0xff == ord('q'):
        break
        

cap.release()



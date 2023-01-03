import cv2
import os

active = True
path = "faces/"

if not os.path.exists(path):
    os.mkdir(path)

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

while active:
    ret, frame = video_capture.read()

    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors=5)

    for (x,y,w,h) in faces:
        print("x: %d\ty: %d\tw: %d\th: %d" % (x,y,w,h))

        print("Lager ny identitet...")
        roi_color = frame[y:y+h+20, x:x+w+20]
        creating = input("Input your name: ")

        filess = os.listdir(path)

        cv2.imwrite(f"faces/{creating}.png", roi_color)
        print("Image saved!")
        active = False
    
video_capture.release() # Bli ferdig med video fra webcam
cv2.destroyAllWindows() 

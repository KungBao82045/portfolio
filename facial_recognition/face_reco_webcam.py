# Laget av Jacky Cao

import numpy as np
import face_recognition as fr
import cv2
import os

path = "faces/"
if not os.path.exists(path):
    os.mkdir(path)
    print(f"Legg til bilder i '{path}' mappe for at koden skal funke.")


elif not os.listdir(path):
    print(f"'{path}' mappe er tomt. Legg til bilder i mappen for at koden skal funke.")


files1 = os.listdir(path)
load_imgs = np.array([], ndmin=1)
load_imgs1 = np.array(files1)
combine = np.concatenate((load_imgs, load_imgs1))

if os.path.exists(f"{path}.DS_Store"): os.remove(f"{path}.DS_Store")

kjent_ansikt_encode = [] # Rekkefølge er viktig. Ellers så viser navnet feil på kamera
kjent_ansikt_navn = []

for xfile in combine:
    name, type = os.path.splitext(xfile)

    alle_bilder = fr.load_image_file(f"{path}{xfile}")
    alle_ansiktsencode = fr.face_encodings(alle_bilder)[0]

    kjent_ansikt_encode.append(alle_ansiktsencode) 
    kjent_ansikt_navn.append(name)   

video_capture = cv2.VideoCapture(0) # Starter video.
# Til å få ansiktet fra front
face_cascade = cv2.CascadeClassifier("archive_ansiktkjennetegn/cascades/data/haarcascade_frontalface_alt2.xml")


# Protocol
active = True

while active: # Neste steg. Kjennetegne på video. Bruk av while True. Framme for framme
    ret, frame = video_capture.read() # ret betyr boolean og returnerer true hvis frame er tilgjengelig. (Lurer på hvorfor den brukes ikke. Bør undersøke på internett) : frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Endre størrelse på framme
    rgb_frame = small_frame[:, :, ::-1] # Fanger RGB på frammen. Printer ut RGB.
    #print(frame)

    ansikt_locations = fr.face_locations(rgb_frame) # Finner hvor er ansikt i framme. Kan være flere ansikter.
    ansikt_encoding = fr.face_encodings(rgb_frame, ansikt_locations) # tar ramme fra kamera og sjekker fargen. Liksom hvor er ansiktet.

    for (top, right, bottom, left), ansikt_encoding in zip(ansikt_locations, ansikt_encoding): # Location lager array for top right bottom og left. Encoding iterates top, right osv.
        
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        

        match = fr.compare_faces(kjent_ansikt_encode, ansikt_encoding) # Analysere ansikt. Sammenligne hvis koden kjenner musk eller meg eller hvilken ansikt (kjent_ansikt_encode)
        navn = "Ukjent"

        face_distance = fr.face_distance(kjent_ansikt_encode, ansikt_encoding) # Sammenligne mellom analysert ansikt - normal ansikt

        try:  
            best_match_index = np.argmin(face_distance) # Hvis koden kjenner ansikt, print ut spesifikk index. # np.argmin returnerer smallest mulig verdi


            if match[best_match_index]:
                navn = kjent_ansikt_navn[best_match_index] # Hvis true, viser det "Elon Musk" eller hva du endrer på linje 11.

            # Lage rektangel

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 100, 0), 2) # frame for bildet, mest betyr størrelse på rektangel, farge og tykkhet av rektangel.

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 100, 0), cv2.FILLED) # Lag rektangel under.
            font = cv2.FONT_HERSHEY_SIMPLEX # Velg hvilken font det skal se ut.
            cv2.putText(frame, navn, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 2) # Plassering av navn, farger, tykkhet og størrelsen.

            # print("Top:", top, "Right:", right, "Bottom:", bottom, "Left:", left)
        except ValueError as e:
            print(e + f": Ingen bilder i {path}")
    cv2.imshow("Big Boi", frame)

    if cv2.waitKey(1) & 0xFF == ord("d"): # waitKey er sikkert frame per second. Settes på 0, fryser video, 1000 er 1 sek per framme. 1 er den beste jeg kan kjøre FPS kjappere på. For å øke FPS, vet jeg bare å gjøre videoen mindre.
        break


video_capture.release() # Bli ferdig med video fra webcam
cv2.destroyAllWindows() 


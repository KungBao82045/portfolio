

import numpy as np
import face_recognition as fr
import cv2
import os




path = "faces/"
active = True



list_of_files = os.listdir(path) # Innhold i "faces/"



if os.path.exists(f"{path}.DS_Store"): os.remove(f"{path}.DS_Store")

known_faces_encode = [] # Order is important. Otherwise, your name will display wrong.
known_faces_names = []

for xfile in list_of_files:
    name, type = os.path.splitext(xfile) # name on file and what filetype

    all_images = fr.load_image_file(f"{path}{xfile}")     # Load image from faces/example.png
    all_faces_encode = fr.face_encodings(all_images)[0] # Analyze face. Size of mouth, distance between eyes, etc.


    known_faces_encode.append(all_faces_encode)  # After analysis, add into known_faces_encode
    known_faces_names.append(name) # And names. So that the code can display name if recognized.

video_capture = cv2.VideoCapture(0) # Start video.


while active: # Using while loop to display frame as long its true
    ret, frame = video_capture.read() # ret means boolean and returns true if frame is available. (Wonder why it is not used. Should research on the internet): frame is an image array vector captured based on the default frames per second. Vector represent list of values in one dimension.
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25) # Change size of the frame

    face_locations = fr.face_locations(small_frame) # Locate faces. 
    faces_encoding = fr.face_encodings(small_frame, face_locations) # takes a frame from the camera and analyze faces it detects. Size of mouth, distance between eyes, etc.

    for (top, right, bottom, left), faces_encoding in zip(face_locations, faces_encoding): # Location creates array for top right bottom and left. Encoding iterates top, right, bottom and left. 
        
        # Since the original fram was resized, I multiply by 4 to get back original size. 
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        

        match = fr.compare_faces(known_faces_encode, faces_encoding) # Analyze face. Compare if the code knows elon musk or me or which face (known_faces_encode)
        name = "Unknown"

        face_distance = fr.face_distance(known_faces_encode, faces_encoding) # Return array of similar face

        try:  
            best_match_index = np.argmin(face_distance) # armgin return smallest value. Given np.argmin, return closest match between analyzed face and your face on screen. Return index. 


            if match[best_match_index]:
                name = known_faces_names[best_match_index] # If true, then display the name for example "Elon Musk" 

            print(match, best_match_index, name, "\t", f"L: {left} R: {right} T: {top} B: {bottom}\t")

            # Lage rektangel

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 100, 0), 2) # Creates rectangle to fit your face on screen.

            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 100, 0), cv2.FILLED) # Creates recktangle under for names.
            font = cv2.FONT_HERSHEY_SIMPLEX # You can choose which font style you want.
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 2) # Placing name, color, thickness and font size.

            # print("Top:", top, "Right:", right, "Bottom:", bottom, "Left:", left)
        except ValueError as e:
            print(f"\nValueError: {e}\nNo images in {path}")
            active = False

    cv2.imshow("Press D to quit", frame) # Display frame with the name: Press D to quit

    if cv2.waitKey(1) & 0xFF == ord("d"): # waitKey is probably frame per second. If you set it to 0, freezes the video, 1000 is 1 sec per frame.
        break


video_capture.release() # Finish video from webcam
cv2.destroyAllWindows()



***How to use face recognition (step-by-step)***

1. Download or clone my project: https://github.com/KungBao82045/portfolio.git

2. Navigate the folder to ***Python Projects > facial_recognition***

3 Just in case you have some missing modules. Install these libraries inside ***facial_recognition*** folder:
      <ul>
      <li>pip3 install numpy</li>
      <li>pip3 install face_recognition</li>
      <li>pip3 install opencv-python</li>
      </ul>

      

4. The file you are using for facial recognition is ***face_reco_webcam.py***
   Before running this file, create a folder named ***faces***
   
5. Inside the ***faces*** folder you just created, add images of person's face. It should format like this ***your_name_example.png***
   Replace ***your_name_example*** with your name and save it as a PNG file.

6. Run the script. It will display green box around any faces it recognizes and names under the box. If a person's face is not inside the ***faces***          folder, it will display as "Unknown" under the box.

IMPORTANT: Make sure to run ***face_reco_webcam.py from face_recognition folder. If you run it from different folder, it may not work.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

OPTIONAL: You can use ***faceCapture.py*** to capture you face and save it to the "faces" folder. But first, you need to get the Cascades from: https://github.com/codingforentrepreneurs/OpenCV-Python-Series/tree/master/src/cascades/data

After you have downloaded the cascade, place

cascades/data/ folder

in 

portfolio/Python Projects/facial_recognition/ 

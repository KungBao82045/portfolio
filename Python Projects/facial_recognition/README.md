<h1>FAQ</h1>

<p>Q: I got IndexError: list index out of range.</p>
<p>A: There must be an image does not contain faces or the faces is too inaccurate. Find it in 'faces' folder and delete it by right clicking it and click delete.</p><br>

<p>Q: This script doesn't recognize me</p>
<p>A: Make sure your face image is accurate enough. High quality, good angle will increase the chance to recognize you.</p>

---

<h2>How to use face recognition (step-by-step)</h2>

1. Download or clone my project: https://github.com/KungBao82045/portfolio.git

2. Navigate the folder to `Python Projects` > `facial_recognition`

3. Just in case you have some missing modules. Install these libraries:

`pip3 install numpy`,
`pip3 install face_recognition` and
`pip3 install opencv-python`


4. The file you are using for facial recognition is `face_reco_webcam.py` Before running this file, create a folder named `faces`

      

4. The file you are using for facial recognition is `face_reco_webcam.py` Before running this file, create a folder named `faces`
   

5. Inside the `faces` folder you just created, add images of person's face. It should format like this `your_name_example.png` Replace `your_name_example` with your name and save it as a PNG file.

6. Run the script. It will display green box around any faces it recognizes and names under the box. If a person's face is not inside the `faces` folder, it will display as "Unknown" under the box.


**_IMPORTANT_**: Make sure to run `face_reco_webcam.py` from `face_recognition` folder. If you run it from different folder, it may not work.

***IMPORTANT***: Make sure to run `face_reco_webcam.py` from `face_recognition` folder. If you run it from different folder, it may not work.
refs/remotes/origin/main

---

OPTIONAL: You can use `faceCapture.py` to capture you face and save it to the `faces` folder. But first, you need to download the Cascades to capture faces: https://github.com/codingforentrepreneurs/OpenCV-Python-Series/tree/master/src/cascades/data

After you have downloaded the cascade, place

`cascades/data/` folder

in

`portfolio/Python Projects/facial_recognition/`

import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime 
import pandas as pd

video_capture = cv2.VideoCapture(0)

ratanTata_image = face_recognition.load_image_file("ratanTata.jpg")
ratanTata_encoding = face_recognition.face_encodings(ratanTata_image)[0]

# _image = face_recognition.load_image_file(".jpg")
# _encoding = face_recognition.face_encodings(_image)[0]

# _image = face_recognition.load_image_file(".jpg")
# _encoding = face_recognition.face_encodings(_image)[0]

# _image = face_recognition.load_image_file(".jpg")
# _encoding = face_recognition.face_encodings(_image)[0]

# _image = face_recognition.load_image_file(".jpg")
# _encoding = face_recognition.face_encodings(_image)[0]

known_face_encoding = [
    ratanTata_encoding,
    # _encoding,
    # _encoding,
    # _encoding,
    # _encoding

]

known_faces_names = [
    "ratanTata",
    # "",
    # "",
    # "",
    # "",
]

students = known_faces_names.copy()

face_locations = []
face_encoding = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame =small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame) 
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations) 
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding) 
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H:%M")
                    lnwriter.writerow([name,current_time])
                    
               
                    
    cv2.imshow("attendence system", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
       break
          
video_capture.release()
cv2.destroyAllWindows() 
f.close()
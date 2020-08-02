import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime
import time
import pandas as pd
from webcam_image_capture import capture

path = '/Users/hk/Desktop/FaceID_Login_openCV/BasicImages'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    if cl == ".DS_Store":
        continue
    else:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])

# print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    df = pd.read_csv('/Users/hk/Desktop/FaceID_Login_openCV/Users.csv')
    # print(list(df.Name))
    if name in list(df.Name):
        print("Login")
    elif name == "Unknown":
        print("Please sign up")
        n = str(input("Enter your name:"))
        capture(n)
        df.loc[len(df)] = [n] #;print(df)
        df.to_csv(r'/Users/hk/Desktop/FaceID_Login_openCV/Users.csv', index=False)


encodeListKnown = findEncodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

proceed = True
while proceed:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)
        #print(matchIndex)

        if faceDis[matchIndex] < 0.50:
            name = classNames[matchIndex]  # .upper()
            # print(name)
            markAttendance(name)
            proceed = False
            # time.sleep(5)
        else:
            name = 'Unknown'
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            proceed = False
            # time.sleep(5)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
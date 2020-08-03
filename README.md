# FaceID login System using openCV

## To execute, run following command in terminal
``` python loginapp.py ```

## About:
- After running the above command, webcam turns on(if using external webcam, change to ```VideoCapture(1)```) and verifies your face with existing images in Images folder. If there is a match, it prints out ```Welcome <name>```, else it takes a snap and asks the user to enter his name. After entering your name, your image can be found in Images folder and your name in ```Users.csv```.

## Required packages:
- opencv-python
- numpy
- pandas
- face-recognition
- dlib

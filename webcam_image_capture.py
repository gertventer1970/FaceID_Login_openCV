import cv2
import os

def capture(name):

    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)

    path = '/Users/hk/Desktop/FaceID_Login_openCV/Images'

    while True:
        try:
            check, frame = webcam.read()
            # print(check)  # prints true as long as the webcam is running
            # print(frame)  # prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)

            cv2.imwrite(os.path.join(path, name + '.jpg'), img=frame)
            webcam.release()
            #img_new = cv2.imread(name + '.jpg', cv2.IMREAD_GRAYSCALE)
            #img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Image saved!")

            break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

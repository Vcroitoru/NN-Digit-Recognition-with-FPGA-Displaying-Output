import cv2
import numpy as np
import serial
import time
from keras.models import load_model

cap = cv2.VideoCapture(0)
WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

model = load_model('digits.h5')

def predict(image, model):
    img = cv2.resize(image, (28, 28))
    img = img / 255.0
    img = np.reshape(img,(1, 28, 28, 1))
    predict = model.predict(img)
    result = np.argmax(predict)
        
    return result

ser = serial.Serial('COM14', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

def send_digit(digit):
    """ Send a digit to the Arduino. """
    if 0 <= digit <= 9:
        ser.write(str(digit).encode())


while True: 
    _, frame = cap.read()

    frame_copy = frame.copy()
    cv2.imshow("input", frame_copy)

    key = cv2.waitKey(1) & 0xff

    if key == ord('a'):
        break

    if key == ord('q'):

        r = cv2.selectROI(frame)
        #Crop image 
        screen_shot = frame[int(r[1]):int(r[1]+r[3]),  
                        int(r[0]):int(r[0]+r[2])] 
        screen_shot = screen_shot[:,:,0]
        cv2.imshow("Screenshot", screen_shot)
        # Filename 
        img=cv2.resize(screen_shot, (28,28))
        
        filename = 'savedImage.jpg'

        cv2.imwrite(filename, screen_shot)
        
        result = predict(screen_shot, model)
        print(result)

        send_digit(result)  

        # Close the serial connection
        ser.close()


    continue
    


cv2.destroyAllWindows()
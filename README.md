# NN-Digit-Recognition-with-FPGA-Displaying-Output
Camera Input image for digit recognition to DE1_SOC Fpga which displays outputs and has arithmetic functionality.

## Materials Required
* DE-1 SOC FPGA
* Arduino Due
* Python (OpenCV, Tensorflow, Keras)
* Arduino IDE

## System Diagram
<img src="NN Block Diagram.svg"
     alt="System Diagram"/>

## To run program
* python mnist.py
  * Writes MNIST dataset through CNN into a h.5 file and saves model
* python camera.py
  * Starts up camera through OpenCV and then you can display a digit in frame
  * Next press "Q" on keyboard to select an ROI that will be saved
  * Image is sent through keras.model.predict() to get a prediction of what digit was presented to Arduino
 
## FPGA Interaction
Arithmetic Functionality on FPGA Board through buttons
### Addition 
<img src="addition.png"
     alt="Addition"/>

### Division
<img src="division.png"
     alt="Division"/>

### Subtraction
<img src="subtraction.png"
     alt="Subtraction"/>

### Multiplication
<img src="multiplication.png"
     alt="Multiplication"/>

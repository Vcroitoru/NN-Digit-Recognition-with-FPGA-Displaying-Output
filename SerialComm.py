import serial
import time


ser = serial.Serial('COM14', 9600, timeout=1)
time.sleep(2)  # Wait for the connection to establish

def send_digit(digit):
    """ Send a digit to the Arduino. """
    if 0 <= digit <= 9:
        ser.write(str(digit).encode())

# Example usage
send_digit(2)  # Sends the digit '3' to the Arduino

# Close the serial connection
ser.close()

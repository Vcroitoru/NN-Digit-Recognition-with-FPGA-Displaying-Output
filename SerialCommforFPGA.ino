const int outputPins[] = {2, 3, 4, 5}; // Digital pins used for output

void setup() {
  Serial.begin(9600);  // Start the serial communication
  for (int i = 0; i < 4; i++) {
    pinMode(outputPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {
    char digit = Serial.read();
    if (digit >= '0' && digit <= '9') {
      setDigit(digit - '0');
    }
  }
}

void setDigit(int digit) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(outputPins[i], (digit >> i) & 0x01);
  }
}

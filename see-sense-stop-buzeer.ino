// Define buzzer pin (D6)
const int buzzerPin = D6;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set buzzer pin as output
  pinMode(buzzerPin, OUTPUT);

  // Initialize buzzer state
  digitalWrite(buzzerPin, LOW);
}

void loop() {
  // Check if data is available to read from serial port
  if (Serial.available() > 0) {
    // Read the incoming byte
    char command = Serial.read();

    // Check the received command
    if (command == 'b') {
      // Activate the buzzer
      digitalWrite(buzzerPin, HIGH);
    } else if (command == 's') {
      // Deactivate the buzzer
      digitalWrite(buzzerPin, LOW);
    }
  }
}
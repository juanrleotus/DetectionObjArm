#include <Servo.h>
Servo myservo;

void setup() {
  myservo.attach(9); // Conectar al pin del servo a calibrar
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int angle = Serial.parseInt();
    myservo.write(angle);
    Serial.print("Movido a: ");
    Serial.println(angle);
  }
}
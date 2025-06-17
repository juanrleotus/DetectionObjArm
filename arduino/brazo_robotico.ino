#include <Servo.h>

// Pines de los servos
const int pinBase = 3;
const int pinHombro = 5;
const int pinCodo = 6;
const int pinPinza = 9;

Servo base, hombro, codo, pinza;

void setup() {
  Serial.begin(9600);
  
  base.attach(pinBase);
  hombro.attach(pinHombro);
  codo.attach(pinCodo);
  pinza.attach(pinPinza);
  
  // Posición inicial
  moverServos(90, 90, 90, 50);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    procesarComando(command);
  }
}

void procesarComando(String cmd) {
  // Formato: "BASE:90,HOMBRO:45,CODO:80,PINZA:30"
  // Implementa el parsing según tus necesidades
}

void moverServos(int angBase, int angHombro, int angCodo, int angPinza) {
  base.write(angBase);
  hombro.write(angHombro);
  codo.write(angCodo);
  pinza.write(angPinza);
}
#include <Servo.h>

Servo ilaclamaServosu;

// Pin Tanımlamaları [cite: 591-597, 686-693]
const int SERVO_PIN = 9;
const int IN1 = 4;
const int IN2 = 5;
const int IN3 = 6;
const int IN4 = 7;
const int ENA = 3;
const int ENB = 11;

char gelen_veri;

void setup() {
  Serial.begin(9600); // UART Haberleşme Başlatma [cite: 600]
  ilaclamaServosu.attach(SERVO_PIN);
  ilaclamaServosu.write(0); // Başlangıç konumu

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  
  robotu_durdur(); // Başlangıçta güvenli duruş
}

void loop() {
  if (Serial.available() > 0) {
    gelen_veri = Serial.read(); // Raspberry Pi'den gelen veriyi oku [cite: 614-615]
    
    if (gelen_veri == 'I') { // Durum: SAĞLIKLI -> İlerle [cite: 719]
      ileri_git(150);
      ilaclamaServosu.write(0);
    } 
    else if (gelen_veri == 'H') { // Durum: HASTALIKLI -> Dur ve İlaçla [cite: 620, 733]
      robotu_durdur();
      delay(500);
      ilaclama_yap();
    }
  }
}

void ileri_git(int hiz) {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, hiz);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, hiz);
}

void robotu_durdur() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}

void ilaclama_yap() {
  ilaclamaServosu.write(180); // İlaçlama pozisyonu [cite: 653, 745]
  delay(3000); // 3 saniye ilaçlama [cite: 654, 750]
  ilaclamaServosu.write(0); // Eski konuma dön
  delay(1000);
}

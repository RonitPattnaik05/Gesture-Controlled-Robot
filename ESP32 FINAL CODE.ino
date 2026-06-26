 ESP32 FINAL CODE 
File: flex_2_mpu_bt.ino 
File: flex_2_mpu_bt.ino 
#include <Wire.h> 
#include <MPU6050.h> 
#include "BluetoothSerial.h" 
 
BluetoothSerial SerialBT; 
MPU6050 mpu; 
 
#define FLEX1 32 
#define FLEX2 33 
 
unsigned long lastSendTime = 0; 
const unsigned long SEND_INTERVAL = 50; 
 
void setup() { 
  Serial.begin(115200); 
  delay(500); 
 
 
 
  pinMode(FLEX1, INPUT); 
  pinMode(FLEX2, INPUT); 
 
  Wire.begin(21, 22); 
  mpu.initialize(); 
 
  if (!mpu.testConnection()) { 
    Serial.println("MPU6050 FAILED"); 
    while (1); 
  } 
 
  SerialBT.begin("ESP32_GLOVE"); 
  Serial.println("Bluetooth Started: ESP32_GLOVE"); 
} 
 
void loop() { 
  if (millis() - lastSendTime >= SEND_INTERVAL) { 
    lastSendTime = millis(); 
    if (SerialBT.hasClient()) { 
      sendData(); 
    } 
 
 
  } 
} 
 
void sendData() { 
  int f1 = analogRead(FLEX1); 
  int f2 = analogRead(FLEX2); 
 
  int16_t ax, ay, az, gx, gy, gz; 
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz); 
 
  String data = 
    String(f1) + "," + String(f2) + "," + 
    String(ax / 16384.0, 3) + "," + 
    String(ay / 16384.0, 3) + "," + 
    String(az / 16384.0, 3) + "," + 
    String(gx / 131.0, 3) + "," + 
    String(gy / 131.0, 3) + "," + 
    String(gz / 131.0, 3); 
 
  SerialBT.println(data); 
}
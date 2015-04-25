/*
  Yún HTTP Client
 
 This example for the Arduino Yún shows how create a basic
 HTTP client that connects to the internet and downloads
 content. In this case, you'll connect to the Arduino
 website and download a version of the logo as ASCII text.
 
 created by Tom igoe
 May 2013
 
 This example code is in the public domain.
 
 http://arduino.cc/en/Tutorial/HttpClient
 
 */
 
#include <Bridge.h>
#include <HttpClient.h>
 
void setup() {
  // Bridge takes about two seconds to start up
  // it can be helpful to use the on-board LED
  // as an indicator for when it has initialized
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(12, LOW);
  Bridge.begin();
  digitalWrite(12, HIGH);
}
 
void loop() {
  // Initialize the client library
  HttpClient client;
 
  // Make a HTTP request:
  client.get("http://192.168.1.6:8000/index.txt");
 
  // if there are incoming bytes available
  // from the server, read them and print them:
  while (client.available()) {
    char c = client.read();
    int pinNumber = c - '0';
    
    if (pinNumber == 0) {
      digitalWrite(12, 1);
      delay(1000);
      digitalWrite(12, 0);
    }
    
    if (pinNumber == 1) {
      digitalWrite(13, 1);
      delay(1000);
      digitalWrite(13, 0);
    }
    delay(500);
  }
  delay(10000);
}
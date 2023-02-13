#include <WiFi.h>
#include "encryption.h"
const char* ssid = "Det_ved_jeg";
const char* password =  "Vfp62rxu";
 
const uint16_t port = 8090;
const char * host = "192.168.1.247";
 
void setup()
{
 
  Serial.begin(115200);
  Serial.println(client_full_key);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    Serial.println("Connected to server successful!");
    String test[] ={"50","2","54","345","9"};
    client.print(test[1]);
 
    Serial.println("Disconnecting...");
    client.stop();
 
    delay(10000);
}

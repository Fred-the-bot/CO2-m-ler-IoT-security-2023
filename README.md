# CO-måler-IoT-security-2023

Besked fra Henning:
Der findes mange simple metoder og biblioteker til at kryptere tekst, både til python og arduino, det er for simpelt at udnytte dem. find på jeres egen istedet


Projektet består af en cloud server hosted i Azure (håbefuldt rykkes til egen server)



1 ESP32 som måler CO og sender resultatet til cloud.
Se plantUML nedunder:


![image](https://user-images.githubusercontent.com/32704145/217624407-7782ff0a-c591-4cd5-bf04-c9df263d4730.png)






Resultaterne skal sende fra ESP32 med en hjemmebrygget krypterings metode.
ESP32 skal forbindes til hjemme wifi ved hjælp af "Captive Portal" (Skal/bør sikres med HTTPS)

Der gøres brug af en diffehelman key exchange til at kryptere beskederne med for at skulle undgå en hacker.
![image](https://user-images.githubusercontent.com/32704145/217820943-8d92fcbf-a589-4ad0-9f90-a15ce0c91ef4.png)

https://techtutorialsx.com/2018/04/18/esp32-arduino-encryption-using-aes-128-in-ecb-mode/

## Things to Do ##
&#x2611; Create checklist


#### ESP32 ####
&#x2610; Connect screen to ESP32

&#x2610; Connect CO måler til ESP32

&#x2611; Create encryption on ESP32

&#x2610; Secure OTA update

#### Listening server ####
&#x2611; Create listening server

&#x2610; Connect listening server to thingspeak

&#x2611; Create decryption on listening server

#### Hacking ####
&#x2610; Hack into wifi

&#x2610; Capture packet with info

&#x2610; Modify data

&#x2610; Remail undetected

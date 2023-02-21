# CO2-måler-IoT-security-2023

Besked fra Henning:
Der findes mange simple metoder og biblioteker til at kryptere tekst, både til python og arduino, det er for simpelt at udnytte dem. find på jeres egen istedet


Projektet består af en cloud server hosted i Azure (håbefuldt rykkes til egen server)

1 ESP32 som måler CO2 og sender resultatet til cloud.
Se plantUML nedunder:


![image](https://user-images.githubusercontent.com/32704145/217624407-7782ff0a-c591-4cd5-bf04-c9df263d4730.png)






Resultaterne skal sende fra ESP32 med en hjemmebrygget krypterings metode.


Der gøres brug af en diffehelman key exchange til at kryptere beskederne med for at skulle undgå en hacker.
![image](https://user-images.githubusercontent.com/32704145/217820943-8d92fcbf-a589-4ad0-9f90-a15ce0c91ef4.png)

https://techtutorialsx.com/2018/04/18/esp32-arduino-encryption-using-aes-128-in-ecb-mode/


&#x2610; Connect screen to ESP32

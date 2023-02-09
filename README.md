# CO2-måler-IoT-security-2023



Projektet består af en cloud server hosted i Azure (håbefuldt rykkes til egen server)

1 ESP32 som måler CO2 og sender resultatet til cloud.
Se plantUML nedunder:


![image](https://user-images.githubusercontent.com/32704145/217624407-7782ff0a-c591-4cd5-bf04-c9df263d4730.png)






Resultaterne skal sende fra ESP32 med en hjemmebrygget krypterings metode.


Der gøres brug af en diffehelman key exchange til at kryptere beskederne med for at skulle undgå en hacker.
![image](https://user-images.githubusercontent.com/32704145/217820943-8d92fcbf-a589-4ad0-9f90-a15ce0c91ef4.png)

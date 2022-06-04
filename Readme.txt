Dette projekt er blevet lavet af 2 semesters studiegruppe A5 @2022

Filerne i RasbperryPi mappen skal downloades ned til din Raspberry Pi, og ESP32 filerne skal downloades ned til din ESP32 der er konfigureret til MicroPython

Før du kører programmet på din Raspberry Pi skal du sørge for at terminallen er i den samme mappe som filerne er gemt, eller
tilføje stilnavnet hvor filen er gemt foran .py filen e.g. sudo  python /home/pi/Desktop/lukkeTjekWebServer.py

For at køre koden på Raspberry Pi brug kommandoen:
sudo python lukkeTjekWebServer.py & python socketServer.py

Vent på webserveren er oppe og kører og forbind din ESP32 til strøm, hvis du forbandt ESP32eren til strøm før du kørte koden på din
Raspberry Pi, skal ESP32eren genstartes ved at trykke på knappen ved siden af USB C forbindelsen hvor der står "EN" under knappen

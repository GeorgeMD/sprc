# SPRC Tema 3 - IoT Platform
**Diaconu George-Marius 342 C3**
##### Recomandare: Cititi acest README cu un editor ce suporta Markdown.

Descrierea componentelor:
1. eclipse-mosquitto
    - Broker-ul de mesaje MQTT
    - L-am ales pentru ca este open source si suporta protocolul MQTT by default. Prin comparatie, rabbitmq, cealalata varianta open source sugerata de hub.docker.com suporta MQTT printr-un plugin.
2. Adapter MQTT to influxdb:
    - L-am scris in python, pentru ca este simplu si rapid.
    - Adaptorul asculta pe toate topic-urile, dar prelucreaza doar mesajele ce vin pe topicuri de forma locatie/statie. De asemenea, daca mesajul nu poate fi parsat ca json, se scrie in log (daca variabila DEBUG_DATA_FLOW este setata la valoarea "true") si mesajul este ignorat.
    - In baza de date am scris intrarile ca linii de forma:  
      ```
      masuratoare, statie, locatie value timestamp
      BAT, location=UPB, station=rpi_1 value=65 1577750012
      ```
    - Am folosit bibliotecile paho-mqtt si influxdb pentru a comunica cu broker-ul si cu baza de date.
3. influxdb:
    - Baza de date de tipul TSDB.
    - Retentia datelor by default este infinita, asadar nu am avut nimic de configurat.
4. grafana:
    - Aplicatia de vizualizare.
    - Configuratiile sunt pastrate in directorul `volumes/grafana` din arhiva. Acestea sunt copiate la prima rulare in $SPRC_DVP

Prima rulare:  
`./run.sh`  
(este nevoie ca variabila `SPRC_DVP` sa fie definita pe tot parcursul verificarii temei, intrucat ea este folosita atat in script cat si in `stack.yml`)

Pentru a opri serviciile:  
`docker stack rm sprc3`

Pentru a le reporni:  
`docker stack deploy -c stack.yml sprc3`

Am inclus si un script de cleanup care opreste serviciile, sterge imaginea adaptorului si sterge volumul asociat bazei de date:  
`./cleanup.sh`

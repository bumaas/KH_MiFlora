

Installation eines Raspberry Pi Zero W

Ein Raspberry Pi Zero lässt sich gut "headless", das heißt ohne angeschlossene Tastatur und Maus installieren.

Eine gute Anleitung findet sich hier https://desertbot.io/blog/headless-pi-zero-w-wifi-setup-windows

Zusammenfassung in wenigen Worten:
- die benötigte bibliothek gattlib lässt sich nicht unter Raspbian Buster (vom 2019-07-12) und auch nicht unter Stretch (vom 2019-04-08) kompilieren
- stattdessen ist Jessie zu installieren (http://downloads.raspberrypi.org/raspbian/images/raspbian-2017-07-05/)
- Image mit Etcher (balenaEtcher) auf die SD Karte übertragen, SD-Karte auswerfen und neu verbinden
- SSH und wpa_supplicant.conf Dateien laut Schritt 3 und 4 vorbereiten und auf die Boot Partition kopieren
- SD Karte in Raspberry stecken und mit Strom versorgen
- nach ca. einer Minute ist der Raspi im WLAN sichtbar
- mit Putty auf dem Raspi anmelden: Host: sudo su, User: pi, Passwort: raspberry
- Hostname und Passwort mit 'sudo raspi-config' ändern und neu booten
- zum Superuser werden
sudo su
- aktuelle Updates beziehen
apt-get update -y
apt-get upgrade -y

Damit ist die Installation des Betriebssystems fertig. Weiter geht es Richtung MyFlora

- Swapfile einrichten und temporär einschalten
su -c 'echo "CONF_SWAPSIZE=1024" > /etc/dphys-swapfile'
dphys-swapfile setup
dphys-swapfile swapon

überprüfen mit
free -m

später wieder ausschalten:
dphys-swapfile swapon

- auf Lite muss noch git installiert werden
apt-get install git

cd /home/pi
git clone https://github.com/open-homeautomation/miflora.git
cd miflora
wget https://raw.githubusercontent.com/bumaas/KH_MiFlora/master/docs/GetMiFloras.py

- Python und andere Pakete installieren
apt-get install python3 libglib2.0-dev libbluetooth-dev python3-pip apache2 libboost-python-dev libboost-thread-dev

Gattlib installieren, dauert 15 Minuten:
pip3 install gattlib

pip3 install btlewrap

Alternative (siehe https://stackoverflow.com/questions/55178684/installing-gattlib-for-pybluez):
pip3 install pygattlib

Testen mit

python3 GetMiFloras.py

Bei einem Fehler in Form von
	RuntimeError: Set scan parameters failed (are you root?)
einmal 
hciconfig hci0 reset


crontab -e

Neuer Eintrag am Ende
*/10 * * * * python3 /home/pi/miflora/GetMiFloras.py > /var/www/html/plants.log



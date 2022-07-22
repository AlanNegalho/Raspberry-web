video streaming using raspiberry, flask, open cv

Essential Libraries to install

sudo apt-get install libopenjp2-7-dev

sudo apt-get install libhdf5-dev

sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test

sudo apt-get install libatlas-base-dev

sudo apt-get install libjasper-dev

sudo apt-get install python3-pip

sudo apt-get install python3-h5py

sudo apt-get install python3-opencv

sudo pip3 install flask


Wfi Settings for Raspbian OS
File Name: wpa_supplicant.conf
Contents:
  country="YOUR COUNTRY CODE"
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  network={
        ssid="YOUR_NETWORK_NAME"
        psk="YOUR_PASSWORD"
        key_mgmt=WPA-PSK
  }


Known Issues
if you face any issue while installing library like python3-opencv or flask,
then run the "sudo apt-get update --fix-missing" command first.


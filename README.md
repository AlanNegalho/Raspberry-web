LiveStramingCamera
DIY live streaming camera using raspberry pi, opencv, flask and remote.it

Essential Libraries to install
echo Y |sudo apt-get install libopenjp2-7-dev

echo Y | sudo apt-get install libhdf5-dev

echo Y |sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test

echo Y | sudo apt-get install libatlas-base-dev

echo Y | sudo apt-get install libjasper-dev

echo Y | sudo apt-get install python3-pip

echo Y | sudo apt-get install python3-h5py

echo Y | sudo apt-get install python3-opencv

echo Y | sudo pip3 install flask

sudo apt install remoteit

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


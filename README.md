# can-py-tool

Link to PiCAN 2 SMPS USER GUIDE
http://skpang.co.uk/catalog/images/raspberrypi/pi_2/PICAN2SMPSUGB.pdf

How-to set up a virtual can bus

sudo modprobe vcan
# Create a vcan network interface with a specific name
sudo ip link add dev vcan0 type vcan
sudo ip link set vcan0 up



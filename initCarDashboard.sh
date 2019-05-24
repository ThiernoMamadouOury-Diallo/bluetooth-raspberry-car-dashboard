#!/bin/bash

#enable bluetooth
sudo systemctl start bluetooth

sleep 1

#run the program bluez
echo -e 'power on \nquit' | bluetoothctl

echo -e 'agent on \nquit' | bluetoothctl

# active pairing
echo -e 'paraible on \nquit' | bluetoothctl

# change bluetooth visibiliy
echo -e 'discoverable on \nquit' | bluetoothctl

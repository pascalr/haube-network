Wifi:
hostapd pour créer un Access Point sur le serveur:
1. Check AP Support: iw list | grep -A 10 "Supported interface modes"
2. Set the Static IP: Voir plus bas
3. Edit hostapd.conf: In /etc/hostapd/hostapd.conf:




Method 1: The "Systemd Service" Way (Recommended)

Since hostapd and dnsmasq are services, we can create a small script that ensures the IP is set right before they start.

    Create a simple shell script: sudo nano /usr/local/bin/setup-hotspot-ip.sh

    Paste this into the file:
    Bash

#!/bin/bash
# Ensure the interface is up and has an IP
ip link set wlxec750c5ed0ea up
ip addr add 192.168.1.1/24 dev wlxec750c5ed0ea

Make it executable: sudo chmod +x /usr/local/bin/setup-hotspot-ip.sh

Edit the hostapd service to run this first: sudo systemctl edit hostapd (This opens a blank file; add these lines):
Plaintext

[Service]
ExecStartPre=/usr/local/bin/setup-hotspot-ip.sh








To disable all sleep/suspend:
Bash

sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

To re-enable it later:
Bash

    sudo systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target

    Note: This is very effective, but it will also prevent you from manually putting the computer to sleep from the Power menu.

# PiPing
Unicornhat based Python Program for the Raspberry Pi.

PiPing is a tiny monitoring tool started to monitor my own Home Lab Network with a Raspberry Pi.
It will show you wether a system is online or offline via Unicorn Hat from Pimoroni:
http://shop.pimoroni.com/products/unicorn-hat
https://github.com/pimoroni/unicorn-hat

Key features:
- 16 systems to monitor
- Wake on Lan 
- Power off ESXi or SSH based system
- Integration as a service
- Time scheduled working time

Pre Requirements:
- python 
- etherwake
- sshpass
- Unicorn Hat (Hardware & Software) "\curl -sS get.pimoroni.com/unicornhat | bash"

Files:
- piping.py (Program)
- pipingservice.sh (service)
- clearunicorn.py (clear Unicornhat LED´s Scrypt)

I´m not a professional developer, this is only a home project, that I want to share and maybe get some improvments by other.

Installation:
- Install all pre requirements first!
- Edit piping.py to your requirements.
- Copy files to the following locations on your Raspberry Pi:
# /etc/pipingservice.sh
# /usr/local/bin/piping/piping.py
# /usr/local/bin/piping/clearunicorn.py

- Register service at boot time
# sudo update-rc.d pipingservice.sh defaults

#!/usr/bin/env python

#########################################################################################
# Bibliotheken importieren START
#########################################################################################

import os
import unicornhat as led
import datetime
import time
import base64

#########################################################################################
# Bibliotheken importieren ENDE
#########################################################################################



#########################################################################################
# Variablen START
#########################################################################################

w = 1
p = "1"

starttime = datetime.time(6)
endtime = datetime.time(23, 30)

hosts = ["192.168.222.1", "192.168.111.1", "192.168.111.253", "192.168.111.252",
         "192.168.111.4", "192.168.111.6", "192.168.111.8", "192.168.111.15",
         "192.168.111.10", "192.168.111.11", "192.168.111.12", "192.168.111.13",
         "192.168.111.9", "192.168.111.7", "", "8.8.8.8"]

hostsmac = ["", "", "", "",
            "", "", "", "",
            "10:60:4b:92:79:84", "", "a0:1d:48:c7:07:50", "",
            "", "", "", ""]

led.brightness(0.3)
green = [0, 255, 0]
red = [255, 0, 0]
blue = [0, 0, 255]
purple = [128, 0, 128]
off = [0, 0, 0]
white = [255, 255, 255]
orange = [255, 165, 0]

#########################################################################################
# Variablen ENDE
#########################################################################################



#########################################################################################
# Funktionen Prozeduren START
#########################################################################################

def led_red():
    led.clear()
    for y in range(8):
        for x in range(8):
            led.set_pixel(x, y, red[0], red[1], red[2])
    led.show()
    time.sleep(w)
    return;


def led_green():
    led.clear()
    for y in range(8):
        for x in range(8):
            led.set_pixel(x, y, green[0], green[1], green[2])
    led.show()
    time.sleep(w)
    return;


def led_blue():
    led.clear()
    for y in range(8):
        for x in range(8):
            led.set_pixel(x, y, blue[0], blue[1], blue[2])
    led.show()
    time.sleep(w)
    return;


def led_reset():
    led.clear()
    led.set_pixel(1, 1, orange[0], orange[1], orange[2])
    led.set_pixel(1, 3, orange[0], orange[1], orange[2])
    led.set_pixel(1, 4, orange[0], orange[1], orange[2])
    led.set_pixel(2, 1, orange[0], orange[1], orange[2])
    led.set_pixel(2, 2, orange[0], orange[1], orange[2])
    led.set_pixel(2, 5, orange[0], orange[1], orange[2])
    led.set_pixel(3, 1, orange[0], orange[1], orange[2])
    led.set_pixel(3, 2, orange[0], orange[1], orange[2])
    led.set_pixel(3, 3, orange[0], orange[1], orange[2])
    led.set_pixel(3, 6, orange[0], orange[1], orange[2])
    led.set_pixel(4, 6, orange[0], orange[1], orange[2])
    led.set_pixel(5, 2, orange[0], orange[1], orange[2])
    led.set_pixel(5, 5, orange[0], orange[1], orange[2])
    led.set_pixel(6, 3, orange[0], orange[1], orange[2])
    led.set_pixel(6, 4, orange[0], orange[1], orange[2])
    led.show()
    time.sleep(w)
    return;


def led_router():
    led.clear()
    led.show()
    while not (os.system("ping -c " + p + " " + hosts[1])) == 0:
        h = 0
        wol(hostsmac[8])
        wol(hostsmac[10])
        while h <= 4:
            # arrow 1
            if h == 0:
                led.set_pixel(0, 5, green[0], green[1], green[2])
                led.set_pixel(0, 7, green[0], green[1], green[2])
                led.set_pixel(1, 5, green[0], green[1], green[2])
                led.set_pixel(1, 6, green[0], green[1], green[2])
                led.set_pixel(2, 5, green[0], green[1], green[2])
                led.set_pixel(2, 6, green[0], green[1], green[2])
                led.set_pixel(2, 7, green[0], green[1], green[2])
            else:
                led.set_pixel(0, 5, red[0], red[1], red[2])
                led.set_pixel(0, 7, red[0], red[1], red[2])
                led.set_pixel(1, 5, red[0], red[1], red[2])
                led.set_pixel(1, 6, red[0], red[1], red[2])
                led.set_pixel(2, 5, red[0], red[1], red[2])
                led.set_pixel(2, 6, red[0], red[1], red[2])
                led.set_pixel(2, 7, red[0], red[1], red[2])
            # arrow 2
            if h == 1:
                led.set_pixel(0, 0, green[0], green[1], green[2])
                led.set_pixel(0, 1, green[0], green[1], green[2])
                led.set_pixel(0, 2, green[0], green[1], green[2])
                led.set_pixel(1, 0, green[0], green[1], green[2])
                led.set_pixel(1, 1, green[0], green[1], green[2])
                led.set_pixel(2, 0, green[0], green[1], green[2])
                led.set_pixel(2, 2, green[0], green[1], green[2])
            else:
                led.set_pixel(0, 0, red[0], red[1], red[2])
                led.set_pixel(0, 1, red[0], red[1], red[2])
                led.set_pixel(0, 2, red[0], red[1], red[2])
                led.set_pixel(1, 0, red[0], red[1], red[2])
                led.set_pixel(1, 1, red[0], red[1], red[2])
                led.set_pixel(2, 0, red[0], red[1], red[2])
                led.set_pixel(2, 2, red[0], red[1], red[2])
            # arrow 3
            if h == 2:
                led.set_pixel(5, 0, green[0], green[1], green[2])
                led.set_pixel(5, 1, green[0], green[1], green[2])
                led.set_pixel(5, 2, green[0], green[1], green[2])
                led.set_pixel(6, 1, green[0], green[1], green[2])
                led.set_pixel(6, 2, green[0], green[1], green[2])
                led.set_pixel(7, 0, green[0], green[1], green[2])
                led.set_pixel(7, 2, green[0], green[1], green[2])
            else:
                led.set_pixel(5, 0, red[0], red[1], red[2])
                led.set_pixel(5, 1, red[0], red[1], red[2])
                led.set_pixel(5, 2, red[0], red[1], red[2])
                led.set_pixel(6, 1, red[0], red[1], red[2])
                led.set_pixel(6, 2, red[0], red[1], red[2])
                led.set_pixel(7, 0, red[0], red[1], red[2])
                led.set_pixel(7, 2, red[0], red[1], red[2])
            # arrow 4
            if h == 3:
                led.set_pixel(5, 5, green[0], green[1], green[2])
                led.set_pixel(5, 7, green[0], green[1], green[2])
                led.set_pixel(6, 6, green[0], green[1], green[2])
                led.set_pixel(6, 7, green[0], green[1], green[2])
                led.set_pixel(7, 5, green[0], green[1], green[2])
                led.set_pixel(7, 6, green[0], green[1], green[2])
                led.set_pixel(7, 7, green[0], green[1], green[2])
            else:
                led.set_pixel(5, 5, red[0], red[1], red[2])
                led.set_pixel(5, 7, red[0], red[1], red[2])
                led.set_pixel(6, 6, red[0], red[1], red[2])
                led.set_pixel(6, 7, red[0], red[1], red[2])
                led.set_pixel(7, 5, red[0], red[1], red[2])
                led.set_pixel(7, 6, red[0], red[1], red[2])
                led.set_pixel(7, 7, red[0], red[1], red[2])
            led.show()
            h += 1
            time.sleep(w)
    return;


def led_eth(eth):
    for a in range(7):
        led.set_pixel(a, 0, red[0], red[1], red[2])
        led.set_pixel(a, 4, red[0], red[1], red[2])
    for b in range(5):
        led.set_pixel(0, b, red[0], red[1], red[2])
        led.set_pixel(6, b, red[0], red[1], red[2])
        led.set_pixel(7, b, red[0], red[1], red[2])
    if eth == 0 or eth == 4:
        led.set_pixel(1, 1, blue[0], blue[1], blue[2])
        led.set_pixel(1, 2, blue[0], blue[1], blue[2])
        led.set_pixel(1, 3, blue[0], blue[1], blue[2])
        led.set_pixel(2, 3, blue[0], blue[1], blue[2])
        led.set_pixel(3, 1, blue[0], blue[1], blue[2])
        led.set_pixel(3, 2, blue[0], blue[1], blue[2])
        led.set_pixel(3, 3, blue[0], blue[1], blue[2])
        led.set_pixel(4, 3, blue[0], blue[1], blue[2])
        led.set_pixel(5, 1, blue[0], blue[1], blue[2])
        led.set_pixel(5, 2, blue[0], blue[1], blue[2])
        led.set_pixel(5, 3, blue[0], blue[1], blue[2])
    if eth == 1 or eth == 5:
        led.set_pixel(1, 1, blue[0], blue[1], blue[2])
        led.set_pixel(1, 2, blue[0], blue[1], blue[2])
        led.set_pixel(1, 3, blue[0], blue[1], blue[2])
        led.set_pixel(2, 2, blue[0], blue[1], blue[2])
        led.set_pixel(3, 2, blue[0], blue[1], blue[2])
        led.set_pixel(4, 2, blue[0], blue[1], blue[2])
        led.set_pixel(5, 2, blue[0], blue[1], blue[2])
    if eth == 2 or eth == 6:
        led.set_pixel(1, 1, blue[0], blue[1], blue[2])
        led.set_pixel(1, 3, blue[0], blue[1], blue[2])
        led.set_pixel(2, 1, blue[0], blue[1], blue[2])
        led.set_pixel(2, 3, blue[0], blue[1], blue[2])
        led.set_pixel(3, 1, blue[0], blue[1], blue[2])
        led.set_pixel(3, 2, blue[0], blue[1], blue[2])
        led.set_pixel(3, 3, blue[0], blue[1], blue[2])
        led.set_pixel(4, 1, blue[0], blue[1], blue[2])
        led.set_pixel(4, 3, blue[0], blue[1], blue[2])
        led.set_pixel(5, 1, blue[0], blue[1], blue[2])
        led.set_pixel(5, 3, blue[0], blue[1], blue[2])
    led.show()
    return;


def led_arrow():
    x = 0
    y = 7
    while x <= 6:
        led.set_pixel(x, y, blue[0], blue[1], blue[2])
        led.set_pixel((x + 1), (y - 1), blue[0], blue[1], blue[2])
        led.set_pixel(x, (y - 2), blue[0], blue[1], blue[2])
        led.show()
        # led_eth(x)
        time.sleep(w)
        x += 1
        led.clear()
    return;


def led_poweroff(hostn):
    x = 0
    while (os.system("ping -c " + p + " " + hostn)) == 0:
        led.clear()
        if x == 0:
            # line
            led.set_pixel(0, 3, red[0], red[1], red[2])
            led.set_pixel(0, 4, red[0], red[1], red[2])
            led.set_pixel(1, 3, red[0], red[1], red[2])
            led.set_pixel(1, 4, red[0], red[1], red[2])
            led.set_pixel(2, 3, red[0], red[1], red[2])
            led.set_pixel(2, 4, red[0], red[1], red[2])
            led.set_pixel(3, 3, red[0], red[1], red[2])
            led.set_pixel(3, 4, red[0], red[1], red[2])
            x += 1
        else:
            led.set_pixel(0, 3, blue[0], blue[1], blue[2])
            led.set_pixel(0, 4, blue[0], blue[1], blue[2])
            led.set_pixel(1, 3, blue[0], blue[1], blue[2])
            led.set_pixel(1, 4, blue[0], blue[1], blue[2])
            led.set_pixel(2, 3, blue[0], blue[1], blue[2])
            led.set_pixel(2, 4, blue[0], blue[1], blue[2])
            led.set_pixel(3, 3, blue[0], blue[1], blue[2])
            led.set_pixel(3, 4, blue[0], blue[1], blue[2])
            x = 0
        # ring
        led.set_pixel(1, 1, red[0], red[1], red[2])
        led.set_pixel(1, 6, red[0], red[1], red[2])
        led.set_pixel(2, 0, red[0], red[1], red[2])
        led.set_pixel(2, 7, red[0], red[1], red[2])
        led.set_pixel(3, 0, red[0], red[1], red[2])
        led.set_pixel(3, 7, red[0], red[1], red[2])
        led.set_pixel(4, 0, red[0], red[1], red[2])
        led.set_pixel(4, 7, red[0], red[1], red[2])
        led.set_pixel(5, 0, red[0], red[1], red[2])
        led.set_pixel(5, 7, red[0], red[1], red[2])
        led.set_pixel(6, 1, red[0], red[1], red[2])
        led.set_pixel(6, 6, red[0], red[1], red[2])
        led.set_pixel(7, 2, red[0], red[1], red[2])
        led.set_pixel(7, 3, red[0], red[1], red[2])
        led.set_pixel(7, 4, red[0], red[1], red[2])
        led.set_pixel(7, 5, red[0], red[1], red[2])
        led.show()
        time.sleep(w)


def clearsystem():
    led.clear()
    led.rotation(0)
    os.system("arp -d *")
    os.system("ip neigh flush all")
    led.show()
    return;


def wol(mac):
    os.system("wakeonlan " + mac)
    return;


def led_piping():
    x = 0
    y = 0
    h = 0
    led.clear()
    led.show()
    time.sleep(w)
    while h <= 15:
        if hosts[h] == "":
            led.set_pixel(x, y, blue[0], blue[1], blue[2])
            led.set_pixel(x, (y + 1), blue[0], blue[1], blue[2])
            led.set_pixel((x + 1), y, blue[0], blue[1], blue[2])
            led.set_pixel((x + 1), (y + 1), blue[0], blue[1], blue[2])
            led.show()
        else:
            if (os.system("ping -c " + p + " " + hosts[h])) == 0:
                led.set_pixel(x, y, green[0], green[1], green[2])
                led.set_pixel(x, (y + 1), green[0], green[1], green[2])
                led.set_pixel((x + 1), y, green[0], green[1], green[2])
                led.set_pixel((x + 1), (y + 1), green[0], green[1], green[2])
                led.show()
            else:
                led.set_pixel(x, y, red[0], red[1], red[2])
                led.set_pixel(x, (y + 1), red[0], red[1], red[2])
                led.set_pixel((x + 1), y, red[0], red[1], red[2])
                led.set_pixel((x + 1), (y + 1), red[0], red[1], red[2])
                led.show()
                if h == 8:
                    wol(hostsmac[h])
                if h == 10:
                    wol(hostsmac[h])
        x += 2
        if x == 8:
            x = 0
            y += 2
        h += 1
        time.sleep(w)
    return;


def sshconnect(hostn, b64password, command):
    os.system("sshpass -p " + base64.b64decode(b64password) + " ssh " + hostn + " " + command)
    return;


#########################################################################################
# Funktionen Prozeduren ENDE
#########################################################################################



#########################################################################################
# Hauptprogram START
#########################################################################################

def main():
    while True:
        led.clear()
        led.show()
        timestamp = datetime.datetime.now().time()
        if (os.system("ping -c " + p + " 192.168.111.25")) == 0:
            if starttime <= timestamp <= endtime:
                clearsystem()
                if (os.system("ping -c " + p + " " + hosts[1])) == 0:
                    led_reset()
                    led_piping()
                else:
                    led_reset()
                    led_router()
            else:
                if (os.system("ping -c " + p + " " + hosts[8])) == 0:
                    led.clear()
                    sshconnect(hosts[8], "###################", "poweroff")
                    led_poweroff(hosts[8])
                    led_reset()
                if (os.system("ping -c " + p + " " + hosts[10])) == 0:
                    led.clear()
                    sshconnect(hosts[10], "###################", "poweroff")
                    led_poweroff(hosts[10])
                    led_reset()
                continue
        else:
            led_arrow()
            continue

if __name__ == '__main__':
    main()

#########################################################################################
# Hauptprogram ENDE
#########################################################################################
